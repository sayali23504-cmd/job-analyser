from pydantic import BaseModel, Field


class JobStructuredJSON(BaseModel):
    job_title: str = Field(min_length=1)
    company: str = Field(min_length=1)
    responsibilities: list[str] = Field(default_factory=list)
    required_skills: list[str] = Field(default_factory=list)
    preferred_skills: list[str] = Field(default_factory=list)
    experience_requirements: list[str] = Field(default_factory=list)
    education_requirements: list[str] = Field(default_factory=list)
    source_summary: str = Field(default="")
