from pydantic import BaseModel, field_validator


class SkillsRequest(BaseModel):
    required_skills: list[str]
    candidate_skills: list[str]

    @field_validator("required_skills", "candidate_skills")
    def clean_whitespace(cls, v):
        for skill in v:
            if not skill.strip():
                raise ValueError("Skills cannot be empty or whitespace")
        return [skill.strip() for skill in v]