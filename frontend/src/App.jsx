import { Routes, Route, Link } from "react-router-dom";
import ReportChallenge from "./pages/ReportChallenge";
import "./App.css";

/* =========================
   HOME PAGE
========================= */

function Home() {
  return (
    <div className="home-page">

      {/* NAVBAR */}
      <nav className="navbar">

        <Link to="/" className="logo">
          <div className="logo-mark">J</div>

          <div className="logo-text">
            <strong>JANSETU AI</strong>
            <span>Societal Innovation Network</span>
          </div>
        </Link>

        <div className="nav-links">
          <a href="#how-it-works">How It Works</a>
          <a href="#ecosystem">Ecosystem</a>
          <a href="#impact">Impact</a>
        </div>

        <div className="nav-actions">
          <Link to="/login" className="login-btn">
            Login
          </Link>

          <Link to="/report" className="nav-report-btn">
            Report a Problem
            <span>→</span>
          </Link>
        </div>

      </nav>


      {/* HERO */}
      <section className="hero-section">

        <div className="hero-content">

          <div className="status-badge">
            <span className="status-dot"></span>
            AI-POWERED SOCIETAL INNOVATION
          </div>

          <h1>
            Turn community
            <br />

            <span>problems into solutions.</span>
          </h1>

          <p className="hero-description">
            JANSETU AI connects citizens, universities,
            industry and government to transform real-world
            societal challenges into measurable solutions.
          </p>

          <div className="hero-buttons">

            <Link
              to="/report"
              className="primary-btn"
            >
              <span>+</span>
              Report a Community Problem
              <strong>→</strong>
            </Link>

            <a
              href="#how-it-works"
              className="secondary-btn"
            >
              Explore the Platform
              <span>↓</span>
            </a>

          </div>

          <div className="hero-trust">

            <div>
              <strong>AI</strong>
              <span>Problem Intelligence</span>
            </div>

            <div className="trust-divider"></div>

            <div>
              <strong>4+</strong>
              <span>Ecosystem Partners</span>
            </div>

            <div className="trust-divider"></div>

            <div>
              <strong>∞</strong>
              <span>Scalable Solutions</span>
            </div>

          </div>

        </div>


        {/* HERO VISUAL */}
        <div className="hero-visual">

          <div className="visual-grid"></div>

          <div className="orbit orbit-large"></div>
          <div className="orbit orbit-small"></div>

          <div className="center-node">

            <div className="center-icon">
              ✦
            </div>

            <strong>JANSETU</strong>
            <span>AI ENGINE</span>

          </div>


          <div className="floating-node citizen-node">
            <div className="node-icon">👤</div>
            <div>
              <strong>Citizens</strong>
              <span>Problems</span>
            </div>
          </div>


          <div className="floating-node university-node">
            <div className="node-icon">🎓</div>
            <div>
              <strong>Universities</strong>
              <span>Expertise</span>
            </div>
          </div>


          <div className="floating-node industry-node">
            <div className="node-icon">🏢</div>
            <div>
              <strong>Industry</strong>
              <span>Resources</span>
            </div>
          </div>


          <div className="floating-node government-node">
            <div className="node-icon">🏛</div>
            <div>
              <strong>Government</strong>
              <span>Impact</span>
            </div>
          </div>

        </div>

      </section>


      {/* HOW IT WORKS */}
      <section
        className="section"
        id="how-it-works"
      >

        <div className="section-heading">

          <div className="section-number">
            01
          </div>

          <div>
            <span className="section-label">
              THE INTELLIGENCE LOOP
            </span>

            <h2>
              From problem to
              <span> measurable impact.</span>
            </h2>

            <p>
              JANSETU AI creates a complete pathway from
              citizen reporting to real-world deployment.
            </p>
          </div>

        </div>


        <div className="process-grid">

          <ProcessCard
            number="01"
            icon="📍"
            title="Report"
            description="Citizens submit real problems affecting their communities."
          />

          <ProcessCard
            number="02"
            icon="🧠"
            title="Understand"
            description="AI analyzes, categorizes and creates a Problem DNA."
          />

          <ProcessCard
            number="03"
            icon="🔗"
            title="Connect"
            description="The right universities, experts and industries are matched."
          />

          <ProcessCard
            number="04"
            icon="🚀"
            title="Solve"
            description="Teams build, test and deploy practical solutions."
          />

        </div>

      </section>


      {/* ECOSYSTEM */}
      <section
        className="ecosystem-section"
        id="ecosystem"
      >

        <div className="ecosystem-content">

          <div className="section-number dark-number">
            02
          </div>

          <span className="dark-label">
            ONE CONNECTED ECOSYSTEM
          </span>

          <h2>
            Everyone brings
            <br />
            <span>something different.</span>
          </h2>

          <p>
            JANSETU AI creates the intelligence layer
            connecting the people who identify problems
            with the people who can solve them.
          </p>

        </div>


        <div className="ecosystem-cards">

          <div className="eco-card">
            <div className="eco-icon">👤</div>
            <span>01</span>
            <h3>Citizens</h3>
            <p>
              Identify and report challenges
              from the ground.
            </p>
          </div>

          <div className="eco-card">
            <div className="eco-icon">🎓</div>
            <span>02</span>
            <h3>Universities</h3>
            <p>
              Provide research, students
              and technical expertise.
            </p>
          </div>

          <div className="eco-card">
            <div className="eco-icon">🏢</div>
            <span>03</span>
            <h3>Industry</h3>
            <p>
              Bring technology, funding
              and deployment capability.
            </p>
          </div>

          <div className="eco-card">
            <div className="eco-icon">🏛</div>
            <span>04</span>
            <h3>Government</h3>
            <p>
              Prioritize challenges and
              measure community impact.
            </p>
          </div>

        </div>

      </section>


      {/* IMPACT */}
      <section
        className="impact-section"
        id="impact"
      >

        <div className="impact-heading">

          <span className="section-label">
            03 · BUILT FOR SCALE
          </span>

          <h2>
            A smarter way to
            <br />
            <span>solve societal challenges.</span>
          </h2>

        </div>


        <div className="impact-stats">

          <div>
            <strong>01</strong>
            <span>Unified challenge intelligence</span>
          </div>

          <div>
            <strong>AI</strong>
            <span>Automated problem analysis</span>
          </div>

          <div>
            <strong>360°</strong>
            <span>End-to-end project lifecycle</span>
          </div>

          <div>
            <strong>∞</strong>
            <span>Reusable solutions</span>
          </div>

        </div>

      </section>


      {/* CTA */}
      <section className="cta-section">

        <div className="cta-content">

          <div className="cta-icon">
            ✦
          </div>

          <span>
            READY TO CREATE IMPACT?
          </span>

          <h2>
            Your community has a problem.
            <br />
            <span>Let's build the solution.</span>
          </h2>

          <Link
            to="/report"
            className="cta-button"
          >
            Report a Problem
            <strong>→</strong>
          </Link>

        </div>

      </section>


      {/* FOOTER */}
      <footer className="footer">

        <div className="footer-brand">

          <div className="logo-mark">
            J
          </div>

          <div>
            <strong>JANSETU AI</strong>
            <span>
              Societal Innovation Network
            </span>
          </div>

        </div>

        <p>
          Turning societal challenges into
          collaborative innovation.
        </p>

        <span className="footer-copy">
          © 2026 JANSETU AI · SIH Prototype
        </span>

      </footer>

    </div>
  );
}


