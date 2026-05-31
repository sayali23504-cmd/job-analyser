from pydantic import BaseModel, Field


class CompanyIntelligenceReport(BaseModel):
    company: str = Field(min_length=1)
    industry: str = "Unknown"
    business_model: str = "Unknown"
    services: list[str] = Field(default_factory=list)
    culture: str = "Unknown"
    growth: str = "Unknown"
    hiring_profile: str = "Unknown"
    confidence: float = Field(default=0.4, ge=0.0, le=1.0)
