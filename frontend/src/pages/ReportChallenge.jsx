import { useState } from "react";
import { Link } from "react-router-dom";
import { createChallenge } from "../services/challengeService";
import "./ReportChallenge.css";

function ReportChallenge() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [category, setCategory] = useState("Infrastructure");

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleSubmit(event) {
    event.preventDefault();

    setLoading(true);
    setError("");
    setResult(null);

    const challengeData = {
      title: title.trim(),
      description: description.trim(),
      category,
    };

    try {
      const response = await createChallenge(challengeData);

      console.log("BACKEND RESPONSE:", response);

      setResult(response);

      setTitle("");
      setDescription("");
      setCategory("Infrastructure");
    } catch (err) {
      console.error("API ERROR:", err);

      if (err.response?.data) {
        setError(
          `Backend Error (${err.response.status}): ${JSON.stringify(
            err.response.data
          )}`
        );
      } else if (err.request) {
        setError(
          "The backend did not respond. Please make sure Member 2's Django server is running."
        );
      } else {
        setError(`Request Error: ${err.message}`);
      }
    } finally {
      setLoading(false);
    }
  }

  const urgency = result?.problem_dna?.urgency_score ?? 0;

  return (
    <div className="report-page">

      {/* Background decoration */}
      <div className="background-glow glow-one"></div>
      <div className="background-glow glow-two"></div>

      {/* Navigation */}
      <header className="report-navbar">

        <Link to="/" className="brand">
          <div className="brand-icon">J</div>

          <div>
            <div className="brand-name">JANSETU AI</div>
            <div className="brand-subtitle">
              Societal Innovation Network
            </div>
          </div>
        </Link>

        <div className="nav-right">
          <span className="live-dot"></span>
          AI SYSTEM ONLINE

          <Link
            to="/citizen/dashboard"
            className="dashboard-link"
          >
            Dashboard
          </Link>
        </div>

      </header>

      {/* Main */}
      <main className="report-container">

        {/* Page heading */}
        <section className="page-heading">

          <div className="eyebrow">
            <span>01</span>
            CITIZEN CHALLENGE SUBMISSION
          </div>

          <h1>
            Turn a local problem
            <span> into an actionable solution.</span>
          </h1>

          <p>
            Describe a problem affecting your community.
            JANSETU AI analyzes the challenge, identifies
            the required expertise and resources, and
            prepares it for collaboration.
          </p>

        </section>

        {/* Content grid */}
        <section className="report-grid">

          {/* FORM */}
          <div className="form-card">

            <div className="card-header">

              <div className="card-icon">
                +
              </div>

              <div>
                <h2>Submit a Challenge</h2>
                <p>
                  Share what your community needs solved.
                </p>
              </div>

            </div>

            <form onSubmit={handleSubmit}>

              <div className="form-group">

                <label>
                  Problem title
                  <span>*</span>
                </label>

                <input
                  type="text"
                  value={title}
                  onChange={(e) =>
                    setTitle(e.target.value)
                  }
                  placeholder="e.g. Bridge damaged during monsoon"
                  required
                />

              </div>

              <div className="form-group">

                <label>
                  Describe the problem
                  <span>*</span>
                </label>

                <textarea
                  value={description}
                  onChange={(e) =>
                    setDescription(e.target.value)
                  }
                  placeholder="Explain what is happening, where it is happening, who is affected and how frequently it occurs..."
                  rows={7}
                  required
                />

                <div className="input-helper">
                  Be specific — better information helps
                  our AI produce better recommendations.
                </div>

              </div>

              <div className="form-group">

                <label>
                  Challenge domain
                  <span>*</span>
                </label>

                <select
                  value={category}
                  onChange={(e) =>
                    setCategory(e.target.value)
                  }
                >
                  <option>Infrastructure</option>
                  <option>Water Management</option>
                  <option>Agriculture</option>
                  <option>Healthcare</option>
                  <option>Education</option>
                  <option>Environment</option>
                  <option>Transportation</option>
                </select>

              </div>

              <button
                type="submit"
                className="analyze-button"
                disabled={loading}
              >

                <span className="button-icon">
                  {loading ? "◌" : "✦"}
                </span>

                <span>
                  {loading
                    ? "AI is analyzing..."
                    : "Analyze with JANSETU AI"}
                </span>

                {!loading && (
                  <span className="button-arrow">
                    →
                  </span>
                )}

              </button>

            </form>

            {error && (
              <div className="error-box">

                <div className="error-title">
                  Analysis failed
                </div>

                <div>{error}</div>

              </div>
            )}

            <div className="privacy-note">
              <span>✓</span>
              Your submission is securely processed and
              used to create an actionable challenge.
            </div>

          </div>

          {/* RIGHT SIDE */}
          <div className="ai-panel">

            {!result ? (

              <div className="empty-ai">

                <div className="ai-orbit">

                  <div className="orbit-ring ring-one"></div>
                  <div className="orbit-ring ring-two"></div>

                  <div className="ai-core">
                    ✦
                  </div>

                </div>

                <div className="ai-label">
                  JANSETU INTELLIGENCE ENGINE
                </div>

                <h2>
                  Your problem.
                  <br />
                  <span>AI-powered clarity.</span>
                </h2>

                <p>
                  Submit a challenge and our intelligence
                  engine will transform your description
                  into a structured Problem DNA.
                </p>

                <div className="process-list">

                  <div>
                    <span>01</span>
                    Understand the problem
                  </div>

                  <div>
                    <span>02</span>
                    Identify required expertise
                  </div>

                  <div>
                    <span>03</span>
                    Estimate resources
                  </div>

                  <div>
                    <span>04</span>
                    Prioritize the challenge
                  </div>

                </div>

              </div>

            ) : (

              <ProblemDNA
                data={result.problem_dna}
                challengeId={
                  result.problem_dna?.challenge ||
                  result.id
                }
              />

            )}

          </div>

        </section>

      </main>

    </div>
  );
}


