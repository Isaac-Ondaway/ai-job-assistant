def find_missing_skills(
    required_skills: list[str],
    candidate_skills: list[str],
) -> list[str]:
    missing = []

    candidate_skills_lower = {s.lower() for s in candidate_skills}

    for skill in required_skills:
        if skill.lower() not in candidate_skills_lower:
            missing.append(skill)

    return missing


def calculate_match_percentage(
    required_skills: list[str],
    candidate_skills: list[str],
) -> float:
    total_required_skill = len(required_skills)
    cand_skill_match = 0

    candidate_skills_lower = {s.lower() for s in candidate_skills}

    for skill in required_skills:
        if skill.lower() in candidate_skills_lower:
            cand_skill_match += 1

    if total_required_skill > 0:
        percentage = (cand_skill_match / total_required_skill) * 100
    else:
        percentage = 0.0

    return percentage