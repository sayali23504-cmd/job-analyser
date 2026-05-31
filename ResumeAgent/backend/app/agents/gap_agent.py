from app.schemas.gap import GapAnalysisReport


def run_gap_agent(missing_keywords: list[str]) -> GapAnalysisReport:
    high = missing_keywords[:5]
    medium = missing_keywords[5:10]
    low = missing_keywords[10:]

    actions = []
    for kw in high:
        actions.append(f"Build one project bullet evidencing {kw} if genuinely done.")
    if not actions:
        actions.append("Maintain strong ATS alignment and improve quantified achievements.")

    return GapAnalysisReport(
        high_priority_gaps=high,
        medium_priority_gaps=medium,
        low_priority_gaps=low,
        recommended_actions=actions,
    )
