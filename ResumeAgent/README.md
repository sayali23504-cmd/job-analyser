# AG CloudCore - Resume Intelligence Agent V1

V1 personal career intelligence platform with local-only storage and strict schema-driven backend.

## Implemented
- FastAPI backend with modular agents and orchestrator
- Input fallback hierarchy: JD PDF -> Job URL -> Manual JD text
- Local outputs: report JSON, tailored resume DOCX, interview prep markdown
- Job History, Application Tracker, Resume Version History modules
- Company Ranking Engine placeholder
- Persistent memory preferences file
- Next.js frontend with Home + Results pages and download links

## Backend APIs
Base: `/api/v1`
- `GET /health`
- `POST /analyze`
- `GET /analyze/{job_id}`
- `GET /download/resume/{job_id}`
- `GET /download/interview/{job_id}`
- `GET /download/report/{job_id}`
- `GET /history/jobs?limit=50`
- `GET /tracker/applications`
- `POST /tracker/applications`

## Run locally
1. Install Python 3.11+ and Node.js 20+
2. Backend setup:
   - `pip install -r requirements.txt`
   - `uvicorn backend.app.main:app --reload --port 8000`
3. Frontend setup:
   - `cd frontend`
   - `npm install`
   - `npm run dev`
4. Open [http://localhost:3000](http://localhost:3000)

## Local storage paths
- `data/outputs/reports`
- `data/outputs/resumes`
- `data/outputs/interview_prep`
- `data/outputs/raw`
- `data/outputs/job_history/history.jsonl`
- `data/outputs/application_tracker/applications.json`
- `data/outputs/resume_versions/versions.jsonl`
- `data/outputs/company_rankings/placeholder.json`
- `data/memory/preferences.json`

## Notes
- V1 uses placeholder deterministic logic for agent intelligence (safe, non-fabricating baseline).
- OpenAI-powered prompt execution can be added in Phase 2 agent upgrades.
