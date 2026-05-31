from enum import Enum


class VerdictTier(str, Enum):
    A = "Tier A: Apply Immediately"
    B = "Tier B: Apply After Resume Changes"
    C = "Tier C: Apply If Time Permits"
    D = "Tier D: Skip"


class AnalysisStatus(str, Enum):
    RECEIVED = "received"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class InputSource(str, Enum):
    JD_PDF = "jd_pdf"
    JOB_URL = "job_url"
    MANUAL_TEXT = "manual_jd_text"
