from datetime import datetime, timezone
from pydantic import BaseModel, Field

from .ats import ATSReport
from .company import CompanyIntelligenceReport
from .decision import DecisionReport
from .enums import AnalysisStatus, InputSource
from .gap import GapAnalysisReport
from .interview import InterviewPrepSheet
from .job import JobStructuredJSON
from .matching import MatchReport


class AnalysisMetadata(BaseModel):
    job_id: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    status: AnalysisStatus
    input_source: InputSource


class ArtifactPaths(BaseModel):
    report_json_path: str
    tailored_resume_path: str | None = None
    interview_sheet_path: str | None = None


class FinalAnalysisReport(BaseModel):
    metadata: AnalysisMetadata
    executive_summary: str
    job: JobStructuredJSON
    company: CompanyIntelligenceReport
    match: MatchReport
    ats: ATSReport
    gaps: GapAnalysisReport
    interview_prep: InterviewPrepSheet
    decision: DecisionReport
    artifacts: ArtifactPaths
