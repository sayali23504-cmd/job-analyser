from app.schemas.company import CompanyIntelligenceReport


def run_company_agent(company_name: str) -> CompanyIntelligenceReport:
    return CompanyIntelligenceReport(
        company=company_name or "Unknown Company",
        industry="Unknown",
        business_model="Unknown",
        services=[],
        culture="Unknown",
        growth="Unknown",
        hiring_profile="Unknown",
        confidence=0.3,
    )
