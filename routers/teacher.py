from fastapi import APIRouter, HTTPException, Header
from typing import Dict, Any
from datetime import datetime
import json
from app.database import db
from app.models import Assignments

router = APIRouter()

@router.post("/assignments/grade")
async def grade_assignment(
    payload: Dict[str, Any], x_principal: str = Header(...)
):
    # Parse the X-Principal header
    teacher_data = json.loads(x_principal)
    if not teacher_data.get("teacher_id"):
        raise HTTPException(status_code=403, detail="Unauthorized")

    # Fetch the assignment
    assignment_id = payload.get("id")
    assignment = db.query(Assignments).filter(Assignments.id == assignment_id).first()
    if not assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")

    # Verify the assignment is submitted to the teacher
    if assignment.teacher_id != teacher_data["teacher_id"]:
        raise HTTPException(status_code=403, detail="Not authorized to grade this assignment")

    # Update the assignment
    assignment.grade = payload.get("grade")
    assignment.state = "GRADED"
    assignment.updated_at = datetime.utcnow()
    db.commit()

    # Format the response
    response = {
        "data": {
            "id": assignment.id,
            "content": assignment.content,
            "created_at": assignment.created_at,
            "grade": assignment.grade,
            "state": assignment.state,
            "student_id": assignment.student_id,
            "teacher_id": assignment.teacher_id,
            "updated_at": assignment.updated_at,
        }
    }
    return response
