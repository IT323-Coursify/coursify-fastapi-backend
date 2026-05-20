from pydantic import BaseModel, EmailStr
from typing import Optional

class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str

class VerifyRequest(BaseModel):
    email: EmailStr
    code: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class UpdateProfileRequest(BaseModel):
    username:   Optional[str] = None
    email:      Optional[EmailStr] = None
    gradeLevel: Optional[str] = None
    strand:     Optional[str] = None

class ForgotPasswordRequest(BaseModel):
    email: EmailStr

class ResetVerifyRequest(BaseModel):
    email: EmailStr
    code: str

class ResetPasswordRequest(BaseModel):
    reset_token: str
    new_password: str


# ── Admin models ──────────────────────────────────────────────────────────────

class UpdateRoleRequest(BaseModel):
    """Body for PUT /api/admin/users/{id}/role"""
    role: str  # "user" | "admin" | "superadmin"


class UpdateStatusRequest(BaseModel):
    """Body for PUT /api/admin/users/{id}/status"""
    isActive: bool


# ── Question management models ────────────────────────────────────────────────

class QuestionCreateRequest(BaseModel):
    """
    Body for POST /api/admin/questions.
    Required fields vary by pool:
      riasec   : text, subcategory
      bigfive  : text, subcategory, reverse_scored (optional, default False)
      aptitude : text, subject, difficulty, options, correct_answer
    """
    pool: str                               # "riasec" | "bigfive" | "aptitude"
    text: str

    # riasec / bigfive
    subcategory:    Optional[str]  = None   # e.g. "realistic", "openness"
    reverse_scored: Optional[bool] = None   # bigfive only

    # aptitude
    subject:        Optional[str]  = None   # "math" | "english" | "science" | "abstract"
    topic:          Optional[str]  = None
    difficulty:     Optional[str]  = None   # "easy" | "medium" | "hard"
    options:        Optional[dict] = None   # {"A": "…", "B": "…", "C": "…", "D": "…"}
    correct_answer: Optional[str]  = None   # "A" | "B" | "C" | "D"


class QuestionUpdateRequest(BaseModel):
    """
    Body for PUT /api/admin/questions/{id}.
    pool is required so the route knows which collection to target.
    All other fields are optional — only provided fields are updated.
    """
    pool: str

    text:           Optional[str]  = None
    subcategory:    Optional[str]  = None
    reverse_scored: Optional[bool] = None
    subject:        Optional[str]  = None
    topic:          Optional[str]  = None
    difficulty:     Optional[str]  = None
    options:        Optional[dict] = None
    correct_answer: Optional[str]  = None