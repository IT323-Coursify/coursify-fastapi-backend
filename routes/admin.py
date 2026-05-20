"""
routes/admin.py
===============
Admin and Superadmin API routes for Coursify.

ADMIN endpoints (admin + superadmin):
  GET  /api/admin/analytics                        → user stats, registration trend
  GET  /api/admin/analytics/courses                → course recommendation trends
  GET  /api/admin/analytics/assessments            → submission stats + trend
  GET  /api/admin/questions                        → list questions (all pools)
  POST /api/admin/questions                        → add a question
  PUT  /api/admin/questions/{id}                   → edit a question
  PATCH /api/admin/questions/{id}/toggle           → activate / deactivate a question

SUPERADMIN-only endpoints:
  GET  /api/admin/users                            → paginated user list
  PUT  /api/admin/users/{user_id}/role             → change role
  PUT  /api/admin/users/{user_id}/status           → activate / deactivate account
  GET  /api/admin/audit-log                        → flat audit event log
  GET  /api/admin/export/users                     → CSV of all users
"""

from fastapi import APIRouter, HTTPException, Depends, Query
from fastapi.responses import StreamingResponse
from bson import ObjectId
from datetime import datetime, timedelta
from typing import Optional, Literal
import csv
import io

from database import users_collection, db
from middleware.roles import require_admin, require_superadmin
from models import (
    UpdateRoleRequest,
    UpdateStatusRequest,
    QuestionCreateRequest,
    QuestionUpdateRequest,
)

router = APIRouter()

# ── Collections ───────────────────────────────────────────────────────────────
results_col  = db["assessment_results"]
riasec_col   = db["questions_riasec"]
bigfive_col  = db["questions_bigfive"]
aptitude_col = db["questions_aptitude"]

POOL_MAP = {
    "riasec":   riasec_col,
    "bigfive":  bigfive_col,
    "aptitude": aptitude_col,
}

# ── Helpers ───────────────────────────────────────────────────────────────────

def _date_filter(range_str: str) -> Optional[datetime]:
    now = datetime.utcnow()
    if range_str == "7d":
        return now - timedelta(days=7)
    if range_str == "30d":
        return now - timedelta(days=30)
    return None  # "all"


def _user_doc(user: dict) -> dict:
    return {
        "id":         str(user["_id"]),
        "username":   user.get("username", ""),
        "email":      user.get("email", ""),
        "role":       user.get("role", "user"),
        "gradeLevel": user.get("gradeLevel", ""),
        "strand":     user.get("strand", ""),
        "isActive":   user.get("isActive", True),
        "createdAt":  user.get("createdAt", datetime.utcnow()).isoformat(),
    }


def _serialize_question(doc: dict, pool: str) -> dict:
    """Normalize a question document across all three pool schemas."""
    base = {
        "id":     str(doc["_id"]),
        "pool":   pool,
        "text":   doc.get("text", ""),
        "active": doc.get("active", True),
    }
    if pool == "riasec":
        base["subcategory"] = doc.get("subcategory", "")
    elif pool == "bigfive":
        base["subcategory"]    = doc.get("subcategory", "")
        base["reverse_scored"] = doc.get("reverse_scored", False)
    elif pool == "aptitude":
        base["subject"]        = doc.get("subject", "")
        base["topic"]          = doc.get("topic", "")
        base["difficulty"]     = doc.get("difficulty", "")
        base["options"]        = doc.get("options", {})   # {"A":…,"B":…,"C":…,"D":…}
        base["correct_answer"] = doc.get("correct_answer", "")
    return base


# ═══════════════════════════════════════════════════════════════════════════════
# ANALYTICS
# ═══════════════════════════════════════════════════════════════════════════════

# ── GET /api/admin/analytics ──────────────────────────────────────────────────

