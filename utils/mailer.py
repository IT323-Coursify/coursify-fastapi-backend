# import aiosmtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from dotenv import load_dotenv
# import os

# load_dotenv()

# async def send_verification_code(to_email: str, code: str):
#     msg = MIMEMultipart("alternative")
#     msg["Subject"] = "Your Coursify Verification Code"
#     msg["From"] = f"Coursify <{os.getenv('EMAIL_USER')}>"
#     msg["To"]      = to_email

#     html = f"""
#         <div style="font-family: sans-serif; max-width: 480px; margin: auto;">
#             <h2 style="color: #20AFAB;">Email Verification</h2>
#             <p>Your verification code is:</p>
#             <h1 style="letter-spacing: 8px; color: #4da3f5;">{code}</h1>
#             <p>This code expires in <strong>10 minutes</strong>.</p>
#         </div>
#     """
#     msg.attach(MIMEText(html, "html"))

#     await aiosmtplib.send(
#         msg,
#         hostname="smtp.gmail.com",
#         port=587,
#         username=os.getenv("EMAIL_USER"),
#         password=os.getenv("EMAIL_PASS"),
#         start_tls=True,
#     )

# async def send_reset_code(to_email: str, code: str):
#     msg = MIMEMultipart("alternative")
#     msg["Subject"] = "Your Coursify Password Reset Code"
#     msg["From"] = f"Coursify <{os.getenv('EMAIL_USER')}>"
#     msg["To"]      = to_email

#     html = f"""
#         <div style="font-family: sans-serif; max-width: 480px; margin: auto;">
#             <h2 style="color: #20AFAB;">Password Reset</h2>
#             <p>You requested to reset your Coursify password. Your reset code is:</p>
#             <h1 style="letter-spacing: 8px; color: #f5a623;">{code}</h1>
#             <p>This code expires in <strong>10 minutes</strong>.</p>
#             <p style="color: #999; font-size: 12px;">If you didn't request this, you can safely ignore this email.</p>
#         </div>
#     """
#     msg.attach(MIMEText(html, "html"))

#     await aiosmtplib.send(
#         msg,
#         hostname="smtp.gmail.com",
#         port=587,
#         username=os.getenv("EMAIL_USER"),
#         password=os.getenv("EMAIL_PASS"),
#         start_tls=True,
#     )

# mailer.py
import aiosmtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# ✅ Environment variables must be set in Render dashboard
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

if not EMAIL_USER or not EMAIL_PASS:
    raise RuntimeError("EMAIL_USER or EMAIL_PASS not set in environment!")

async def send_verification_code(to_email: str, code: str):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Your Coursify Verification Code"
    msg["From"] = f"Coursify <{EMAIL_USER}>"
    msg["To"] = to_email

    html = f"""
        <div style="font-family: sans-serif; max-width: 480px; margin: auto;">
            <h2 style="color: #20AFAB;">Email Verification</h2>
            <p>Your verification code is:</p>
            <h1 style="letter-spacing: 8px; color: #4da3f5;">{code}</h1>
            <p>This code expires in <strong>10 minutes</strong>.</p>
        </div>
    """
    msg.attach(MIMEText(html, "html"))

    try:
        # ✅ Gmail SMTP with STARTTLS (port 587)
        await aiosmtplib.send(
            msg,
            hostname="smtp.gmail.com",
            port=587,
            username=EMAIL_USER,
            password=EMAIL_PASS,
            start_tls=True,
        )
    except Exception as e:
        # Try SSL/TLS on port 465 if 587 fails
        try:
            await aiosmtplib.send(
                msg,
                hostname="smtp.gmail.com",
                port=465,
                username=EMAIL_USER,
                password=EMAIL_PASS,
                use_tls=True,
            )
        except Exception as e2:
            print("SMTP error:", e2)
            raise

async def send_reset_code(to_email: str, code: str):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Your Coursify Password Reset Code"
    msg["From"] = f"Coursify <{EMAIL_USER}>"
    msg["To"] = to_email

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

    try:
        await aiosmtplib.send(
            msg,
            hostname="smtp.gmail.com",
            port=587,
            username=EMAIL_USER,
            password=EMAIL_PASS,
            start_tls=True,
        )
    except Exception as e:
        try:
            await aiosmtplib.send(
                msg,
                hostname="smtp.gmail.com",
                port=465,
                username=EMAIL_USER,
                password=EMAIL_PASS,
                use_tls=True,
            )
        except Exception as e2:
            print("SMTP error:", e2)
            raise
