const API_BASE = process.env.NEXT_PUBLIC_API_BASE || "http://localhost:8000/api/v1";

export async function analyzeJob(input: { jobUrl?: string; manualText?: string; jdPdf?: File | null }) {
  const form = new FormData();
  if (input.jobUrl) form.append("job_url", input.jobUrl);
  if (input.manualText) form.append("manual_jd_text", input.manualText);
  if (input.jdPdf) form.append("jd_pdf", input.jdPdf);

  const res = await fetch(`${API_BASE}/analyze`, {
    method: "POST",
    body: form,
  });

  if (!res.ok) {
    const err = await res.text();
    throw new Error(err || "Failed to analyze");
  }

  return res.json();
}

export async function getAnalysis(jobId: string) {
  const res = await fetch(`${API_BASE}/analyze/${jobId}`, { cache: "no-store" });
  if (!res.ok) {
    throw new Error("Failed to load analysis result");
  }
  return res.json();
}
