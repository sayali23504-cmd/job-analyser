from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from app.services.file_store import FileStore

router = APIRouter(tags=["files"])
store = FileStore()


@router.get("/download/resume/{job_id}")
def download_resume(job_id: str) -> FileResponse:
    path = store.resume_path(job_id)
    if not path.exists():
        raise HTTPException(status_code=404, detail="Resume file not found")
    return FileResponse(path=str(path), filename=path.name, media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")


@router.get("/download/interview/{job_id}")
def download_interview(job_id: str) -> FileResponse:
    path = store.interview_path(job_id)
    if not path.exists():
        raise HTTPException(status_code=404, detail="Interview sheet not found")
    return FileResponse(path=str(path), filename=path.name, media_type="text/markdown")


@router.get("/download/report/{job_id}")
def download_report(job_id: str) -> FileResponse:
    path = store.report_path(job_id)
    return FileResponse(path=str(path), filename=path.name, media_type="application/json")
