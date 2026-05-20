from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os, random, re

from database import users_collection
from models import (
    RegisterRequest, VerifyRequest, LoginRequest,
    UpdateProfileRequest, ForgotPasswordRequest,
    ResetVerifyRequest, ResetPasswordRequest
)
from utils.mailer import send_verification_code, send_reset_code

load_dotenv()

router    = APIRouter()
pwd       = CryptContext(schemes=["bcrypt"], deprecated="auto")
security  = HTTPBearer()
SECRET    = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"

# Temp in-memory stores
pending_users = {}
reset_codes   = {}


# ── helpers ───────────────────────────────────────────────────────────────────

def validate_password(password: str):
    """Enforce minimum password strength requirements."""
    if len(password) < 8:
        raise HTTPException(status_code=400, detail="Password must be at least 8 characters.")
    if not re.search(r"[A-Z]", password):
        raise HTTPException(status_code=400, detail="Password must contain at least one uppercase letter.")
    if not re.search(r"[0-9]", password):
        raise HTTPException(status_code=400, detail="Password must contain at least one number.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        raise HTTPException(status_code=400, detail="Password must contain at least one special character.")


def create_token(data: dict, expires_delta: timedelta = timedelta(days=7)):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + expires_delta
    return jwt.encode(payload, SECRET, algorithm=ALGORITHM)


def _serialize_user(user: dict) -> dict:
    """Return a safe, role-inclusive user dict from a MongoDB document."""
    return {
        "id":         str(user["_id"]),
        "username":   user.get("username", ""),
        "email":      user.get("email", ""),
        "role":       user.get("role", "user"),
        "gradeLevel": user.get("gradeLevel", ""),
        "strand":     user.get("strand", ""),
        "isActive":   user.get("isActive", True),
    }


async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET, algorithms=[ALGORITHM])
        # Ensure role is always present — fall back to "user" for tokens
        # issued before the role field was added.
        if "role" not in payload:
            user = await users_collection.find_one({"email": payload.get("email")})
            payload["role"] = user.get("role", "user") if user else "user"
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token.")


# ── POST /api/auth/register ───────────────────────────────────────────────────

@router.post("/register")
async def register(data: RegisterRequest):
    validate_password(data.password)

    if await users_collection.find_one({"email": data.email}):
        raise HTTPException(status_code=409, detail="Email already in use.")
    if await users_collection.find_one({"username": data.username}):
        raise HTTPException(status_code=409, detail="Username already taken.")

    code       = str(random.randint(100000, 999999))
    expires_at = datetime.utcnow() + timedelta(minutes=10)
    hashed     = pwd.hash(data.password)

    pending_users[data.email] = {
        "code":            code,
        "expires_at":      expires_at,
        "username":        data.username,
        "hashed_password": hashed,
    }

    await send_verification_code(data.email, code)
    return {"message": "Verification code sent to your email."}


# ── POST /api/auth/verify ─────────────────────────────────────────────────────

@router.post("/verify")
async def verify(data: VerifyRequest):
    pending = pending_users.get(data.email)

    if not pending:
        raise HTTPException(status_code=400, detail="No registration found. Please sign up again.")
    if datetime.utcnow() > pending["expires_at"]:
        del pending_users[data.email]
        raise HTTPException(status_code=400, detail="Code expired. Please sign up again.")
    if pending["code"] != data.code:
        raise HTTPException(status_code=400, detail="Incorrect code. Try again.")

    new_user = {
        "username":   pending["username"],
        "email":      data.email,
        "password":   pending["hashed_password"],
        "role":       "user",               # all self-registered accounts start as "user"
        "gradeLevel": "",
        "strand":     "",
        "isActive":   True,
        "createdAt":  datetime.utcnow(),
    }
    result = await users_collection.insert_one(new_user)
    del pending_users[data.email]

    new_user["_id"] = result.inserted_id   # needed by _serialize_user

    token = create_token({
        "id":    str(result.inserted_id),
        "email": data.email,
        "role":  "user",
    })
    return {
        "message": "Registration successful!",
        "token":   token,
        "user":    _serialize_user(new_user),
    }


