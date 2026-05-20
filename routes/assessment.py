"""
routes/assessment.py
====================
GET  /api/assessment/questions          — returns a randomized assessment set
POST /api/assessment/submit             — scores answers, runs ML, returns recommendations
GET  /api/assessment/results/latest     — returns the most recent result for the logged-in user
GET  /api/assessment/results/history    — returns all past results (newest first, capped at 20)
"""

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Any, Optional
from datetime import datetime
import random

from bson import ObjectId
from database import db
from routes.auth import get_current_user
from ml.predictor import get_top5_recommendations

router = APIRouter()

# ── Collections ──────────────────────────────────────────────────────────────
riasec_col   = db["questions_riasec"]
bigfive_col  = db["questions_bigfive"]
aptitude_col = db["questions_aptitude"]
results_col  = db["assessment_results"]

# ── Helpers ──────────────────────────────────────────────────────────────────

def serialize(doc: dict) -> dict:
    doc["_id"] = str(doc["_id"])
    return doc

async def random_sample(collection, query: dict, n: int) -> list:
    docs = await collection.find(query).to_list(length=None)
    if len(docs) < n:
        raise HTTPException(
            status_code=500,
            detail=f"Not enough questions in pool. Need {n}, found {len(docs)}. Query: {query}"
        )
    return [serialize(d) for d in random.sample(docs, n)]


# ── GET /api/assessment/questions ────────────────────────────────────────────

@router.get("/questions")
async def get_questions(current_user=Depends(get_current_user)):
    riasec_codes = ["realistic", "investigative", "artistic", "social", "enterprising", "conventional"]
    riasec = []
    for code in riasec_codes:
        samples = await random_sample(riasec_col, {"subcategory": code, "active": True}, 6)
        riasec.extend(samples)
    random.shuffle(riasec)

    traits = ["openness", "conscientiousness", "extraversion", "agreeableness", "neuroticism"]
    bigfive = []
    for trait in traits:
        samples = await random_sample(bigfive_col, {"subcategory": trait, "active": True}, 5)
        bigfive.extend(samples)
    random.shuffle(bigfive)

    subjects = ["math", "science", "english", "abstract"]
    aptitude = {}
    for subject in subjects:
        subject_qs = []
        for difficulty in ["easy", "medium", "hard"]:
            samples = await random_sample(
                aptitude_col,
                {"subject": subject, "difficulty": difficulty, "active": True},
                4
            )
            subject_qs.extend(samples)
        random.shuffle(subject_qs)
        aptitude[subject] = subject_qs

    return {"riasec": riasec, "bigfive": bigfive, "aptitude": aptitude}


# ── POST /api/assessment/submit ──────────────────────────────────────────────

class SubmitRequest(BaseModel):
    strand:           str
    riasec_answers:   dict   # { question_id: 1-5 }
    bigfive_answers:  dict   # { question_id: 1-5 }
    aptitude_answers: dict   # { question_id: "A"|"B"|"C"|"D" }


