import DashboardLayout from "../Layouts/DashboardLayout";

function CitizenDashboard() {
  return (
    <DashboardLayout>
      <div className="dashboard-header">
        <div>
          <p className="eyebrow">
            CITIZEN PORTAL
          </p>

          <h1>
            Good morning 👋
          </h1>

          <p>
            Turn community problems into meaningful solutions.
          </p>
        </div>

        <button className="primary-button">
          + Report a Problem
        </button>
      </div>

      <div className="stats-grid">
        <div className="stat-card">
          <span>Submitted Challenges</span>
          <strong>12</strong>
          <small>Total reported</small>
        </div>

        <div className="stat-card">
          <span>Active Projects</span>
          <strong>4</strong>
          <small>Currently progressing</small>
        </div>

        <div className="stat-card">
          <span>Resolved</span>
          <strong>2</strong>
          <small>Successfully completed</small>
        </div>

        <div className="stat-card">
          <span>Community Impact</span>
          <strong>87%</strong>
          <small>Impact contribution</small>
        </div>
      </div>

      <section className="dashboard-section">
        <div className="section-heading">
          <div>
            <h2>Recent Challenges</h2>
            <p>Your latest community submissions</p>
          </div>

          <button className="text-button">
            View all
          </button>
        </div>

        <div className="challenge-list">

          <div className="challenge-item">
            <div>
              <h3>School Road Flooding</h3>
              <p>
                Demo Village • Infrastructure
              </p>
            </div>

            <span className="status high">
              HIGH
            </span>

            <span className="status review">
              AI Review
            </span>
          </div>

          <div className="challenge-item">
            <div>
              <h3>Village Water Shortage</h3>
              <p>
                Demo Village • Water Management
              </p>
            </div>

            <span className="status medium">
              MEDIUM
            </span>

            <span className="status progress">
              In Progress
            </span>
          </div>

        </div>
      </section>
    </DashboardLayout>
  );
}

export default CitizenDashboard;