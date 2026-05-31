from pydantic import BaseModel, Field


class ATSReport(BaseModel):
    required_keywords: list[str] = Field(default_factory=list)
    preferred_keywords: list[str] = Field(default_factory=list)
    industry_keywords: list[str] = Field(default_factory=list)
    present_keywords: list[str] = Field(default_factory=list)
    missing_keywords: list[str] = Field(default_factory=list)
    recommended_keywords: list[str] = Field(default_factory=list)
    ats_suggestions: list[str] = Field(default_factory=list)