/* =========================
   PROCESS CARD
========================= */

function ProcessCard({
  number,
  icon,
  title,
  description,
}) {
  return (
    <div className="process-card">

      <div className="process-top">

        <span>{number}</span>

        <div className="process-icon">
          {icon}
        </div>

      </div>

      <h3>{title}</h3>

      <p>{description}</p>

      <div className="card-arrow">
        →
      </div>

    </div>
  );
}


/* =========================
   SIMPLE PAGES
========================= */

function Login() {
  return (
    <div className="simple-page">

      <div className="simple-card">

        <div className="logo-mark">
          J
        </div>

        <h1>Welcome back</h1>

        <p>
          JANSETU AI account access will be
          connected to the backend next.
        </p>

        <Link
          to="/citizen/dashboard"
          className="primary-btn simple-btn"
        >
          Continue to Dashboard →
        </Link>

        <Link to="/" className="simple-back">
          ← Back to JANSETU
        </Link>

      </div>

    </div>
  );
}


function Dashboard() {
  return (
    <div className="dashboard-placeholder">

      <div className="placeholder-card">

        <span className="section-label">
          CITIZEN PORTAL
        </span>

        <h1>
          Welcome to your dashboard.
        </h1>

        <p>
          Your personalized challenge workspace
          will appear here.
        </p>

        <Link
          to="/report"
          className="primary-btn simple-btn"
        >
          + Report a Problem
        </Link>

      </div>

    </div>
  );
}


/* =========================
   ROUTES
========================= */

function App() {
  return (
    <Routes>

      <Route
        path="/"
        element={<Home />}
      />

      <Route
        path="/report"
        element={<ReportChallenge />}
      />

      <Route
        path="/login"
        element={<Login />}
      />

      <Route
        path="/citizen/dashboard"
        element={<Dashboard />}
      />

      <Route
        path="/challenges"
        element={
          <Dashboard />
        }
      />

      <Route
        path="/projects"
        element={
          <Dashboard />
        }
      />

      <Route
        path="/solutions"
        element={
          <Dashboard />
        }
      />

      <Route
        path="/universities"
        element={
          <Dashboard />
        }
      />

      <Route
        path="/industry"
        element={
          <Dashboard />
        }
      />

      <Route
        path="/analytics"
        element={
          <Dashboard />
        }
      />

    </Routes>
  );
}

export default App;