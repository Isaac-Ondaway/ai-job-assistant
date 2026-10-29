from app.ai_service import extract_required_skills

job_description = """
We are looking for a Software Engineer with experience in Python,
FastAPI, REST APIs, PostgreSQL, Git, Docker, and automated testing.
Familiarity with AWS is a plus.
"""

skills = extract_required_skills(job_description)
print(skills)