# FastAPI routes for teams
from fastapi import APIRouter

router = APIRouter()

@router.get("/teams")
def get_teams():
    return {"message": "Teams route working"}
