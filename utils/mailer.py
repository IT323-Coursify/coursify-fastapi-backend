import aiosmtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

async def send_verification_code(to_email: str, code: str):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Your Coursify Verification Code"
    msg["From"] = f"Coursify <{os.getenv('EMAIL_USER')}>"
    msg["To"]      = to_email

    html = f"""
        <div style="font-family: sans-serif; max-width: 480px; margin: auto;">
            <h2 style="color: #20AFAB;">Email Verification</h2>
            <p>Your verification code is:</p>
            <h1 style="letter-spacing: 8px; color: #4da3f5;">{code}</h1>
            <p>This code expires in <strong>10 minutes</strong>.</p>
        </div>
    """
    msg.attach(MIMEText(html, "html"))

    await aiosmtplib.send(
        msg,
        hostname="smtp.gmail.com",
        port=587,
        username=os.getenv("EMAIL_USER"),
        password=os.getenv("EMAIL_PASS"),
        start_tls=True,
    )

async def send_reset_code(to_email: str, code: str):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Your Coursify Password Reset Code"
    msg["From"] = f"Coursify <{os.getenv('EMAIL_USER')}>"
    msg["To"]      = to_email

    html = f"""
        <div style="font-family: sans-serif; max-width: 480px; margin: auto;">
            <h2 style="color: #20AFAB;">Password Reset</h2>
            <p>You requested to reset your Coursify password. Your reset code is:</p>
            <h1 style="letter-spacing: 8px; color: #f5a623;">{code}</h1>
            <p>This code expires in <strong>10 minutes</strong>.</p>
            <p style="color: #999; font-size: 12px;">If you didn't request this, you can safely ignore this email.</p>
        </div>
    """
    msg.attach(MIMEText(html, "html"))

    await aiosmtplib.send(
        msg,
        hostname="smtp.gmail.com",
        port=587,
        username=os.getenv("EMAIL_USER"),
        password=os.getenv("EMAIL_PASS"),
        start_tls=True,
    )