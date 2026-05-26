import resend
import os
from dotenv import load_dotenv

load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")

FROM_EMAIL = "Coursify <onboarding@resend.dev>"

async def send_verification_code(to_email: str, code: str):
    resend.Emails.send({
        "from": FROM_EMAIL,
        "to": [to_email],
        "subject": "Your Coursify Verification Code",
        "html": f"""
            <div style="font-family: sans-serif; max-width: 480px; margin: auto;">
                <h2 style="color: #20AFAB;">Email Verification</h2>
                <p>Your verification code is:</p>
                <h1 style="letter-spacing: 8px; color: #4da3f5;">{code}</h1>
                <p>This code expires in <strong>10 minutes</strong>.</p>
            </div>
        """,
    })

async def send_reset_code(to_email: str, code: str):
    resend.Emails.send({
        "from": FROM_EMAIL,
        "to": [to_email],
        "subject": "Your Coursify Password Reset Code",
        "html": f"""
            <div style="font-family: sans-serif; max-width: 480px; margin: auto;">
                <h2 style="color: #20AFAB;">Password Reset</h2>
                <p>You requested to reset your Coursify password. Your reset code is:</p>
                <h1 style="letter-spacing: 8px; color: #f5a623;">{code}</h1>
                <p>This code expires in <strong>10 minutes</strong>.</p>
                <p style="color: #999; font-size: 12px;">
                    If you didn't request this, you can safely ignore this email.
                </p>
            </div>
        """,
    })