from fastapi import APIRouter, HTTPException, Header
from typing import Dict, Any
import json
from app.database import db
from app.models import Users

router = APIRouter()

@router.get("/teachers")
async def list_teachers(x_principal: str = Header(...)):
    # Parse the X-Principal header
    principal_data = json.loads(x_principal)
    if not principal_data.get("principal_id"):
        raise HTTPException(status_code=403, detail="Unauthorized")

    # Query the database for teachers
    teachers = db.query(Users).filter(Users.role == "teacher").all()

    # Format the response
    response = {
        "data": [
            {
                "id": teacher.id,
                "user_id": teacher.user_id,
                "created_at": teacher.created_at,
                "updated_at": teacher.updated_at,
            }
            for teacher in teachers
        ]
    }
    return response
