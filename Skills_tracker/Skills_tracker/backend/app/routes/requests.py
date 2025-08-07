# FastAPI routes for skill requests
from fastapi import APIRouter

router = APIRouter()

@router.get("/requests")
def get_requests():
    return {"message": "Requests route working"}
