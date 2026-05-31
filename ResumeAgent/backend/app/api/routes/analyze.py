import os
import tempfile
from typing import Any

from fastapi import APIRouter, File, Form, HTTPException, UploadFile

from app.schemas.api import AnalyzeResponse
from app.services.orchestrator import Orchestrator

router = APIRouter(tags=["analysis"])
orchestrator = Orchestrator()


@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_job(
    job_url: str | None = Form(default=None),
    manual_jd_text: str | None = Form(default=None),
    jd_pdf: UploadFile | None = File(default=None),
) -> AnalyzeResponse:
    if not any([job_url, manual_jd_text, jd_pdf]):
        raise HTTPException(status_code=400, detail="Provide at least one input: jd_pdf, job_url, or manual_jd_text")

    temp_pdf_path: str | None = None
    try:
        if jd_pdf is not None:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                temp_file.write(await jd_pdf.read())
                temp_pdf_path = temp_file.name

        report = orchestrator.run_analysis(
            job_url=job_url,
            manual_jd_text=manual_jd_text,
            jd_pdf_path=temp_pdf_path,
        )

        return AnalyzeResponse(
            job_id=report.metadata.job_id,
            status=report.metadata.status.value,
            message="Analysis completed",
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {error}") from error
    finally:
        if temp_pdf_path and os.path.exists(temp_pdf_path):
            os.remove(temp_pdf_path)


@router.get("/analyze/{job_id}")
def get_analysis_result(job_id: str) -> dict[str, Any]:
    try:
        return orchestrator.get_report(job_id)
    except FileNotFoundError as error:
        raise HTTPException(status_code=404, detail=str(error)) from error
