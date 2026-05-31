from app.schemas.matching import MatchReport


BASE_PROFILE_SKILLS = {"python", "sql", "excel", "analytics", "communication", "presentation"}


def run_resume_agent(required_skills: list[str], preferred_skills: list[str]) -> MatchReport:
    required = {s.lower() for s in required_skills}
    preferred = {s.lower() for s in preferred_skills}

    required_hit = len(required & BASE_PROFILE_SKILLS)
    preferred_hit = len(preferred & BASE_PROFILE_SKILLS)

    skills_score = min(100, int((required_hit * 12) + (preferred_hit * 6) + 40))
    experience_score = 55
    career_score = 65
    overall = int((skills_score * 0.45) + (experience_score * 0.30) + (career_score * 0.25))

    matched_points = [f"Matched required skills: {required_hit}", f"Matched preferred skills: {preferred_hit}"]
    risk_points = []
    if required_hit < max(1, len(required) // 2):
        risk_points.append("Several core required skills are missing or unclear.")

    return MatchReport(
        overall_match_score=max(0, min(100, overall)),
        skills_match=skills_score,
        experience_match=experience_score,
        career_match=career_score,
        matched_points=matched_points,
        risk_points=risk_points,
    )
