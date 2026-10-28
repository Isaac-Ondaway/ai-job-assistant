from pydantic import BaseModel


class SkillsRequest(BaseModel):
    required_skills: list[str]
    candidate_skills: list[str]