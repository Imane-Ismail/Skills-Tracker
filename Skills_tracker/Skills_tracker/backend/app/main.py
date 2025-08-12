from fastapi import FastAPI
from app.routes import users, teams, skills, skill_status, requests

app = FastAPI(title="MDR Skills Tracker")

@app.get("/")
def root():
    return {"message": "Welcome to the MDR Skills Tracker API!"}
  
app.include_router(users.router)
app.include_router(teams.router)
app.include_router(skills.router)
app.include_router(skill_status.router)
app.include_router(requests.router)
