from pydantic import BaseModel, Field


class MatchReport(BaseModel):
    overall_match_score: int = Field(ge=0, le=100)
    skills_match: int = Field(ge=0, le=100)
    experience_match: int = Field(ge=0, le=100)
    career_match: int = Field(ge=0, le=100)
    matched_points: list[str] = Field(default_factory=list)
    risk_points: list[str] = Field(default_factory=list)
