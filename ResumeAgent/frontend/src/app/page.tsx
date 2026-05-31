"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { analyzeJob } from "../lib/api";

export default function HomePage() {
  const [jobUrl, setJobUrl] = useState("");
  const [manualText, setManualText] = useState("");
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const router = useRouter();

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError("");
    setLoading(true);
    try {
      const result = await analyzeJob({ jobUrl, manualText, jdPdf: file });
      router.push(`/results/${result.job_id}`);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Analysis failed");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="container">
      <section className="card">
        <h1>AG CloudCore - Resume Intelligence Agent V1</h1>
        <p>Paste a Job URL, optionally upload a JD PDF, then click Analyze.</p>
      </section>

      <form onSubmit={onSubmit} className="card grid">
        <label>
          Job URL
          <input type="url" value={jobUrl} onChange={(e) => setJobUrl(e.target.value)} placeholder="https://..." />
        </label>

        <label>
          JD PDF (optional)
          <input type="file" accept="application/pdf" onChange={(e) => setFile(e.target.files?.[0] ?? null)} />
        </label>

        <label>
          Manual JD Text (optional fallback)
          <textarea rows={8} value={manualText} onChange={(e) => setManualText(e.target.value)} />
        </label>

        <button type="submit" disabled={loading}>{loading ? "Analyzing..." : "Analyze"}</button>
        {error ? <p style={{ color: "#b42318" }}>{error}</p> : null}
      </form>
    </main>
  );
}
