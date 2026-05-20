"""
middleware/roles.py
===================
Reusable FastAPI dependencies that enforce role-based access control.
Import and use as a Depends() in any route.
"""

from fastapi import Depends, HTTPException
from routes.auth import get_current_user


async def require_admin(current_user=Depends(get_current_user)):
    """Allows admin and superadmin."""
    role = current_user.get("role", "user")
    if role not in ("admin", "superadmin"):
        raise HTTPException(status_code=403, detail="Admin access required.")
    return current_user


async def require_superadmin(current_user=Depends(get_current_user)):
    """Allows superadmin only."""
    role = current_user.get("role", "user")
    if role != "superadmin":
        raise HTTPException(status_code=403, detail="Superadmin access required.")
    return current_user