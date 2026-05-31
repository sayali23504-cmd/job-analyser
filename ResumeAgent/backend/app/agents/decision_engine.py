from app.schemas.decision import DecisionReport
from app.schemas.enums import VerdictTier


def run_decision_engine(score: int) -> DecisionReport:
    if score >= 80:
        tier = VerdictTier.A
    elif score >= 65:
        tier = VerdictTier.B
    elif score >= 45:
        tier = VerdictTier.C
    else:
        tier = VerdictTier.D

    return DecisionReport(
        suitability_score=score,
        verdict=tier,
        justification=["Phase 1 rule-based placeholder decision."],
    )
