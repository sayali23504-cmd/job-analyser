from app.schemas.ats import ATSReport


BASE_PROFILE_SKILLS = {"python", "sql", "excel", "analytics", "communication", "presentation"}


def run_ats_agent(required_skills: list[str], preferred_skills: list[str]) -> ATSReport:
    required = [s.lower() for s in required_skills]
    preferred = [s.lower() for s in preferred_skills]
    present = sorted([s for s in required + preferred if s in BASE_PROFILE_SKILLS])
    missing = sorted([s for s in required if s not in BASE_PROFILE_SKILLS])
    recommended = sorted(set(missing + preferred))

    return ATSReport(
        required_keywords=sorted(set(required)),
        preferred_keywords=sorted(set(preferred)),
        industry_keywords=["problem solving", "stakeholder management", "data-driven decision making"],
        present_keywords=present,
        missing_keywords=missing,
        recommended_keywords=recommended,
        ats_suggestions=[
            "Place critical required keywords in skills and project bullets where truthfully applicable.",
            "Use exact keyword variants from the JD for ATS compatibility.",
        ],
    )
