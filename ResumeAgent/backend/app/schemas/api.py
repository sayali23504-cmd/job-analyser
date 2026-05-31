from pydantic import BaseModel, Field, HttpUrl


class AnalyzeResponse(BaseModel):
    job_id: str
    status: str
    message: str


class AnalyzeResultResponse(BaseModel):
    report: dict


class UpdateApplicationStatusRequest(BaseModel):
    job_id: str = Field(min_length=5)
    status: str = Field(min_length=3)


class AnalyzeInputsPreview(BaseModel):
    job_url: HttpUrl | None = None
    manual_jd_text: str | None = None
