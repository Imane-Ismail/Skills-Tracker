# FastAPI routes for users
from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def list_users():
    return {"message": "Users endpoint ready"}
