from datetime import datetime, timezone

from app.agents.ats_agent import run_ats_agent
from app.agents.company_agent import run_company_agent
from app.agents.decision_engine import run_decision_engine
from app.agents.gap_agent import run_gap_agent
from app.agents.interview_agent import run_interview_agent
from app.agents.job_agent import run_job_agent
from app.agents.resume_agent import run_resume_agent
from app.schemas.enums import AnalysisStatus, InputSource
from app.schemas.report import AnalysisMetadata, ArtifactPaths, FinalAnalysisReport
from app.services.extractor import extract_text_from_pdf
from app.services.file_store import FileStore
from app.services.interview_builder import build_interview_markdown
from app.services.resume_builder import build_resume_docx
from app.services.web_extract import extract_text_from_url


class Orchestrator:
    def __init__(self) -> None:
        self.store = FileStore()

    def _select_input_source(self, jd_pdf_path: str | None, job_url: str | None, manual_jd_text: str | None) -> InputSource:
        if jd_pdf_path:
            return InputSource.JD_PDF
        if job_url:
            return InputSource.JOB_URL
        return InputSource.MANUAL_TEXT

    def _resolve_job_text(self, jd_pdf_path: str | None, job_url: str | None, manual_jd_text: str | None) -> str:
        if jd_pdf_path:
            pdf_text = extract_text_from_pdf(jd_pdf_path)
            if pdf_text.strip():
                return pdf_text
        if job_url:
            url_text = extract_text_from_url(job_url)
            if url_text.strip():
                return url_text
        if manual_jd_text and manual_jd_text.strip():
            return manual_jd_text.strip()
        raise ValueError("No usable job description input found.")

    def run_analysis(self, job_url: str | None, manual_jd_text: str | None, jd_pdf_path: str | None) -> FinalAnalysisReport:
        job_id = self.store.new_job_id()
        input_source = self._select_input_source(jd_pdf_path, job_url, manual_jd_text)
        job_text = self._resolve_job_text(jd_pdf_path, job_url, manual_jd_text)

        self.store.save_raw_payload(
            job_id,
            {
                "job_id": job_id,
                "job_url": job_url,
                "manual_jd_text": manual_jd_text,
                "jd_pdf_path": jd_pdf_path,
                "resolved_input_source": input_source.value,
                "resolved_job_text_preview": job_text[:1000],
            },
        )

        job = run_job_agent(job_text=job_text, job_url=job_url)
        company = run_company_agent(job.company)
        match = run_resume_agent(job.required_skills, job.preferred_skills)
        ats = run_ats_agent(job.required_skills, job.preferred_skills)
        gaps = run_gap_agent(ats.missing_keywords)
        interview = run_interview_agent(job.job_title, company.company)
        decision = run_decision_engine(match.overall_match_score)

        resume_path = str(self.store.resume_path(job_id))
        interview_path = str(self.store.interview_path(job_id))

        build_resume_docx(
            resume_path,
            job_title=job.job_title,
            company=job.company,
            summary_points=match.matched_points + match.risk_points,
            ats_keywords=ats.recommended_keywords,
        )
        build_interview_markdown(
            interview_path,
            {
                "HR Questions": interview.hr_questions,
                "Technical Questions": interview.technical_questions,
                "Behavioral Questions": interview.behavioral_questions,
                "Resume Questions": interview.resume_questions,
                "Case Questions": interview.case_questions,
                "Company Questions": interview.company_questions,
            },
        )

        report = FinalAnalysisReport(
            metadata=AnalysisMetadata(
                job_id=job_id,
                created_at=datetime.now(timezone.utc),
                status=AnalysisStatus.COMPLETED,
                input_source=input_source,
            ),
            executive_summary="Analysis completed successfully for V1 pipeline with local artifacts generated.",
            job=job,
            company=company,
            match=match,
            ats=ats,
            gaps=gaps,
            interview_prep=interview,
            decision=decision,
            artifacts=ArtifactPaths(
                report_json_path="",
                tailored_resume_path=resume_path,
                interview_sheet_path=interview_path,
            ),
        )

        saved_report_path = self.store.save_report(job_id, report.model_dump(mode="json"))
        report.artifacts.report_json_path = saved_report_path
        self.store.save_report(job_id, report.model_dump(mode="json"))

        self.store.append_job_history(
            {
                "job_id": job_id,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "job_title": job.job_title,
                "company": job.company,
                "status": report.metadata.status.value,
                "verdict": report.decision.verdict.value,
                "suitability_score": report.decision.suitability_score,
            }
        )

        self.store.append_resume_version(
            {
                "job_id": job_id,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "version_label": "v1-initial-tailored",
                "path": resume_path,
                "notes": "Generated from pipeline output without inventing qualifications.",
            }
        )

        return report

    def get_report(self, job_id: str) -> dict:
        return self.store.load_report(job_id)

    def get_job_history(self, limit: int = 50) -> list[dict]:
        return self.store.list_job_history(limit=limit)

    def get_applications(self) -> dict:
        return self.store.read_applications()

    def update_application(self, job_id: str, status: str) -> dict:
        return self.store.upsert_application(job_id=job_id, status=status)
