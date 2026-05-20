"""
seed_superadmin.py
==================
One-time script to create the first superadmin account.
Run from your backend folder:

    python seed_superadmin.py

You will be prompted for username, email, and password.
If the email already exists, it will be upgraded to superadmin.
"""

import asyncio
import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from passlib.context import CryptContext
from datetime import datetime

load_dotenv()

pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

client = AsyncIOMotorClient(
    os.getenv("MONGO_URI"),
    tlsAllowInvalidCertificates=True
)
db = client["coursify"]
users_col = db["users"]


async def seed():
    print("\n── Coursify Superadmin Seed ──────────────────────")
    username = input("Username   : ").strip()
    email    = input("Email      : ").strip()
    password = input("Password   : ").strip()

    existing = await users_col.find_one({"email": email})

    if existing:
        await users_col.update_one(
            {"email": email},
            {"$set": {"role": "superadmin"}}
        )
        print(f"\n✅ Existing user '{email}' upgraded to superadmin.")
    else:
        await users_col.insert_one({
            "username":  username,
            "email":     email,
            "password":  pwd.hash(password),
            "role":      "superadmin",
            "isActive":  True,
            "createdAt": datetime.utcnow(),
        })
        print(f"\n✅ Superadmin '{username}' created successfully.")

    print("─────────────────────────────────────────────────\n")


asyncio.run(seed())