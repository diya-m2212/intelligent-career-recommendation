import { useState } from "react";
import CAREER_CONTENT from "./careerContent";
import "./App.css";

const skills = [
  ["python_skill", "Python"],
  ["java_skill", "Java"],
  ["sql_skill", "SQL"],
  ["programming_skill", "Programming"],
  ["statistics_skill", "Statistics"],
  ["mathematics_skill", "Mathematics"],
  ["linux_skill", "Linux"],
  ["networking_skill", "Networking"],
  ["cloud_skill", "Cloud Computing"],
  ["cybersecurity_skill", "Cybersecurity"],
  ["problem_solving", "Problem Solving"],
  ["analytical_thinking", "Analytical Thinking"],
];

const interests = [
  ["ai_interest", "AI / Machine Learning", "🤖"],
  ["data_interest", "Data Science", "📊"],
  ["software_interest", "Software Development", "💻"],
  ["cloud_interest", "Cloud Computing", "☁️"],
  ["security_interest", "Cybersecurity", "🔐"],
];

const initialForm = {
  education_level: "",
  cgpa: "",
  python_skill: 0,
  java_skill: 0,
  sql_skill: 0,
  programming_skill: 0,
  statistics_skill: 0,
  mathematics_skill: 0,
  linux_skill: 0,
  networking_skill: 0,
  cloud_skill: 0,
  cybersecurity_skill: 0,
  problem_solving: 0,
  analytical_thinking: 0,
  ai_interest: 0,
  data_interest: 0,
  software_interest: 0,
  cloud_interest: 0,
  security_interest: 0,
  number_of_projects: 0,
  number_of_certifications: 0,
};

function getCareerIcon(career) {
  if (career?.includes("Cloud")) return "☁️";
  if (career?.includes("Artificial")) return "🤖";
  if (career?.includes("Data")) return "📊";
  if (career?.includes("Software")) return "💻";
  if (career?.includes("Cyber")) return "🔐";

  return "🎯";
}