@router.get("/analytics")
async def get_analytics(
    range: str = Query("7d", regex="^(7d|30d|all)$"),
    current_user=Depends(require_admin),
):
    since       = _date_filter(range)
    base_filter = {"createdAt": {"$gte": since}} if since else {}

    total_users    = await users_collection.count_documents({})
    new_users      = await users_collection.count_documents(base_filter)
    active_users   = await users_collection.count_documents({"isActive": True})
    inactive_users = await users_collection.count_documents({"isActive": False})

    # Role breakdown
    roles = {
        doc["_id"]: doc["count"]
        async for doc in users_collection.aggregate(
            [{"$group": {"_id": "$role", "count": {"$sum": 1}}}]
        )
    }

    # Registration trend (daily buckets)
    match_stage = {"$match": base_filter} if since else {"$match": {}}
    trend = []
    async for doc in users_collection.aggregate([
        match_stage,
        {"$group": {
            "_id":   {"year": {"$year": "$createdAt"}, "month": {"$month": "$createdAt"}, "day": {"$dayOfMonth": "$createdAt"}},
            "count": {"$sum": 1},
        }},
        {"$sort": {"_id.year": 1, "_id.month": 1, "_id.day": 1}},
    ]):
        d = doc["_id"]
        trend.append({"date": f"{d['year']}-{d['month']:02d}-{d['day']:02d}", "count": doc["count"]})

    # Strand + grade breakdowns
    strands = [
        {"strand": doc["_id"] or "Unknown", "count": doc["count"]}
        async for doc in users_collection.aggregate(
            [{"$group": {"_id": "$strand", "count": {"$sum": 1}}}]
        )
    ]
    grades = [
        {"gradeLevel": doc["_id"] or "Unknown", "count": doc["count"]}
        async for doc in users_collection.aggregate(
            [{"$group": {"_id": "$gradeLevel", "count": {"$sum": 1}}}]
        )
    ]

    return {
        "range":               range,
        "totalUsers":          total_users,
        "newUsers":            new_users,
        "activeUsers":         active_users,
        "inactiveUsers":       inactive_users,
        "roleBreakdown":       roles,
        "registrationTrend":   trend,
        "strandBreakdown":     strands,
        "gradeLevelBreakdown": grades,
    }


# ── GET /api/admin/analytics/courses ─────────────────────────────────────────

