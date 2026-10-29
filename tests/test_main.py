
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_skills_matching():
    payload = {
        "required_skills": ["Python", "FastAPI", "SQL", "Git"],
        "candidate_skills": ["Python", "SQL", "Git"]
    }

    response = client.post("/skills", json=payload)

    assert response.status_code == 200
    assert response.json() == {
        "missing_skills": ["FastAPI"],
        "match_percentage": 75.0
    }


def test_skills_missing_required_field():
    payload = {
        "required_skills": ["Python", "SQL"]
    }

    response = client.post("/skills", json=payload)

    assert response.status_code == 422


def test_skills_with_empty_requirements():
    payload = {
        "required_skills": [],
        "candidate_skills": ["Python", "SQL"]
    }

    response = client.post("/skills", json=payload)

    assert response.status_code == 200
    assert response.json() == {
        "missing_skills": [],
        "match_percentage": 0.0
    }

def test_skills_with_case_insensitive_matching():
    payload = {
        "required_skills": ["python", "sql", "Git"],
        "candidate_skills": ["Python", "SQL"]
    }

    response = client.post("/skills", json=payload)

    assert response.status_code == 200
    assert response.json() == {
        "missing_skills": ["Git"],
        "match_percentage": 66.67
    }

def test_skills_with_duplicate_candidate_skills():
    payload = {
        "required_skills": ["Python", "SQL"],
        "candidate_skills": ["Python", "Python", "SQL"]
    }

    response = client.post("/skills", json=payload)

    assert response.status_code == 200
    assert response.json() == {
        "missing_skills": [],
        "match_percentage": 100.0
    }

def test_skills_with_no_matching_skills():
    payload = {
        "required_skills": ["Python", "SQL"],
        "candidate_skills": ["Java", "C++"]
    }

    response = client.post("/skills", json=payload)

    assert response.status_code == 200
    assert response.json() == {
        "missing_skills": ["Python", "SQL"],
        "match_percentage": 0.0
    }

def test_skills_with_empty_and_whitespace_skills():
    payload = {
        "required_skills": ["Python", "  ", ""],
        "candidate_skills": ["Python", "SQL"]
    }

    response = client.post("/skills", json=payload)

    assert response.status_code == 422