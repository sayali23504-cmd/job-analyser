from pydantic import BaseModel, Field


class InterviewPrepSheet(BaseModel):
    hr_questions: list[str] = Field(default_factory=list)
    technical_questions: list[str] = Field(default_factory=list)
    behavioral_questions: list[str] = Field(default_factory=list)
    resume_questions: list[str] = Field(default_factory=list)
    case_questions: list[str] = Field(default_factory=list)
    company_questions: list[str] = Field(default_factory=list)
