# FastAPI routes for skills
from fastapi import APIRouter

router = APIRouter()

@router.get("/skills")
def get_skills():
    return {"message": "Skills route working"}
