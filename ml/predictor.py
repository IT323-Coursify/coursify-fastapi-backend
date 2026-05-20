"""
ml/predictor.py
===============
Loads the trained RandomForest model and converts raw assessment
scores into the exact feature vector the model expects.

FEATURE VECTOR (20 features, must match training order exactly):
  [0–5]   RIASEC      : realistic, investigative, artistic, social, enterprising, conventional
                        → normalized 0–1  (raw_sum / 30)
  [6–10]  Big Five    : openness, conscientiousness, extraversion, agreeableness, neuroticism
                        → normalized 0–1  ((mean_score - 1) / 4)
  [11–14] Aptitude    : math, english, science, abstract
                        → raw percentage  (correct / 12 * 100)
  [15–19] Strand      : strand_STEM, strand_ABM, strand_HUMSS, strand_TVL, strand_GAS
                        → one-hot         (1 for selected strand, 0 for rest)

Usage:
    from ml.predictor import get_top5_recommendations
    results = await get_top5_recommendations(
        riasec_raw   = {"realistic": 24, "investigative": 28, ...},
        bigfive_raw  = {"openness": 3.8, "conscientiousness": 4.2, ...},
        aptitude_pct = {"math": 75.0, "english": 66.7, "science": 83.3, "abstract": 91.7},
        strand       = "STEM"
    )
    # returns: [{"course": "Computer Science", "confidence": 45.5}, ...]
"""

import os
import numpy as np
import pandas as pd
import joblib

# ── Paths ─────────────────────────────────────────────────────────────────────
BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "artifacts", "course_model.joblib")
SCALER_PATH= os.path.join(BASE_DIR, "artifacts", "scaler.joblib")
LE_PATH    = os.path.join(BASE_DIR, "artifacts", "label_encoder.joblib")
FN_PATH    = os.path.join(BASE_DIR, "artifacts", "feature_names.joblib")

# ── Lazy-load model (loaded once, reused across requests) ─────────────────────
_model    = None
_scaler   = None
_le       = None
_features = None

def _load_artifacts():
    global _model, _scaler, _le, _features
    if _model is None:
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            _model    = joblib.load(MODEL_PATH)
            _scaler   = joblib.load(SCALER_PATH)
            _le       = joblib.load(LE_PATH)
            _features = joblib.load(FN_PATH)


# ── Score conversion ──────────────────────────────────────────────────────────

def convert_to_feature_vector(
    riasec_raw:   dict,
    bigfive_raw:  dict,
    aptitude_pct: dict,
    strand:       str,
) -> pd.DataFrame:
    """
    Converts raw assessment scores into the normalized feature vector
    the model was trained on.

    Parameters
    ----------
    riasec_raw   : { code: raw_sum }   e.g. {"realistic": 24, ...}
                   raw_sum = sum of 6 Likert answers (1–5), range 6–30
    bigfive_raw  : { trait: mean }     e.g. {"openness": 3.8, ...}
                   mean = average of 5 items after reverse scoring, range 1–5
    aptitude_pct : { subject: pct }    e.g. {"math": 75.0, ...}
                   pct = correct/12 * 100, range 0–100
    strand       : str                 one of STEM | ABM | HUMSS | TVL | GAS

    Returns
    -------
    pd.DataFrame with shape (1, 20) matching training feature order
    """

    # ── RIASEC: normalize to 0–1 (raw sum / 30) ──────────────────────────────
    riasec_codes = ["realistic", "investigative", "artistic",
                    "social", "enterprising", "conventional"]
    riasec_norm  = {
        code: round(riasec_raw.get(code, 0) / 30, 4)
        for code in riasec_codes
    }

    # ── Big Five: normalize to 0–1 ((mean - 1) / 4) ──────────────────────────
    bigfive_traits = ["openness", "conscientiousness", "extraversion",
                      "agreeableness", "neuroticism"]
    bigfive_norm   = {
        trait: round((bigfive_raw.get(trait, 3.0) - 1) / 4, 4)
        for trait in bigfive_traits
    }

    # ── Aptitude: keep as raw % (matches training data 0–100) ────────────────
    aptitude_subjects = ["math", "english", "science", "abstract"]
    aptitude_vals     = {
        subj: round(aptitude_pct.get(subj, 0.0), 1)
        for subj in aptitude_subjects
    }

    # ── Strand: one-hot encode ────────────────────────────────────────────────
    strand_cols = ["strand_STEM", "strand_ABM", "strand_HUMSS", "strand_TVL", "strand_GAS"]
    strand_key  = f"strand_{strand.upper()}"
    strand_vals = {col: 1 if col == strand_key else 0 for col in strand_cols}

    # ── Assemble in exact training order ─────────────────────────────────────
    row = {}
    row.update(riasec_norm)
    row.update(bigfive_norm)
    row.update(aptitude_vals)
    row.update(strand_vals)

    return pd.DataFrame([row])


# ── Main prediction function ──────────────────────────────────────────────────

def get_top5_recommendations(
    riasec_raw:   dict,
    bigfive_raw:  dict,
    aptitude_pct: dict,
    strand:       str,
    k:            int = 5,
) -> list[dict]:
    """
    Returns top-K course recommendations with confidence scores.

    Returns
    -------
    list of dicts:
        [
            {"rank": 1, "course": "Computer Science",  "confidence": 45.5},
            {"rank": 2, "course": "Data Science",      "confidence": 18.2},
            ...
        ]
    """
    _load_artifacts()

    # Build feature vector
    X_df = convert_to_feature_vector(riasec_raw, bigfive_raw, aptitude_pct, strand)

    # Reorder columns to match exact training feature order
    X_ordered = X_df[_features]

    # Scale
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        X_scaled = _scaler.transform(X_ordered)

    # Predict probabilities
    proba    = _model.predict_proba(X_scaled)[0]
    top_k    = np.argsort(proba)[::-1][:k]

    return [
        {
            "rank":       int(rank + 1),
            "course":     str(_le.classes_[idx]),
            "confidence": round(float(proba[idx]) * 100, 1),
        }
        for rank, idx in enumerate(top_k)
    ]