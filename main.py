from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import google.generativeai as genai

from routes.auth import router as auth_router
from routes.assessment import router as assessment_router
from routes.admin import router as admin_router   # ← add this

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI(title="Coursify API")

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    os.getenv("FRONTEND_URL", ""),
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://coursify-web-mzls.onrender.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(auth_router, prefix="/api/auth", tags=["Auth"])
app.include_router(assessment_router, prefix="/api/assessment", tags=["Assessment"])
app.include_router(admin_router, prefix="/api/admin", tags=["Admin"])  # ← add this

@app.get("/")
def root():
    return {"message": "Coursify API is running!"}

@app.get("/ping")
def ping():
    return {"status": "ok"}