import httpx
import os
from dotenv import load_dotenv

load_dotenv()

MAILERSEND_API_KEY = os.getenv("MAILERSEND_API_KEY")
FROM_EMAIL = "test-vz9dlemy8014kj50.mlsender.net"  
FROM_NAME = "Coursify"

async def _send(to_email: str, subject: str, html: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.mailersend.com/v1/email",
            headers={
                "Authorization": f"Bearer {MAILERSEND_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "from": {"email": FROM_EMAIL, "name": FROM_NAME},
                "to": [{"email": to_email}],
                "subject": subject,
                "html": html,
            },
        )
        print("MAILERSEND STATUS:", response.status_code)
        print("MAILERSEND RESPONSE:", response.text)

async def send_verification_code(to_email: str, code: str):
    await _send(
        to_email,
        "Your Coursify Verification Code",
        f"""
            <div style="font-family: sans-serif; max-width: 480px; margin: auto;">
                <h2 style="color: #20AFAB;">Email Verification</h2>
                <p>Your verification code is:</p>
                <h1 style="letter-spacing: 8px; color: #4da3f5;">{code}</h1>
                <p>This code expires in <strong>10 minutes</strong>.</p>
            </div>
        """,
    )

async def send_reset_code(to_email: str, code: str):
    await _send(
        to_email,
        "Your Coursify Password Reset Code",
        f"""
            <div style="font-family: sans-serif; max-width: 480px; margin: auto;">
                <h2 style="color: #20AFAB;">Password Reset</h2>
                <p>Your reset code is:</p>
                <h1 style="letter-spacing: 8px; color: #f5a623;">{code}</h1>
                <p>This code expires in <strong>10 minutes</strong>.</p>
                <p style="color: #999; font-size: 12px;">If you didn't request this, ignore this email.</p>
            </div>
        """,
    )