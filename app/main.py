from fastapi import FastAPI

from app.models import SkillsRequest
from app.services import (
    find_missing_skills,
    calculate_match_percentage,
)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to AI Job Assistant"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/skills")
def skills(data: SkillsRequest):
    required = data.required_skills
    candidate = data.candidate_skills

    missing = find_missing_skills(required, candidate)
    percentage = calculate_match_percentage(required, candidate)

    return {
        "missing_skills": missing,
        "match_percentage": round(percentage, 2),
    }