# ── POST /api/auth/login ──────────────────────────────────────────────────────

@router.post("/login")
async def login(data: LoginRequest):
    user = await users_collection.find_one({"email": data.email})

    if not user or not pwd.verify(data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password.")

    if not user.get("isActive", True):
        raise HTTPException(status_code=403, detail="Your account has been deactivated. Please contact support.")
    print("DEBUG:", user.get("role"), user.get("email"))

    role  = user.get("role", "user")
    token = create_token({
        "id":    str(user["_id"]),
        "email": user["email"],
        "role":  role,                      
    })
    return {
        "message": "Login successful!",
        "token":   token,
        "user":    _serialize_user(user),   
    }


# ── POST /api/auth/forgot-password ───────────────────────────────────────────

@router.post("/forgot-password")
async def forgot_password(data: ForgotPasswordRequest):
    user = await users_collection.find_one({"email": data.email})
    # Always return success to prevent email enumeration.
    if not user:
        return {"message": "If that email exists, a reset code has been sent."}

    code       = str(random.randint(100000, 999999))
    expires_at = datetime.utcnow() + timedelta(minutes=10)

    reset_codes[data.email] = {
        "code":       code,
        "expires_at": expires_at,
    }

    await send_reset_code(data.email, code)
    return {"message": "If that email exists, a reset code has been sent."}


# ── POST /api/auth/reset-verify ──────────────────────────────────────────────

@router.post("/reset-verify")
async def reset_verify(data: ResetVerifyRequest):
    entry = reset_codes.get(data.email)

    if not entry:
        raise HTTPException(status_code=400, detail="No reset request found. Please try again.")
    if datetime.utcnow() > entry["expires_at"]:
        del reset_codes[data.email]
        raise HTTPException(status_code=400, detail="Code expired. Please request a new one.")
    if entry["code"] != data.code:
        raise HTTPException(status_code=400, detail="Incorrect code. Try again.")

    # Issue a short-lived reset token (10 min).
    reset_token = create_token(
        {"email": data.email, "purpose": "reset"},
        expires_delta=timedelta(minutes=10),
    )
    return {"message": "Code verified.", "reset_token": reset_token}


# ── POST /api/auth/reset-password ────────────────────────────────────────────

@router.post("/reset-password")
async def reset_password(data: ResetPasswordRequest):
    try:
        payload = jwt.decode(data.reset_token, SECRET, algorithms=[ALGORITHM])
        if payload.get("purpose") != "reset":
            raise HTTPException(status_code=400, detail="Invalid reset token.")
        email = payload.get("email")
    except JWTError:
        raise HTTPException(status_code=400, detail="Reset token expired or invalid.")

    validate_password(data.new_password)

    hashed = pwd.hash(data.new_password)
    await users_collection.update_one(
        {"email": email},
        {"$set": {"password": hashed}},
    )

    reset_codes.pop(email, None)
    return {"message": "Password reset successful! You can now log in."}


# ── GET /api/auth/profile ─────────────────────────────────────────────────────

@router.get("/profile")
async def get_profile(current_user=Depends(get_current_user)):
    user = await users_collection.find_one({"email": current_user["email"]})
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    return _serialize_user(user)


# ── PUT /api/auth/profile ─────────────────────────────────────────────────────

@router.put("/profile")
async def update_profile(data: UpdateProfileRequest, current_user=Depends(get_current_user)):
    await users_collection.update_one(
        {"email": current_user["email"]},
        {"$set": data.dict(exclude_none=True)},
    )
    updated = await users_collection.find_one({"email": current_user["email"]})
    if not updated:
        raise HTTPException(status_code=404, detail="User not found.")
    return {
        "message": "Profile updated!",
        "user":    _serialize_user(updated),
    }