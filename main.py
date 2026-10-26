from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SkillsRequest(BaseModel):
    required_skills: list[str]
    candidate_skills: list[str]

@app.get("/")
def home():
    return{"message": "Welcome to AI Job Assistant"}

@app.get("/health")
def health_check():
    return{"status":"ok"}

def find_missing_skills(required_skills: list[str], candidate_skills: list[str]):
    missing = []

    for skill in required_skills:
        if skill not in candidate_skills:
            missing.append(skill)

    return missing

def calculate_match_percentage(required_skills: list[str], candidate_skills: list[str]):

    total_required_skill = len(required_skills)
    cand_skill_match = 0

    for skill in required_skills:
        if skill in candidate_skills:
            cand_skill_match +=1

    if total_required_skill>0:
        percentage = (cand_skill_match / total_required_skill) * 100
    else:
        percentage = 0.00
    return percentage

    

@app.post("/skills")
def skills(data: SkillsRequest):
    required = data.required_skills
    candidate = data.candidate_skills

    missing = find_missing_skills(required, candidate)
    percentage = calculate_match_percentage(required, candidate)

    result = {
        "missing_skills": missing,
        "match_percentage": round(percentage,2)
    }
    return result



