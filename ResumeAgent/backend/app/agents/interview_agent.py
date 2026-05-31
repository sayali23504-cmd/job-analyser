from app.schemas.interview import InterviewPrepSheet


def run_interview_agent(job_title: str, company: str) -> InterviewPrepSheet:
    return InterviewPrepSheet(
        hr_questions=[
            "Tell me about yourself and why this role fits your goals.",
            f"Why do you want to work at {company}?",
        ],
        technical_questions=[
            f"How would you prioritize KPIs in a {job_title} context?",
            "Explain a project where you used data to make a decision.",
        ],
        behavioral_questions=[
            "Describe a time you handled ambiguity.",
            "Tell me about a conflict and how you resolved it.",
        ],
        resume_questions=["Walk me through your most relevant resume experience for this role."],
        case_questions=["Estimate the market size for a new service in a city of your choice."],
        company_questions=[f"What are {company}'s top priorities for this role in the first 90 days?"],
    )