function ProblemDNA({ data, challengeId }) {

  const urgency = data?.urgency_score ?? 0;

  let urgencyClass = "low";

  if (urgency >= 75) {
    urgencyClass = "high";
  } else if (urgency >= 50) {
    urgencyClass = "medium";
  }

  return (
    <div className="dna-card">

      <div className="dna-top">

        <div>

          <div className="ai-label">
            AI ANALYSIS COMPLETE
          </div>

          <h2>
            Problem DNA
          </h2>

        </div>

        <div className="verified">
          ✓ VERIFIED
        </div>

      </div>

      <div className="dna-id">
        Challenge #{challengeId ?? "—"}
      </div>

      {/* Domain */}
      <div className="dna-section">

        <div className="section-label">
          DOMAIN
        </div>

        <div className="domain-value">
          {data?.domain || "Not available"}
        </div>

      </div>

      {/* Urgency */}
      <div className="dna-section">

        <div className="urgency-header">

          <div className="section-label">
            URGENCY SCORE
          </div>

          <div className={`urgency-value ${urgencyClass}`}>
            {urgency}
            <small>/100</small>
          </div>

        </div>

        <div className="urgency-track">

          <div
            className={`urgency-fill ${urgencyClass}`}
            style={{
              width: `${Math.min(100, urgency)}%`,
            }}
          ></div>

        </div>

        <div className="urgency-status">
          <span className={`status-dot ${urgencyClass}`}></span>

          {urgency >= 75
            ? "High-priority challenge"
            : urgency >= 50
              ? "Moderate-priority challenge"
              : "Lower-priority challenge"}
        </div>

      </div>

      {/* Skills */}
      <div className="dna-section">

        <div className="section-label">
          REQUIRED EXPERTISE
        </div>

        <div className="skill-list">

          {data?.skills_required?.length > 0 ? (
            data.skills_required.map(
              (skill, index) => (
                <div
                  className="skill-chip"
                  key={index}
                >
                  <span>◆</span>
                  {skill}
                </div>
              )
            )
          ) : (
            <span>No skills identified</span>
          )}

        </div>

      </div>

      {/* Cost */}
      <div className="dna-bottom-grid">

        <div className="metric">

          <div className="section-label">
            ESTIMATED COST
          </div>

          <div className="cost-value">
            {data?.estimated_cost ||
              "Not available"}
          </div>

        </div>

        <div className="metric">

          <div className="section-label">
            NEXT STEP
          </div>

          <div className="next-value">
            Find collaborators →
          </div>

        </div>

      </div>

      <div className="success-message">
        <span>✓</span>

        Challenge successfully analyzed and
        added to the JANSETU ecosystem.

      </div>

    </div>
  );
}

export default ReportChallenge;