function formatDate(value) {
  if (!value) {
    return "—";
  }

  const date = new Date(value);

  if (Number.isNaN(date.getTime())) {
    return "—";
  }

  return date.toLocaleString("en-IN", {
    day: "2-digit",
    month: "short",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
}

/* =========================================================
   HEADER
   ========================================================= */

function Header({ onDashboard }) {
  return (
    <header className="site-header">
      <div className="nav">
        <div className="logo">
          <div className="logo-mark">✦</div>

          <div>
            <strong>CareerAI</strong>

            <span>
              Intelligent Career Guidance
            </span>
          </div>
        </div>

        <div className="nav-actions">
          <button
            type="button"
            className="dashboard-trigger"
            onClick={onDashboard}
          >
            ◫ Dashboard
          </button>

          <div className="nav-pill">
            <span></span>
            Powered by Machine Learning
          </div>
        </div>
      </div>
    </header>
  );
}

/* =========================================================
   FOOTER
   ========================================================= */

function Footer() {
  return (
    <footer className="footer">
      <strong>✦ CareerAI</strong>

      <span>
        MCA Project · Machine Learning · FastAPI · React · PostgreSQL
      </span>
    </footer>
  );
}

/* =========================================================
   ASSESSMENT PAGE
   ========================================================= */

function AssessmentPage({
  form,
  setForm,
  step,
  setStep,
  error,
  setError,
  loading,
  onSubmit,
  onReset,
}) {
  const updateField = (name, value) => {
    setForm((oldForm) => ({
      ...oldForm,
      [name]:
        name === "education_level"
          ? value
          : value === ""
          ? ""
          : Number(value),
    }));
  };

  return (
    <>
      <section className="hero">
        <div className="hero-content">
          <div className="hero-text">
            <div className="hero-badge">
              🎓 MACHINE LEARNING CAREER DISCOVERY
            </div>

            <h1>
              Your next career
              <br />
              starts with
              <span>
                understanding you.
              </span>
            </h1>

            <p>
              Tell us about your education, skills,
              interests and experience. Our system
              will recommend a career direction and
              build a personalized roadmap for you.
            </p>
          </div>
        </div>
      </section>

      <main className="assessment">
        <div className="assessment-top">
          <div>
            <span>CAREER ASSESSMENT</span>

            <h2>
              Step {step} of 3
            </h2>
          </div>

          <div className="progress">
            <div
              style={{
                width: `${step * 33.33}%`,
              }}
            />
          </div>
        </div>

        <div className="steps">
          <button
            type="button"
            className={
              step >= 1 ? "active" : ""
            }
            onClick={() => setStep(1)}
          >
            <b>01</b>
            <span>Profile</span>
          </button>

          <button
            type="button"
            className={
              step >= 2 ? "active" : ""
            }
            onClick={() => {
              if (step >= 2) {
                setStep(2);
              }
            }}
          >
            <b>02</b>
            <span>Skills</span>
          </button>

          <button
            type="button"
            className={
              step >= 3 ? "active" : ""
            }
            onClick={() => {
              if (step >= 3) {
                setStep(3);
              }
            }}
          >
            <b>03</b>
            <span>Interests</span>
          </button>
        </div>

        <div className="assessment-body">
          {step === 1 && (
            <section className="step-content">
              <div className="section-heading">
                <span>STEP 01</span>

                <h2>
                  Tell us about yourself.
                </h2>

                <p>
                  Start with your academic background
                  and practical experience.
                </p>
              </div>

              <div className="profile-grid">
                <label className="field">
                  <span>Education Level</span>

                  <select
                    value={form.education_level}
                    onChange={(event) =>
                      updateField(
                        "education_level",
                        event.target.value
                      )
                    }
                  >
                    <option value="">
                      Select education level
                    </option>

                    <option value="Graduation">
                      Graduation
                    </option>

                    <option value="Post Graduation">
                      Post Graduation
                    </option>
                  </select>
                </label>

                <label className="field">
                  <span>CGPA</span>

                  <input
                    type="number"
                    min="5.5"
                    max="10"
                    step="0.01"
                    placeholder="Enter your CGPA"
                    value={form.cgpa}
                    onChange={(event) =>
                      updateField(
                        "cgpa",
                        event.target.value
                      )
                    }
                  />
                </label>

                <label className="field">
                  <span>
                    Number of Projects
                  </span>

                  <input
                    type="number"
                    min="0"
                    placeholder="0"
                    value={
                      form.number_of_projects
                    }
                    onChange={(event) =>
                      updateField(
                        "number_of_projects",
                        event.target.value
                      )
                    }
                  />
                </label>

                <label className="field">
                  <span>
                    Certifications
                  </span>

                  <input
                    type="number"
                    min="0"
                    placeholder="0"
                    value={
                      form.number_of_certifications
                    }
                    onChange={(event) =>
                      updateField(
                        "number_of_certifications",
                        event.target.value
                      )
                    }
                  />
                </label>
              </div>
            </section>
          )}

          {step === 2 && (
            <section className="step-content">
              <div className="section-heading">
                <span>STEP 02</span>

                <h2>
                  What can you already do?
                </h2>

                <p>
                  Rate each technical skill from
                  1 to 5.
                </p>
              </div>

              <div className="skill-list">
                {skills.map(([key, label]) => (
                  <div
                    className="skill-row"
                    key={key}
                  >
                    <div>
                      <strong>{label}</strong>

                      <small>
                        Current ability
                      </small>
                    </div>

                    <div className="skill-buttons">
                      {[1, 2, 3, 4, 5].map(
                        (rating) => (
                          <button
                            type="button"
                            key={rating}
                            className={
                              form[key] === rating
                                ? "selected"
                                : ""
                            }
                            onClick={() =>
                              updateField(
                                key,
                                rating
                              )
                            }
                          >
                            {rating}
                          </button>
                        )
                      )}
                    </div>

                    <span className="skill-rating">
                      {form[key] === 0
                        ? "Not rated"
                        : `${form[key]}/5`}
                    </span>
                  </div>
                ))}
              </div>
            </section>
          )}

          {step === 3 && (
            <section className="step-content">
              <div className="section-heading">
                <span>STEP 03</span>

                <h2>
                  What are you interested in?
                </h2>

                <p>
                  Click each area to increase its
                  interest rating from 1 to 5.
                </p>
              </div>

              <div className="interest-grid">
                {interests.map(
                  ([key, label, icon]) => (
                    <button
                      type="button"
                      className={
                        form[key] >= 4
                          ? "interest selected"
                          : "interest"
                      }
                      key={key}
                      onClick={() => {
                        const nextValue =
                          form[key] >= 5
                            ? 1
                            : form[key] + 1;

                        updateField(
                          key,
                          nextValue
                        );
                      }}
                    >
                      <span className="interest-icon">
                        {icon}
                      </span>

                      <strong>{label}</strong>

                      <small>
                        Interest level
                      </small>

                      <div className="interest-dots">
                        {[1, 2, 3, 4, 5].map(
                          (rating) => (
                            <i
                              key={rating}
                              className={
                                rating <= form[key]
                                  ? "filled"
                                  : ""
                              }
                            />
                          )
                        )}
                      </div>

                      <b>
                        {form[key] === 0
                          ? "Not rated"
                          : `${form[key]}/5`}
                      </b>
                    </button>
                  )
                )}
              </div>
            </section>
          )}
        </div>

        {error && (
          <div className="error">
            <strong>
              Please complete your profile
            </strong>

            <span>{error}</span>
          </div>
        )}

        <div className="assessment-footer">
          <button
            type="button"
            className="secondary"
            onClick={
              step === 1
                ? onReset
                : () => setStep(step - 1)
            }
          >
            {step === 1 ? "Reset" : "← Back"}
          </button>

          {step < 3 ? (
            <button
              type="button"
              className="primary"
              onClick={() => {
                setError("");

                if (
                  step === 1 &&
                  (!form.education_level ||
                    form.cgpa === "")
                ) {
                  setError(
                    "Please complete your education level and CGPA before continuing."
                  );
                  return;
                }

                setStep(step + 1);

                window.scrollTo({
                  top: 0,
                  behavior: "smooth",
                });
              }}
            >
              Continue →
            </button>
          ) : (
            <button
              type="button"
              className="primary"
              onClick={onSubmit}
              disabled={loading}
            >
              {loading
                ? "Analyzing..."
                : "✨ Reveal My Career"}
            </button>
          )}
        </div>
      </main>
    </>
  );
}

/* =========================================================
   DASHBOARD PAGE
   ========================================================= */

function DashboardPage({
  data,
  loading,
  error,
  searchText,
  setSearchText,
  careerFilter,
  setCareerFilter,
  selectedId,
  setSelectedId,
  onBack,
  onRetry,
}) {
  const assessments = data?.assessments || [];

  const averageCgpa =
    assessments.length > 0
      ? assessments.reduce(
          (sum, item) =>
            sum + Number(item.cgpa || 0),
          0
        ) / assessments.length
      : 0;

  const averageMatch =
    assessments.length > 0
      ? assessments.reduce(
          (sum, item) =>
            sum +
            Number(
              item.top_match_score || 0
            ),
          0
        ) / assessments.length
      : 0;

  const totalProjects =
    assessments.reduce(
      (sum, item) =>
        sum +
        Number(
          item.number_of_projects || 0
        ),
      0
    );

  const careerCounts = {};

  assessments.forEach((item) => {
    const career =
      item.recommended_career ||
      "Unknown";

    careerCounts[career] =
      (careerCounts[career] || 0) + 1;
  });

  const careerDistribution =
    Object.entries(careerCounts).sort(
      (a, b) => b[1] - a[1]
    );

  const educationCounts = {};

  assessments.forEach((item) => {
    const education =
      item.education_level ||
      "Unknown";

    educationCounts[education] =
      (educationCounts[education] || 0) + 1;
  });

  const educationDistribution =
    Object.entries(educationCounts);

  const careerOptions = [
    "All",
    ...Object.keys(careerCounts),
  ];

  const filteredAssessments =
    assessments.filter((assessment) => {
      const query =
        searchText.trim().toLowerCase();

      const studentId = String(
        assessment.student_id ?? ""
      ).toLowerCase();

      const career = String(
        assessment.recommended_career ??
          ""
      ).toLowerCase();

      const education = String(
        assessment.education_level ?? ""
      ).toLowerCase();

      const matchesSearch =
        query === "" ||
        studentId.includes(query) ||
        career.includes(query) ||
        education.includes(query);

      const matchesCareer =
        careerFilter === "All" ||
        assessment.recommended_career ===
          careerFilter;

      return (
        matchesSearch &&
        matchesCareer
      );
    });

  const selectedAssessment =
    selectedId === null
      ? null
      : assessments.find(
          (item) =>
            item.student_id === selectedId
        ) || null;

  const educationChart = (() => {
    if (assessments.length === 0) {
      return "conic-gradient(#eee9e4 0deg 360deg)";
    }

    let current = 0;

    const segments =
      educationDistribution.map(
        ([, count], index) => {
          const start = current;

          current +=
            (count / assessments.length) *
            360;

          const segmentColor =
            index % 2 === 0
              ? "#7659dc"
              : "#927cf0";

          return `${segmentColor} ${start}deg ${current}deg`;
        }
      );

    return `conic-gradient(${segments.join(
      ", "
    )})`;
  })();

  return (
    <>
      <section className="dashboard-hero">
        <div className="dashboard-hero-content">
          <div className="dashboard-copy">
            <div className="hero-badge">
              📊 CAREERAI ANALYTICS
            </div>

            <h1>
              Your assessment
              <br />
              <span>
                dashboard.
              </span>
            </h1>

            <p>
              View career recommendations and
              assessment history stored in your
              PostgreSQL database.
            </p>

            <button
              type="button"
              className="dashboard-back"
              onClick={onBack}
            >
              ← Back to assessment
            </button>
          </div>
        </div>
      </section>

      <section className="dashboard-shell">
        {loading && (
          <div className="dashboard-loading">
            <div className="loading-orb">
              ✦
            </div>

            <h2>
              Loading dashboard
            </h2>

            <p>
              Reading data from PostgreSQL...
            </p>
          </div>
        )}

        {!loading && error && (
          <div className="dashboard-error">
            <strong>
              Dashboard unavailable
            </strong>

            <span>{error}</span>

            <button
              type="button"
              onClick={onRetry}
            >
              Try again
            </button>
          </div>
        )}

        {!loading &&
          !error &&
          data && (
            <>
              {/* =================================================
                  OVERVIEW
                  ================================================= */}

              <section className="dashboard-section">
                <div className="dashboard-heading">
                  <div>
                    <span>OVERVIEW</span>

                    <h2>
                      CareerAI at a glance.
                    </h2>

                    <p>
                      A live summary of saved
                      assessment records.
                    </p>
                  </div>

                  <div className="dashboard-status">
                    <span></span>
                    Database connected
                  </div>
                </div>

                <div className="dashboard-stats">
                  <article className="dashboard-stat">
                    <div className="dashboard-stat-icon purple">
                      ◉
                    </div>

                    <div>
                      <small>
                        TOTAL ASSESSMENTS
                      </small>

                      <strong>
                        {data.total_assessments}
                      </strong>

                      <span>
                        Saved records
                      </span>
                    </div>
                  </article>

                  <article className="dashboard-stat">
                    <div className="dashboard-stat-icon blue">
                      ✦
                    </div>

                    <div>
                      <small>
                        AVERAGE CGPA
                      </small>

                      <strong>
                        {averageCgpa.toFixed(2)}
                      </strong>

                      <span>
                        Across assessments
                      </span>
                    </div>
                  </article>

                  <article className="dashboard-stat">
                    <div className="dashboard-stat-icon green">
                      %
                    </div>

                    <div>
                      <small>
                        AVG. MATCH
                      </small>

                      <strong>
                        {averageMatch.toFixed(2)}%
                      </strong>

                      <span>
                        Average recommendation
                      </span>
                    </div>
                  </article>

                  <article className="dashboard-stat">
                    <div className="dashboard-stat-icon orange">
                      ▣
                    </div>

                    <div>
                      <small>
                        PROJECTS
                      </small>

                      <strong>
                        {totalProjects}
                      </strong>

                      <span>
                        Total reported
                      </span>
                    </div>
                  </article>
                </div>
              </section>

              {/* =================================================
                  VISUAL ANALYTICS
                  ================================================= */}

              <section className="dashboard-section">
                <div className="dashboard-heading">
                  <div>
                    <span>
                      VISUAL ANALYTICS
                    </span>

                    <h2>
                      What the data is saying.
                    </h2>

                    <p>
                      A visual view of career
                      recommendations, match strength
                      and education background.
                    </p>
                  </div>
                </div>

                <div className="visual-analytics-grid">
                  {/* CAREER DISTRIBUTION */}

                  <article className="visual-card">
                    <div className="visual-card-heading">
                      <div>
                        <small>
                          CAREER DISTRIBUTION
                        </small>

                        <h3>
                          Recommended paths
                        </h3>
                      </div>

                      <span>
                        {assessments.length} total
                      </span>
                    </div>

                    {careerDistribution.length ===
                    0 ? (
                      <div className="analytics-empty">
                        No career data available.
                      </div>
                    ) : (
                      <div className="chart-list">
                        {careerDistribution.map(
                          ([career, count]) => {
                            const percentage =
                              assessments.length >
                              0
                                ? (count /
                                    assessments.length) *
                                  100
                                : 0;

                            return (
                              <div
                                className="chart-row"
                                key={career}
                              >
                                <div className="chart-label">
                                  <span>
                                    {getCareerIcon(
                                      career
                                    )}
                                  </span>

                                  <strong>
                                    {career}
                                  </strong>
                                </div>

                                <div className="chart-bar">
                                  <div
                                    style={{
                                      width: `${percentage}%`,
                                    }}
                                  />
                                </div>

                                <b>
                                  {percentage.toFixed(
                                    0
                                  )}
                                  %
                                </b>
                              </div>
                            );
                          }
                        )}
                      </div>
                    )}
                  </article>

                  {/* MATCH SCORE */}

                  <article className="visual-card">
                    <div className="visual-card-heading">
                      <div>
                        <small>
                          MATCH SCORE
                        </small>

                        <h3>
                          Recommendation strength
                        </h3>
                      </div>

                      <span>
                        Live
                      </span>
                    </div>

                    {assessments.length === 0 ? (
                      <div className="analytics-empty">
                        No match data available.
                      </div>
                    ) : (
                      <div className="chart-list">
                        {assessments.map(
                          (assessment) => {
                            const score =
                              Number(
                                assessment.top_match_score ||
                                  0
                              );

                            return (
                              <div
                                className="chart-row"
                                key={`match-${assessment.student_id}`}
                              >
                                <div className="chart-label">
                                  <span>
                                    {getCareerIcon(
                                      assessment.recommended_career
                                    )}
                                  </span>

                                  <strong>
                                    #
                                    {
                                      assessment.student_id
                                    }{" "}
                                    {
                                      assessment.recommended_career
                                    }
                                  </strong>
                                </div>

                                <div className="chart-bar">
                                  <div
                                    style={{
                                      width: `${Math.min(
                                        score,
                                        100
                                      )}%`,
                                    }}
                                  />
                                </div>

                                <b>
                                  {score.toFixed(2)}
                                  %
                                </b>
                              </div>
                            );
                          }
                        )}
                      </div>
                    )}
                  </article>

                  {/* EDUCATION MIX */}

                  <article className="visual-card education-visual-card">
                    <div className="visual-card-heading">
                      <div>
                        <small>
                          EDUCATION MIX
                        </small>

                        <h3>
                          Student background
                        </h3>
                      </div>

                      <span>
                        {assessments.length} records
                      </span>
                    </div>

                    {educationDistribution.length ===
                    0 ? (
                      <div className="analytics-empty">
                        No education data available.
                      </div>
                    ) : (
                      <div className="education-chart">
                        <div
                          className="education-donut"
                          style={{
                            background:
                              educationChart,
                          }}
                        >
                          <div>
                            <strong>
                              {assessments.length}
                            </strong>

                            <span>
                              students
                            </span>
                          </div>
                        </div>

                        <div className="education-legend">
                          {educationDistribution.map(
                            (
                              [education, count],
                              index
                            ) => {
                              const percentage =
                                assessments.length >
                                0
                                  ? (count /
                                      assessments.length) *
                                    100
                                  : 0;

                              return (
                                <div
                                  className="legend-item"
                                  key={education}
                                >
                                  <span
                                    className={
                                      index === 0
                                        ? "legend-dot one"
                                        : "legend-dot two"
                                    }
                                  />

                                  <div>
                                    <strong>
                                      {education}
                                    </strong>

                                    <small>
                                      {count} student
                                      {count !== 1
                                        ? "s"
                                        : ""}
                                    </small>
                                  </div>

                                  <b>
                                    {percentage.toFixed(
                                      0
                                    )}
                                    %
                                  </b>
                                </div>
                              );
                            }
                          )}
                        </div>
                      </div>
                    )}
                  </article>
                </div>
              </section>

              {/* =================================================
                  DISTRIBUTION
                  ================================================= */}

              <section className="dashboard-section">
                <div className="dashboard-heading">
                  <div>
                    <span>
                      DISTRIBUTION
                    </span>

                    <h2>
                      Recommendation trends.
                    </h2>

                    <p>
                      Which career domains are
                      appearing most often?
                    </p>
                  </div>
                </div>

                <div className="dashboard-analysis">
                  <article className="analytics-card">
                    <div className="analytics-card-top">
                      <div>
                        <small>
                          CAREER DOMAINS
                        </small>

                        <h3>
                          Career distribution
                        </h3>
                      </div>

                      <span>
                        {assessments.length} records
                      </span>
                    </div>

                    {careerDistribution.length ===
                    0 ? (
                      <div className="analytics-empty">
                        No assessment data yet.
                      </div>
                    ) : (
                      <div className="distribution-list">
                        {careerDistribution.map(
                          ([career, count]) => {
                            const percentage =
                              assessments.length >
                              0
                                ? (count /
                                    assessments.length) *
                                  100
                                : 0;

                            return (
                              <div
                                className="distribution-row"
                                key={career}
                              >
                                <div className="distribution-label">
                                  <span>
                                    {getCareerIcon(
                                      career
                                    )}
                                  </span>

                                  <strong>
                                    {career}
                                  </strong>
                                </div>

                                <div className="distribution-track">
                                  <div
                                    style={{
                                      width: `${percentage}%`,
                                    }}
                                  />
                                </div>

                                <b>
                                  {count}
                                </b>
                              </div>
                            );
                          }
                        )}
                      </div>
                    )}
                  </article>

                  <article className="analytics-card">
                    <div className="analytics-card-top">
                      <div>
                        <small>
                          EDUCATION
                        </small>

                        <h3>
                          Student background
                        </h3>
                      </div>

                      <span>
                        {assessments.length} records
                      </span>
                    </div>

                    {educationDistribution.length ===
                    0 ? (
                      <div className="analytics-empty">
                        No education data yet.
                      </div>
                    ) : (
                      <div className="education-list">
                        {educationDistribution.map(
                          ([education, count]) => (
                            <div
                              className="education-card"
                              key={education}
                            >
                              <div className="education-icon">
                                🎓
                              </div>

                              <div className="education-info">
                                <strong>
                                  {education}
                                </strong>

                                <span>
                                  {count} assessment
                                  {count !== 1
                                    ? "s"
                                    : ""}
                                </span>
                              </div>

                              <b>
                                {(
                                  (count /
                                    assessments.length) *
                                  100
                                ).toFixed(0)}
                                %
                              </b>
                            </div>
                          )
                        )}
                      </div>
                    )}
                  </article>
                </div>
              </section>

              {/* =================================================
                  ASSESSMENT HISTORY
                  ================================================= */}

              <section className="dashboard-section">
                <div className="dashboard-heading">
                  <div>
                    <span>
                      ASSESSMENT HISTORY
                    </span>

                    <h2>
                      Recent assessments.
                    </h2>

                    <p>
                      These records come directly
                      from PostgreSQL.
                    </p>
                  </div>
                </div>

                <div className="assessment-filter-bar">
                  <input
                    type="text"
                    placeholder="🔎 Search student ID, career or education..."
                    value={searchText}
                    onChange={(event) =>
                      setSearchText(
                        event.target.value
                      )
                    }
                  />

                  <select
                    value={careerFilter}
                    onChange={(event) =>
                      setCareerFilter(
                        event.target.value
                      )
                    }
                  >
                    {careerOptions.map(
                      (career) => (
                        <option
                          key={career}
                          value={career}
                        >
                          {career === "All"
                            ? "All Careers"
                            : career}
                        </option>
                      )
                    )}
                  </select>

                  <button
                    type="button"
                    onClick={() => {
                      setSearchText("");
                      setCareerFilter("All");
                    }}
                  >
                    Clear
                  </button>
                </div>

                <div className="filter-count">
                  Showing{" "}
                  {filteredAssessments.length} of{" "}
                  {assessments.length} assessments
                </div>

                {filteredAssessments.length ===
                0 ? (
                  <div className="dashboard-empty">
                    <div>🔎</div>

                    <h3>
                      No matching assessments
                    </h3>

                    <p>
                      Try a different search term
                      or career filter.
                    </p>

                    <button
                      type="button"
                      onClick={() => {
                        setSearchText("");
                        setCareerFilter("All");
                      }}
                    >
                      Clear filters →
                    </button>
                  </div>
                ) : (
                  <div className="assessment-history">
                    {filteredAssessments.map(
                      (assessment) => {
                        const match =
                          Number(
                            assessment.top_match_score ||
                              0
                          );

                        const isSelected =
                          selectedId ===
                          assessment.student_id;

                        return (
                          <article
                            className={
                              isSelected
                                ? "history-card selected"
                                : "history-card"
                            }
                            key={`${assessment.student_id}-${assessment.created_at}`}
                          >
                            <div className="history-number">
                              #
                              {
                                assessment.student_id
                              }
                            </div>

                            <div className="history-main">
                              <div className="history-career">
                                <div className="history-career-icon">
                                  {getCareerIcon(
                                    assessment.recommended_career
                                  )}
                                </div>

                                <div>
                                  <small>
                                    RECOMMENDED CAREER
                                  </small>

                                  <h3>
                                    {
                                      assessment.recommended_career
                                    }
                                  </h3>
                                </div>
                              </div>

                              <div className="history-meta">
                                <span>
                                  🎓{" "}
                                  {
                                    assessment.education_level
                                  }
                                </span>

                                <span>
                                  GPA{" "}
                                  {Number(
                                    assessment.cgpa
                                  ).toFixed(2)}
                                </span>

                                <span>
                                  ▣{" "}
                                  {
                                    assessment.number_of_projects
                                  }{" "}
                                  projects
                                </span>

                                <span>
                                  ◇{" "}
                                  {
                                    assessment.number_of_certifications
                                  }{" "}
                                  certs
                                </span>
                              </div>
                            </div>

                            <div className="history-score">
                              <small>
                                MATCH
                              </small>

                              <strong>
                                {match.toFixed(2)}%
                              </strong>

                              <span>
                                {formatDate(
                                  assessment.created_at
                                )}
                              </span>
                            </div>

                            <button
                              type="button"
                              className="history-view"
                              onClick={() => {
                                if (
                                  isSelected
                                ) {
                                  setSelectedId(
                                    null
                                  );
                                } else {
                                  setSelectedId(
                                    assessment.student_id
                                  );
                                }
                              }}
                            >
                              {isSelected
                                ? "Hide"
                                : "View"}
                            </button>
                          </article>
                        );
                      }
                    )}
                  </div>
                )}
              </section>

              {/* =================================================
                  SELECTED ASSESSMENT
                  ================================================= */}

              {selectedAssessment && (
                <section className="assessment-detail">
                  <div className="detail-heading">
                    <div>
                      <span>
                        ASSESSMENT #
                        {
                          selectedAssessment.student_id
                        }
                      </span>

                      <h2>
                        Recommendation breakdown.
                      </h2>
                    </div>

                    <button
                      type="button"
                      onClick={() =>
                        setSelectedId(null)
                      }
                    >
                      Close ×
                    </button>
                  </div>

                  <div className="detail-grid">
                    <div className="detail-profile">
                      <div className="detail-avatar">
                        {getCareerIcon(
                          selectedAssessment.recommended_career
                        )}
                      </div>

                      <small>
                        RECOMMENDED CAREER
                      </small>

                      <h3>
                        {
                          selectedAssessment.recommended_career
                        }
                      </h3>

                      <p>
                        {
                          selectedAssessment.education_level
                        }
                        {" · "}
                        CGPA{" "}
                        {Number(
                          selectedAssessment.cgpa
                        ).toFixed(2)}
                      </p>
                    </div>

                    <div className="detail-scores">
                      <div className="detail-score-title">
                        <span>
                          MATCH SCORES
                        </span>

                        <strong>
                          {Number(
                            selectedAssessment.top_match_score
                          ).toFixed(2)}
                          %
                        </strong>
                      </div>

                      {Object.entries(
                        selectedAssessment.match_scores ||
                          {}
                      )
                        .sort(
                          (a, b) =>
                            Number(b[1]) -
                            Number(a[1])
                        )
                        .map(
                          ([career, score]) => (
                            <div
                              className="detail-score-row"
                              key={career}
                            >
                              <span>
                                {getCareerIcon(
                                  career
                                )}
                              </span>

                              <strong>
                                {career}
                              </strong>

                              <div>
                                <i
                                  style={{
                                    width: `${Math.min(
                                      Number(
                                        score
                                      ),
                                      100
                                    )}%`,
                                  }}
                                />
                              </div>

                              <b>
                                {Number(
                                  score
                                ).toFixed(2)}
                                %
                              </b>
                            </div>
                          )
                        )}
                    </div>
                  </div>
                </section>
              )}
            </>
          )}
      </section>
    </>
  );
}

/* =========================================================
   RESULTS PAGE
   ========================================================= */

function ResultsPage({
  result,
  topScore,
  sortedScores,
  careerContent,
  onReset,
}) {
  return (
    <main className="results" id="results">
      <button
        type="button"
        className="new-assessment"
        onClick={onReset}
      >
        ← Start a new assessment
      </button>

      <section className="recommendation">
        <div>
          <span className="result-label">
            ✦ YOUR BEST MATCH
          </span>

          <div className="result-icon">
            {careerContent?.icon ||
              getCareerIcon(
                result.recommended_career
              )}
          </div>

          <h1>
            {result.recommended_career}
          </h1>

          <p>
            {careerContent?.description ||
              "This career was selected based on your profile."}
          </p>
        </div>

        <div
          className="match-circle"
          style={{
            background: `conic-gradient(
              #a78bfa ${Math.min(topScore, 100)}%,
              rgba(255,255,255,0.12) ${Math.min(
                topScore,
                100
              )}% 100%
            )`,
          }}
        >
          <div>
            <strong>
              {topScore.toFixed(2)}%
            </strong>

            <span>
              match
            </span>
          </div>
        </div>
      </section>

      <section className="result-section">
        <div className="result-title">
          <span>
            01 / CAREER FIT
          </span>

          <h2>
            Your career landscape
          </h2>

          <p>
            How well your profile matches
            each career domain.
          </p>
        </div>

        <div className="scores">
          {sortedScores.map(
            ([career, score], index) => (
              <div
                className={
                  index === 0
                    ? "score best"
                    : "score"
                }
                key={career}
              >
                <div className="score-name">
                  <span>
                    {getCareerIcon(career)}
                  </span>

                  <strong>
                    {career}
                  </strong>
                </div>

                <div className="score-track">
                  <div
                    style={{
                      width: `${Math.min(
                        Number(score),
                        100
                      )}%`,
                    }}
                  />
                </div>

                <b>
                  {Number(score).toFixed(2)}%
                </b>
              </div>
            )
          )}
        </div>
      </section>

      <section className="result-section">
        <div className="result-title">
          <span>
            02 / INSIGHTS
          </span>

          <h2>
            Understand your result.
          </h2>
        </div>

        <div className="insight-grid">
          <article>
            <span>💡</span>

            <h3>
              Why this career?
            </h3>

            <p>
              {result.why_this_career}
            </p>
          </article>

          <article>
            <span>🔍</span>

            <h3>
              Skill gap
            </h3>

            <p>
              {result.skill_gap_analysis}
            </p>
          </article>

          <article>
            <span>📈</span>

            <h3>
              Improve next
            </h3>

            <p>
              {result.improvement_suggestions}
            </p>
          </article>
        </div>
      </section>

      <section className="result-section">
        <div className="result-title">
          <span>
            03 / BUILD
          </span>

          <h2>
            Projects for your path.
          </h2>

          <p>
            Build practical evidence of your
            skills.
          </p>
        </div>

        {careerContent && (
          <div className="project-grid">
            {careerContent.projects.map(
              (project) => (
                <article
                  className="project"
                  key={project.title}
                >
                  <div>
                    {project.icon}
                  </div>

                  <small>
                    {project.title}
                  </small>

                  <h3>
                    {project.title.replace(
                      " Project",
                      ""
                    )}
                  </h3>

                  <p>
                    {project.description}
                  </p>
                </article>
              )
            )}
          </div>
        )}

        <details>
          <summary>
            View detailed project recommendations
          </summary>

          <p>
            {result.recommended_projects}
          </p>
        </details>
      </section>

      <section className="result-section">
        <div className="result-title">
          <span>
            04 / ROADMAP
          </span>

          <h2>
            Your journey starts here.
          </h2>

          <p>
            Follow these stages toward
            career readiness.
          </p>
        </div>

        {careerContent && (
          <div className="roadmap">
            {careerContent.roadmap.map(
              ([number, title, description]) => (
                <article
                  key={number}
                >
                  <span>{number}</span>

                  <div>
                    <small>
                      PHASE {number}
                    </small>

                    <h3>
                      {title}
                    </h3>

                    <p>
                      {description}
                    </p>
                  </div>
                </article>
              )
            )}
          </div>
        )}

        <details>
          <summary>
            View full personalized roadmap
          </summary>

          <p>
            {result.personalized_roadmap}
          </p>
        </details>
      </section>

      <section className="final-message">
        <span>✦</span>

        <h2>
          Your career isn't chosen.
          <br />
          It's built.
        </h2>

        <p>
          Keep learning, build projects and follow
          your roadmap one step at a time.
        </p>

        <button
          type="button"
          onClick={onReset}
        >
          Start Again →
        </button>
      </section>
    </main>
  );
}

/* =========================================================
   MAIN APP
   ========================================================= */

function App() {
  const [form, setForm] =
    useState(initialForm);

  const [step, setStep] =
    useState(1);

  const [result, setResult] =
    useState(null);

  const [loading, setLoading] =
    useState(false);

  const [error, setError] =
    useState("");

  const [showDashboard, setShowDashboard] =
    useState(false);

  const [dashboardLoading, setDashboardLoading] =
    useState(false);

  const [dashboardError, setDashboardError] =
    useState("");

  const [dashboardData, setDashboardData] =
    useState(null);

  const [searchText, setSearchText] =
    useState("");

  const [careerFilter, setCareerFilter] =
    useState("All");

  const [selectedId, setSelectedId] =
    useState(null);

  const validateForm = () => {
    if (!form.education_level) {
      return {
        step: 1,
        message:
          "Please select your education level.",
      };
    }

    if (
      form.cgpa === "" ||
      Number(form.cgpa) < 5.5 ||
      Number(form.cgpa) > 10
    ) {
      return {
        step: 1,
        message:
          "Please enter a valid CGPA between 5.5 and 10.",
      };
    }

    if (
      Number(form.number_of_projects) < 0
    ) {
      return {
        step: 1,
        message:
          "Please enter a valid number of projects.",
      };
    }

    if (
      Number(
        form.number_of_certifications
      ) < 0
    ) {
      return {
        step: 1,
        message:
          "Please enter a valid number of certifications.",
      };
    }

    const missingSkill = skills.find(
      ([key]) =>
        Number(form[key]) < 1
    );

    if (missingSkill) {
      return {
        step: 2,
        message: `Please rate your ${missingSkill[1]} skill.`,
      };
    }

    const missingInterest = interests.find(
      ([key]) =>
        Number(form[key]) < 1
    );

    if (missingInterest) {
      return {
        step: 3,
        message: `Please rate your interest in ${missingInterest[1]}.`,
      };
    }

    return null;
  };

  const submitRecommendation = async () => {
    setError("");

    const validationError =
      validateForm();

    if (validationError) {
      setStep(
        validationError.step
      );

      setError(
        validationError.message
      );

      window.scrollTo({
        top: 0,
        behavior: "smooth",
      });

      return;
    }

    setLoading(true);

    try {
      const response =
        await fetch(
          "/api/recommend",
          {
            method: "POST",
            headers: {
              "Content-Type":
                "application/json",
            },
            body: JSON.stringify({
              ...form,
              cgpa: Number(
                form.cgpa
              ),
              number_of_projects:
                Number(
                  form.number_of_projects
                ),
              number_of_certifications:
                Number(
                  form.number_of_certifications
                ),
            }),
          }
        );

      const data =
        await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail
            ? JSON.stringify(
                data.detail
              )
            : "Recommendation request failed."
        );
      }

      setResult(data);

      setTimeout(() => {
        document
          .getElementById(
            "results"
          )
          ?.scrollIntoView({
            behavior:
              "smooth",
          });
      }, 100);
    } catch (err) {
      setError(
        err.message ||
          "Could not connect to FastAPI."
      );
    } finally {
      setLoading(false);
    }
  };

  const loadDashboard =
    async () => {
      setShowDashboard(true);
      setDashboardLoading(true);
      setDashboardError("");
      setDashboardData(null);
      setSearchText("");
      setCareerFilter("All");
      setSelectedId(null);

      window.scrollTo({
        top: 0,
        behavior: "smooth",
      });

      try {
        const response =
          await fetch(
            "/api/assessments"
          );

        const data =
          await response.json();

        if (!response.ok) {
          throw new Error(
            data.detail ||
              "Could not load assessment history."
          );
        }

        const assessments =
          Array.isArray(
            data.assessments
          )
            ? [
                ...data.assessments,
              ].sort(
                (a, b) =>
                  new Date(
                    b.created_at
                  ) -
                  new Date(
                    a.created_at
                  )
              )
            : [];

        setDashboardData({
          total_assessments:
            Number(
              data.total_assessments
            ) ||
            assessments.length,
          assessments,
        });
      } catch (err) {
        setDashboardError(
          err.message ||
            "Could not load dashboard data."
        );
      } finally {
        setDashboardLoading(
          false
        );
      }
    };

  const resetAll = () => {
    setForm(initialForm);
    setStep(1);
    setResult(null);
    setError("");
    setShowDashboard(false);
    setDashboardError("");
    setDashboardData(null);
    setSelectedId(null);
    setSearchText("");
    setCareerFilter("All");

    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  };

  const sortedScores =
    result
      ? Object.entries(
          result.match_scores ||
            {}
        ).sort(
          (a, b) =>
            Number(b[1]) -
            Number(a[1])
        )
      : [];

  const topScore =
    sortedScores.length > 0
      ? Number(
          sortedScores[0][1]
        )
      : 0;

  const careerContent =
    result &&
    CAREER_CONTENT[
      result.career_code
    ]
      ? CAREER_CONTENT[
          result.career_code
        ]
      : null;

  if (showDashboard) {
    return (
      <div className="app">
        <Header
          onDashboard={
            loadDashboard
          }
        />

        <DashboardPage
          data={
            dashboardData
          }
          loading={
            dashboardLoading
          }
          error={
            dashboardError
          }
          searchText={
            searchText
          }
          setSearchText={
            setSearchText
          }
          careerFilter={
            careerFilter
          }
          setCareerFilter={
            setCareerFilter
          }
          selectedId={
            selectedId
          }
          setSelectedId={
            setSelectedId
          }
          onBack={() => {
            setShowDashboard(
              false
            );

            setSelectedId(
              null
            );

            window.scrollTo({
              top: 0,
              behavior:
                "smooth",
            });
          }}
          onRetry={
            loadDashboard
          }
        />

        <Footer />
      </div>
    );
  }

  if (!result) {
    return (
      <div className="app">
        <Header
          onDashboard={
            loadDashboard
          }
        />

        <AssessmentPage
          form={form}
          setForm={setForm}
          step={step}
          setStep={setStep}
          error={error}
          setError={setError}
          loading={loading}
          onSubmit={
            submitRecommendation
          }
          onReset={
            resetAll
          }
        />

        <Footer />
      </div>
    );
  }

  return (
    <div className="app">
      <Header
        onDashboard={
          loadDashboard
        }
      />

      <ResultsPage
        result={result}
        topScore={topScore}
        sortedScores={
          sortedScores
        }
        careerContent={
          careerContent
        }
        onReset={
          resetAll
        }
      />

      <Footer />
    </div>
  );
}

export default App;