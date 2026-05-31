from pydantic import BaseModel, Field


class GapAnalysisReport(BaseModel):
    high_priority_gaps: list[str] = Field(default_factory=list)
    medium_priority_gaps: list[str] = Field(default_factory=list)
    low_priority_gaps: list[str] = Field(default_factory=list)
    recommended_actions: list[str] = Field(default_factory=list)
