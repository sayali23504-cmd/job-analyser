import re
from app.schemas.job import JobStructuredJSON


SKILL_HINTS = [
    "python", "sql", "excel", "power bi", "tableau", "analytics", "operations", "strategy", "communication", "presentation"
]


def _extract_skills(text: str) -> list[str]:
    lower = text.lower()
    found = [skill for skill in SKILL_HINTS if skill in lower]
    return sorted(set(found))


def run_job_agent(job_text: str, job_url: str | None) -> JobStructuredJSON:
    lines = [line.strip() for line in job_text.splitlines() if line.strip()]
    title = lines[0][:120] if lines else "Unknown Job Title"
    company = "Unknown Company"

    for line in lines[:25]:
        m = re.search(r"(.+)\s+at\s+(.+)", line, flags=re.IGNORECASE)
        if m:
            title = m.group(1).strip()[:120]
            company = m.group(2).strip()[:120]
            break

    skills = _extract_skills(job_text)

    return JobStructuredJSON(
        job_title=title,
        company=company,
        responsibilities=lines[1:8],
        required_skills=skills[:8],
        preferred_skills=skills[8:14],
        experience_requirements=["As mentioned in job description"],
        education_requirements=["Bachelor's degree or equivalent (if specified)"],
        source_summary=f"Source used: {'JD PDF' if job_url is None else 'URL/PDF/manual combination'}",
    )
