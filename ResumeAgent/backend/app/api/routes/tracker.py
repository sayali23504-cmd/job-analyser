from fastapi import APIRouter

from app.schemas.api import UpdateApplicationStatusRequest
from app.services.orchestrator import Orchestrator

router = APIRouter(tags=["tracker"])
orchestrator = Orchestrator()


@router.get("/history/jobs")
def list_job_history(limit: int = 50) -> dict:
    return {"items": orchestrator.get_job_history(limit=limit)}


@router.get("/tracker/applications")
def list_applications() -> dict:
    return orchestrator.get_applications()


@router.post("/tracker/applications")
def update_application_status(payload: UpdateApplicationStatusRequest) -> dict:
    return orchestrator.update_application(payload.job_id, payload.status)