@router.get("/analytics/courses")
async def get_course_analytics(
    range: str  = Query("7d", regex="^(7d|30d|all)$"),
    strand: str = Query("all"),
    current_user=Depends(require_admin),
):
    """
    Aggregates course recommendation data from assessment_results.
    Returns:
      - topCourses        : top 10 most-recommended courses overall
      - coursesByStrand   : top 5 courses per strand
      - courseTrend       : daily submission count in the selected range
      - totalSubmissions  : total assessments ever
      - submissionsInRange: assessments in selected range
    """
    since = _date_filter(range)
    match: dict = {"status": "completed"}
    if since:
        match["submittedAt"] = {"$gte": since}
    if strand != "all":
        match["strand"] = strand

    # ── top 10 courses overall ────────────────────────────────────────────────
    top_pipeline = [
        {"$match": match},
        {"$unwind": "$recommendations"},
        {"$match": {"recommendations.rank": 1}},          # only rank-1 per submission
        {"$group": {"_id": "$recommendations.course", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {"course": "$_id", "count": 1, "_id": 0}},
    ]
    top_courses = [doc async for doc in results_col.aggregate(top_pipeline)]

    # ── top 5 courses per strand ──────────────────────────────────────────────
    strand_pipeline = [
        {"$match": {"status": "completed"}},               # no range filter here — all-time
        {"$unwind": "$recommendations"},
        {"$match": {"recommendations.rank": 1}},
        {"$group": {
            "_id":   {"strand": "$strand", "course": "$recommendations.course"},
            "count": {"$sum": 1},
        }},
        {"$sort": {"count": -1}},
        {"$group": {
            "_id":    "$_id.strand",
            "courses": {"$push": {"course": "$_id.course", "count": "$count"}},
        }},
        {"$project": {
            "strand":  "$_id",
            "courses": {"$slice": ["$courses", 5]},
            "_id":     0,
        }},
    ]
    courses_by_strand = [doc async for doc in results_col.aggregate(strand_pipeline)]

    # ── daily submission trend ────────────────────────────────────────────────
    trend_pipeline = [
        {"$match": match},
        {"$group": {
            "_id": {
                "year":  {"$year":         "$submittedAt"},
                "month": {"$month":        "$submittedAt"},
                "day":   {"$dayOfMonth":   "$submittedAt"},
            },
            "count": {"$sum": 1},
        }},
        {"$sort": {"_id.year": 1, "_id.month": 1, "_id.day": 1}},
    ]
    course_trend = []
    async for doc in results_col.aggregate(trend_pipeline):
        d = doc["_id"]
        course_trend.append({"date": f"{d['year']}-{d['month']:02d}-{d['day']:02d}", "count": doc["count"]})

    total_submissions   = await results_col.count_documents({"status": "completed"})
    range_submissions   = await results_col.count_documents(match)

    return {
        "range":              range,
        "strand":             strand,
        "topCourses":         top_courses,
        "coursesByStrand":    courses_by_strand,
        "courseTrend":        course_trend,
        "totalSubmissions":   total_submissions,
        "submissionsInRange": range_submissions,
    }


# ── GET /api/admin/analytics/assessments ─────────────────────────────────────

@router.get("/analytics/assessments")
async def get_assessment_analytics(
    range: str = Query("7d", regex="^(7d|30d|all)$"),
    current_user=Depends(require_admin),
):
    """
    Returns assessment completion stats and per-subject aptitude averages.
    Returns:
      - totalSubmissions       : all completed assessments ever
      - submissionsInRange     : completed in the selected range
      - avgAptitudeScores      : average % per subject across all submissions
      - avgRiasecScores        : average raw score per RIASEC code
      - submissionTrend        : daily completed count in range
      - topStrandsBySubmission : which strands submit most
    """
    since = _date_filter(range)
    match: dict = {"status": "completed"}
    if since:
        match["submittedAt"] = {"$gte": since}

    total_submissions = await results_col.count_documents({"status": "completed"})
    range_submissions = await results_col.count_documents(match)

    # ── average aptitude % per subject ───────────────────────────────────────
    apt_pipeline = [
        {"$match": {"status": "completed"}},
        {"$group": {
            "_id": None,
            "math":     {"$avg": "$scores.aptitude_pct.math"},
            "english":  {"$avg": "$scores.aptitude_pct.english"},
            "science":  {"$avg": "$scores.aptitude_pct.science"},
            "abstract": {"$avg": "$scores.aptitude_pct.abstract"},
        }},
    ]
    apt_doc = None
    async for doc in results_col.aggregate(apt_pipeline):
        apt_doc = doc
    avg_aptitude = {
        k: round(apt_doc.get(k, 0), 1) if apt_doc else 0
        for k in ["math", "english", "science", "abstract"]
    }

    # ── average RIASEC raw score per code ─────────────────────────────────────
    riasec_codes = ["realistic", "investigative", "artistic", "social", "enterprising", "conventional"]
    riasec_group = {code: {"$avg": f"$scores.riasec_raw.{code}"} for code in riasec_codes}
    riasec_group["_id"] = None
    riasec_pipeline = [
        {"$match": {"status": "completed"}},
        {"$group": riasec_group},
    ]
    riasec_doc = None
    async for doc in results_col.aggregate(riasec_pipeline):
        riasec_doc = doc
    avg_riasec = {
        code: round(riasec_doc.get(code, 0), 2) if riasec_doc else 0
        for code in riasec_codes
    }

    # ── daily submission trend ────────────────────────────────────────────────
    trend_pipeline = [
        {"$match": match},
        {"$group": {
            "_id": {
                "year":  {"$year":       "$submittedAt"},
                "month": {"$month":      "$submittedAt"},
                "day":   {"$dayOfMonth": "$submittedAt"},
            },
            "count": {"$sum": 1},
        }},
        {"$sort": {"_id.year": 1, "_id.month": 1, "_id.day": 1}},
    ]
    trend = []
    async for doc in results_col.aggregate(trend_pipeline):
        d = doc["_id"]
        trend.append({"date": f"{d['year']}-{d['month']:02d}-{d['day']:02d}", "count": doc["count"]})

    # ── submissions per strand ────────────────────────────────────────────────
    strand_pipeline = [
        {"$match": {"status": "completed"}},
        {"$group": {"_id": "$strand", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$project": {"strand": "$_id", "count": 1, "_id": 0}},
    ]
    strands_by_sub = [doc async for doc in results_col.aggregate(strand_pipeline)]

    return {
        "range":                  range,
        "totalSubmissions":       total_submissions,
        "submissionsInRange":     range_submissions,
        "avgAptitudeScores":      avg_aptitude,
        "avgRiasecScores":        avg_riasec,
        "submissionTrend":        trend,
        "topStrandsBySubmission": strands_by_sub,
    }


# ═══════════════════════════════════════════════════════════════════════════════
# QUESTION MANAGEMENT  (admin + superadmin)
# ═══════════════════════════════════════════════════════════════════════════════

# ── GET /api/admin/questions ──────────────────────────────────────────────────

@router.get("/questions")
async def list_questions(
    pool:       str            = Query("riasec", regex="^(riasec|bigfive|aptitude)$"),
    subcategory: Optional[str] = Query(None),   # riasec / bigfive subcategory filter
    subject:    Optional[str]  = Query(None),   # aptitude subject filter
    topic:       Optional[str] = Query(None),
    difficulty: Optional[str]  = Query(None),   # aptitude difficulty filter
    active:     Optional[bool] = Query(None),   # None = all, True/False = filter
    page:       int            = Query(1, ge=1),
    limit:      int            = Query(50, ge=1, le=200),
    current_user=Depends(require_admin),
):
    col   = POOL_MAP[pool]
    query: dict = {}

    if active is not None:
        query["active"] = active
    if pool in ("riasec", "bigfive") and subcategory:
        query["subcategory"] = subcategory
    if pool == "aptitude":
        if subject:
            query["subject"] = subject
        if topic:                          # ← ADD THIS BLOCK
            query["topic"] = topic
        if difficulty:
            query["difficulty"] = difficulty

    total  = await col.count_documents(query)
    cursor = col.find(query).sort("_id", -1).skip((page - 1) * limit).limit(limit)
    docs   = [_serialize_question(doc, pool) async for doc in cursor]

    return {"pool": pool, "total": total, "page": page, "limit": limit, "questions": docs}


# ── POST /api/admin/questions ─────────────────────────────────────────────────

@router.post("/questions", status_code=201)
async def create_question(
    data: QuestionCreateRequest,
    current_user=Depends(require_admin),
):
    col = POOL_MAP.get(data.pool)
    if not col:
        raise HTTPException(status_code=400, detail="Invalid pool.")

    doc: dict = {
        "text":      data.text,
        "active":    True,
        "createdAt": datetime.utcnow(),
        "createdBy": current_user.get("email", "admin"),
    }

    if data.pool == "riasec":
        if not data.subcategory:
            raise HTTPException(status_code=422, detail="subcategory required for riasec.")
        doc["subcategory"] = data.subcategory

    elif data.pool == "bigfive":
        if not data.subcategory:
            raise HTTPException(status_code=422, detail="subcategory required for bigfive.")
        doc["subcategory"]    = data.subcategory
        doc["reverse_scored"] = data.reverse_scored or False

    elif data.pool == "aptitude":
        missing = [f for f in ["subject", "difficulty", "options", "correct_answer"] if not getattr(data, f, None)]
        if missing:
            raise HTTPException(status_code=422, detail=f"Missing fields for aptitude: {missing}")
        if data.correct_answer not in ("A", "B", "C", "D"):
            raise HTTPException(status_code=422, detail="correct_answer must be A, B, C, or D.")
        doc["subject"]        = data.subject
        doc["topic"]          = data.topic 
        doc["difficulty"]     = data.difficulty
        doc["options"]        = data.options
        doc["correct_answer"] = data.correct_answer

    result = await col.insert_one(doc)
    return {"id": str(result.inserted_id), "message": "Question created."}


# ── PUT /api/admin/questions/{id} ─────────────────────────────────────────────

@router.put("/questions/{question_id}")
async def update_question(
    question_id: str,
    data: QuestionUpdateRequest,
    current_user=Depends(require_admin),
):
    col = POOL_MAP.get(data.pool)
    if not col:
        raise HTTPException(status_code=400, detail="Invalid pool.")

    update: dict = {"updatedAt": datetime.utcnow(), "updatedBy": current_user.get("email", "admin")}

    if data.text is not None:
        update["text"] = data.text
    if data.subcategory is not None:
        update["subcategory"] = data.subcategory
    if data.reverse_scored is not None:
        update["reverse_scored"] = data.reverse_scored
    if data.subject is not None:
        update["subject"] = data.subject
    if data.difficulty is not None:
        update["difficulty"] = data.difficulty
    if data.options is not None:
        update["options"] = data.options
    if data.correct_answer is not None:
        if data.correct_answer not in ("A", "B", "C", "D"):
            raise HTTPException(status_code=422, detail="correct_answer must be A, B, C, or D.")
        update["correct_answer"] = data.correct_answer

    result = await col.update_one({"_id": ObjectId(question_id)}, {"$set": update})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Question not found.")

    return {"message": "Question updated."}


# ── PATCH /api/admin/questions/{id}/toggle ────────────────────────────────────

@router.patch("/questions/{question_id}/toggle")
async def toggle_question(
    question_id: str,
    pool: str = Query(..., regex="^(riasec|bigfive|aptitude)$"),
    current_user=Depends(require_admin),
):
    col = POOL_MAP[pool]
    doc = await col.find_one({"_id": ObjectId(question_id)})
    if not doc:
        raise HTTPException(status_code=404, detail="Question not found.")

    new_state = not doc.get("active", True)
    await col.update_one(
        {"_id": ObjectId(question_id)},
        {"$set": {
            "active":    new_state,
            "updatedAt": datetime.utcnow(),
            "updatedBy": current_user.get("email", "admin"),
        }},
    )
    return {"id": question_id, "active": new_state, "message": f"Question {'activated' if new_state else 'deactivated'}."}


# ═══════════════════════════════════════════════════════════════════════════════
# SUPERADMIN — USER MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════════

@router.get("/users")
async def list_users(
    page:   int            = Query(1, ge=1),
    limit:  int            = Query(20, ge=1, le=100),
    role:   Optional[str]  = Query(None),
    search: Optional[str]  = Query(None),
    current_user=Depends(require_superadmin),
):
    query: dict = {}
    if role:
        query["role"] = role
    if search:
        query["$or"] = [
            {"username": {"$regex": search, "$options": "i"}},
            {"email":    {"$regex": search, "$options": "i"}},
        ]

    total  = await users_collection.count_documents(query)
    cursor = users_collection.find(query).sort("createdAt", -1).skip((page - 1) * limit).limit(limit)
    users  = [_user_doc(u) async for u in cursor]
    return {"total": total, "page": page, "limit": limit, "users": users}


@router.put("/users/{user_id}/role")
async def update_user_role(
    user_id: str,
    data: UpdateRoleRequest,
    current_user=Depends(require_superadmin),
):
    if data.role not in ("user", "admin", "superadmin"):
        raise HTTPException(status_code=400, detail="Invalid role.")

    result = await users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {
            "$set":  {"role": data.role},
            "$push": {"auditLog": {
                "action":    "role_change",
                "by":        current_user["email"],
                "newRole":   data.role,
                "timestamp": datetime.utcnow(),
            }},
        },
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found.")
    return {"message": f"Role updated to '{data.role}'."}


@router.put("/users/{user_id}/status")
async def update_user_status(
    user_id: str,
    data: UpdateStatusRequest,
    current_user=Depends(require_superadmin),
):
    result = await users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {
            "$set":  {"isActive": data.isActive},
            "$push": {"auditLog": {
                "action":    "status_change",
                "by":        current_user["email"],
                "isActive":  data.isActive,
                "timestamp": datetime.utcnow(),
            }},
        },
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found.")
    return {"message": f"User {'activated' if data.isActive else 'deactivated'}."}


@router.get("/audit-log")
async def get_audit_log(
    page:  int = Query(1, ge=1),
    limit: int = Query(50, ge=1, le=200),
    current_user=Depends(require_superadmin),
):
    pipeline = [
        {"$match":   {"auditLog": {"$exists": True, "$ne": []}}},
        {"$unwind":  "$auditLog"},
        {"$project": {
            "_id":       0,
            "userId":    {"$toString": "$_id"},
            "username":  1,
            "email":     1,
            "action":    "$auditLog.action",
            "by":        "$auditLog.by",
            "newRole":   "$auditLog.newRole",
            "isActive":  "$auditLog.isActive",
            "timestamp": "$auditLog.timestamp",
        }},
        {"$sort":  {"timestamp": -1}},
        {"$skip":  (page - 1) * limit},
        {"$limit": limit},
    ]
    events = []
    async for doc in users_collection.aggregate(pipeline):
        doc["timestamp"] = doc["timestamp"].isoformat() if doc.get("timestamp") else None
        events.append(doc)
    return {"page": page, "limit": limit, "events": events}


@router.get("/export/users")
async def export_users(current_user=Depends(require_superadmin)):
    cursor = users_collection.find({}).sort("createdAt", -1)
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["id", "username", "email", "role", "gradeLevel", "strand", "isActive", "createdAt"])
    async for user in cursor:
        writer.writerow([
            str(user["_id"]),
            user.get("username", ""),
            user.get("email", ""),
            user.get("role", "user"),
            user.get("gradeLevel", ""),
            user.get("strand", ""),
            user.get("isActive", True),
            user.get("createdAt", "").isoformat() if user.get("createdAt") else "",
        ])
    output.seek(0)
    filename = f"coursify_users_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.csv"
    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )