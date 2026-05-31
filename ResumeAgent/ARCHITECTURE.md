# Generated Architecture and File Explanation

## Root
- `README.md`: run instructions and V1 scope.
- `requirements.txt`: pinned Python dependencies for FastAPI, schema validation, file upload, PDF parsing, docx readiness.
- `.env.example`: API key placeholder.

## Frontend
- `frontend/`: Next.js placeholder directory for V1 UI integration.

## Backend
- `backend/app/main.py`: FastAPI app entrypoint and router registration.
- `backend/app/config.py`: environment and path configuration.

### API Routes
- `backend/app/api/routes/health.py`: health endpoint.
- `backend/app/api/routes/analyze.py`: analysis trigger and report fetch.
- `backend/app/api/routes/files.py`: download endpoints.
- `backend/app/api/routes/tracker.py`: job history and application tracker routes.

### Schemas (Strict Validation)
- `backend/app/schemas/enums.py`: enums for status, input source, verdict tier.
- `backend/app/schemas/api.py`: request/response models.
- `backend/app/schemas/job.py`: structured job extraction model.
- `backend/app/schemas/company.py`: company intelligence model.
- `backend/app/schemas/matching.py`: resume-job match model.
- `backend/app/schemas/ats.py`: ATS analysis model.
- `backend/app/schemas/gap.py`: gap analysis model.
- `backend/app/schemas/interview.py`: interview prep model.
- `backend/app/schemas/decision.py`: final decision model.
- `backend/app/schemas/report.py`: final aggregate report model.

### Services
- `backend/app/services/file_store.py`: local filesystem persistence.
- `backend/app/services/extractor.py`: PDF extraction.
- `backend/app/services/web_extract.py`: URL text extraction.
- `backend/app/services/resume_builder.py`: DOCX generator.
- `backend/app/services/interview_builder.py`: markdown interview sheet writer.
- `backend/app/services/orchestrator.py`: pipeline orchestration.

### Agents
- job_agent.py, company_agent.py, resume_agent.py, ats_agent.py, gap_agent.py, interview_agent.py, decision_engine.py

## Output Modules (V1)
- Job History
- Application Tracker
- Resume Version History
- Company Ranking placeholder
- Memory preferences store