@router.post("/submit")
async def submit_assessment(data: SubmitRequest, current_user=Depends(get_current_user)):

    # ── 1. RIASEC — sum raw Likert scores per code ───────────────────────────
    riasec_oids = [ObjectId(qid) for qid in data.riasec_answers.keys()]
    riasec_docs = await riasec_col.find({"_id": {"$in": riasec_oids}}).to_list(length=None)

    riasec_raw = {
        code: 0 for code in
        ["realistic", "investigative", "artistic", "social", "enterprising", "conventional"]
    }
    for doc in riasec_docs:
        code  = doc["subcategory"]
        score = data.riasec_answers[str(doc["_id"])]
        riasec_raw[code] += score

    # ── 2. Big Five — average per trait, applying reverse scoring ────────────
    bigfive_oids = [ObjectId(qid) for qid in data.bigfive_answers.keys()]
    bigfive_docs = await bigfive_col.find({"_id": {"$in": bigfive_oids}}).to_list(length=None)

    trait_buckets: dict[str, list[float]] = {
        t: [] for t in ["openness", "conscientiousness", "extraversion", "agreeableness", "neuroticism"]
    }
    for doc in bigfive_docs:
        trait = doc["subcategory"]
        raw   = data.bigfive_answers[str(doc["_id"])]
        score = (6 - raw) if doc.get("reverse_scored", False) else raw
        trait_buckets[trait].append(score)

    bigfive_raw = {
        trait: round(sum(scores) / len(scores), 4) if scores else 3.0
        for trait, scores in trait_buckets.items()
    }

    # ── 3. Aptitude — count correct answers per subject ──────────────────────
    aptitude_oids = [ObjectId(qid) for qid in data.aptitude_answers.keys()]
    aptitude_docs = await aptitude_col.find({"_id": {"$in": aptitude_oids}}).to_list(length=None)

    subject_tally: dict[str, dict] = {
        s: {"correct": 0, "total": 0}
        for s in ["math", "english", "science", "abstract"]
    }
    for doc in aptitude_docs:
        subject = doc["subject"]
        given   = data.aptitude_answers[str(doc["_id"])]
        subject_tally[subject]["total"]   += 1
        subject_tally[subject]["correct"] += int(given == doc["correct_answer"])

    aptitude_pct = {
        subj: round(v["correct"] / v["total"] * 100, 1) if v["total"] else 0.0
        for subj, v in subject_tally.items()
    }

    # ── 4. Run ML model ──────────────────────────────────────────────────────
    recommendations = get_top5_recommendations(
        riasec_raw   = riasec_raw,
        bigfive_raw  = bigfive_raw,
        aptitude_pct = aptitude_pct,
        strand       = data.strand,
    )

    # ── 5. Persist everything ────────────────────────────────────────────────
    result_doc = {
        "userId":  current_user["id"],
        "email":   current_user["email"],
        "strand":  data.strand,

        "riasec_answers":   data.riasec_answers,
        "bigfive_answers":  data.bigfive_answers,
        "aptitude_answers": data.aptitude_answers,

        "scores": {
            "riasec_raw":   riasec_raw,
            "bigfive_raw":  bigfive_raw,
            "aptitude_pct": aptitude_pct,
        },

        "recommendations": recommendations,
        "status":          "completed",
        "submittedAt":     datetime.utcnow(),
    }

    result = await results_col.insert_one(result_doc)

    return {
        "message":         "Assessment submitted successfully.",
        "result_id":       str(result.inserted_id),
        "status":          "completed",
        "recommendations": recommendations,
    }


# ── GET /api/assessment/results/latest ───────────────────────────────────────
# Returns the most recent completed result for the logged-in user.
# Used by the Dashboard to populate all profile sections.

@router.get("/results/latest")
async def get_latest_result(current_user=Depends(get_current_user)):
    doc = await results_col.find_one(
        {"userId": current_user["id"], "status": "completed"},
        sort=[("submittedAt", -1)],
    )
    if not doc:
        raise HTTPException(status_code=404, detail="No results found.")

    return {
        "result_id":       str(doc["_id"]),
        "strand":          doc["strand"],
        "submittedAt":     doc["submittedAt"].isoformat(),
        "scores": {
            "riasec_raw":   doc["scores"]["riasec_raw"],
            "bigfive_raw":  doc["scores"]["bigfive_raw"],
            "aptitude_pct": doc["scores"]["aptitude_pct"],
        },
        "recommendations": doc["recommendations"],  # [{ rank, course, confidence }]
    }


# ── GET /api/assessment/results/history ──────────────────────────────────────
# Returns all past results (newest first) — used by the History drawer.

@router.get("/results/history")
async def get_results_history(current_user=Depends(get_current_user)):
    cursor = results_col.find(
        {"userId": current_user["id"], "status": "completed"},
        sort=[("submittedAt", -1)],
    )
    docs = await cursor.to_list(length=20)

    return [
        {
            "result_id":       str(doc["_id"]),
            "strand":          doc["strand"],
            "submittedAt":     doc["submittedAt"].isoformat(),
            "scores": {
                "riasec_raw":   doc["scores"]["riasec_raw"],
                "bigfive_raw":  doc["scores"]["bigfive_raw"],
                "aptitude_pct": doc["scores"]["aptitude_pct"],
            },
            "recommendations": doc["recommendations"],
        }
        for doc in docs
    ]