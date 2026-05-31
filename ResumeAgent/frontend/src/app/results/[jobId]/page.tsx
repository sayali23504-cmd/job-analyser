import Link from "next/link";
import { getAnalysis } from "../../../lib/api";

export default async function ResultsPage({ params }: { params: { jobId: string } }) {
  const report = await getAnalysis(params.jobId);

  return (
    <main className="container">
      <section className="card">
        <h1>Results</h1>
        <p><strong>Job ID:</strong> {params.jobId}</p>
        <p><strong>Executive Summary:</strong> {report.executive_summary}</p>
        <p><strong>Suitability Score:</strong> {report.decision.suitability_score}</p>
        <p><strong>Verdict:</strong> {report.decision.verdict}</p>
      </section>

      <section className="card grid grid-2">
        <div>
          <h3>Job Analysis</h3>
          <p><strong>Title:</strong> {report.job.job_title}</p>
          <p><strong>Company:</strong> {report.job.company}</p>
        </div>
        <div>
          <h3>ATS Analysis</h3>
          <p><strong>Missing Keywords:</strong> {report.ats.missing_keywords.join(", ") || "None"}</p>
        </div>
      </section>

      <section className="card">
        <h3>Downloads</h3>
        <p><Link href={`http://localhost:8000/api/v1/download/resume/${params.jobId}`}>Download Tailored Resume (DOCX)</Link></p>
        <p><Link href={`http://localhost:8000/api/v1/download/interview/${params.jobId}`}>Download Interview Prep</Link></p>
        <p><Link href={`http://localhost:8000/api/v1/download/report/${params.jobId}`}>Download Full Report (JSON)</Link></p>
      </section>
    </main>
  );
}
