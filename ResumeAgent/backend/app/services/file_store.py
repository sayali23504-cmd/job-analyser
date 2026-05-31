import json
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from app.config import settings


class FileStore:
    def __init__(self) -> None:
        self.output_dir = settings.output_dir
        self.report_dir = self.output_dir / "reports"
        self.raw_dir = self.output_dir / "raw"
        self.resume_dir = self.output_dir / "resumes"
        self.interview_dir = self.output_dir / "interview_prep"

        self.job_history_file = self.output_dir / "job_history" / "history.jsonl"
        self.application_tracker_file = self.output_dir / "application_tracker" / "applications.json"
        self.resume_versions_file = self.output_dir / "resume_versions" / "versions.jsonl"
        self.company_rankings_placeholder_file = self.output_dir / "company_rankings" / "placeholder.json"
        self.memory_file = settings.data_dir / "memory" / "preferences.json"

        self._ensure_structure()

    def _ensure_structure(self) -> None:
        for path in [
            self.output_dir,
            self.report_dir,
            self.raw_dir,
            self.resume_dir,
            self.interview_dir,
            self.job_history_file.parent,
            self.application_tracker_file.parent,
            self.resume_versions_file.parent,
            self.company_rankings_placeholder_file.parent,
            self.memory_file.parent,
        ]:
            path.mkdir(parents=True, exist_ok=True)

        if not self.application_tracker_file.exists():
            self._write_json(self.application_tracker_file, {"applications": []})
        if not self.company_rankings_placeholder_file.exists():
            self._write_json(self.company_rankings_placeholder_file, {"rankings": [], "note": "V1 placeholder only"})
        if not self.memory_file.exists():
            self._write_json(self.memory_file, {"preferred_roles": [], "preferred_locations": [], "notes": ""})

    @staticmethod
    def _write_json(path: Path, payload: dict[str, Any]) -> None:
        path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    @staticmethod
    def _append_jsonl(path: Path, payload: dict[str, Any]) -> None:
        with path.open("a", encoding="utf-8") as file:
            file.write(json.dumps(payload) + "\n")

    @staticmethod
    def _read_json(path: Path) -> dict[str, Any]:
        return json.loads(path.read_text(encoding="utf-8"))

    def new_job_id(self) -> str:
        return datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S") + "-" + uuid.uuid4().hex[:8]

    def save_raw_payload(self, job_id: str, payload: dict[str, Any]) -> str:
        path = self.raw_dir / f"{job_id}.json"
        self._write_json(path, payload)
        return str(path)

    def save_report(self, job_id: str, report: dict[str, Any]) -> str:
        path = self.report_dir / f"{job_id}.json"
        self._write_json(path, report)
        return str(path)

    def load_report(self, job_id: str) -> dict[str, Any]:
        path = self.report_dir / f"{job_id}.json"
        if not path.exists():
            raise FileNotFoundError(f"No report found for job_id={job_id}")
        return self._read_json(path)

    def report_path(self, job_id: str) -> Path:
        path = self.report_dir / f"{job_id}.json"
        if not path.exists():
            raise FileNotFoundError(f"No report found for job_id={job_id}")
        return path

    def resume_path(self, job_id: str) -> Path:
        return self.resume_dir / f"{job_id}.docx"

    def interview_path(self, job_id: str) -> Path:
        return self.interview_dir / f"{job_id}.md"

    def append_job_history(self, payload: dict[str, Any]) -> None:
        self._append_jsonl(self.job_history_file, payload)

    def list_job_history(self, limit: int = 50) -> list[dict[str, Any]]:
        if not self.job_history_file.exists():
            return []
        rows = [json.loads(line) for line in self.job_history_file.read_text(encoding="utf-8").splitlines() if line.strip()]
        return list(reversed(rows[-limit:]))

    def append_resume_version(self, payload: dict[str, Any]) -> None:
        self._append_jsonl(self.resume_versions_file, payload)

    def read_applications(self) -> dict[str, Any]:
        return self._read_json(self.application_tracker_file)

    def upsert_application(self, job_id: str, status: str) -> dict[str, Any]:
        data = self.read_applications()
        apps = data.get("applications", [])
        now = datetime.now(timezone.utc).isoformat()
        updated = False
        for item in apps:
            if item.get("job_id") == job_id:
                item["status"] = status
                item["updated_at"] = now
                updated = True
                break
        if not updated:
            apps.append({"job_id": job_id, "status": status, "updated_at": now})
        data["applications"] = apps
        self._write_json(self.application_tracker_file, data)
        return data
