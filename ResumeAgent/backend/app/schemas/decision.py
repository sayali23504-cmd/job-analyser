from pydantic import BaseModel, Field

from .enums import VerdictTier


class DecisionReport(BaseModel):
    suitability_score: int = Field(ge=0, le=100)
    verdict: VerdictTier
    justification: list[str] = Field(default_factory=list)
