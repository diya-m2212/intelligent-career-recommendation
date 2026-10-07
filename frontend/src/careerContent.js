// ============================================================
// DYNAMIC CAREER CONTENT
// ============================================================

const CAREER_CONTENT = {
  AI_ML: {
    icon: "🤖",
    description:
      "A strong path for students interested in artificial intelligence, machine learning, mathematics, statistics and intelligent systems.",

    projects: [
      {
        icon: "🌱",
        title: "Beginner Project",
        description:
          "Build a Student Performance Prediction system using Python, Pandas and basic machine learning."
      },
      {
        icon: "📊",
        title: "Intermediate Project",
        description:
          "Build a Customer Churn Prediction system using data preprocessing, feature engineering and classification."
      },
      {
        icon: "🧠",
        title: "Advanced Project",
        description:
          "Build an end-to-end AI recommendation system with model training, prediction APIs and a web interface."
      }
    ],

    roadmap: [
      ["1", "Python & Math", "Python, NumPy, Pandas, mathematics and statistics"],
      ["2", "Machine Learning", "Regression, classification, clustering and evaluation"],
      ["3", "Deep Learning", "Neural networks, CNNs and modern AI concepts"],
      ["4", "AI Projects", "Build practical ML and AI applications"],
      ["5", "Career Preparation", "Portfolio, internships, GitHub and interviews"]
    ]
  },

  Data_Science: {
    icon: "📊",
    description:
      "A strong path for students who enjoy data analysis, statistics, SQL, Python and solving business problems using data.",

    projects: [
      {
        icon: "🌱",
        title: "Beginner Project",
        description:
          "Build a Sales Data Analysis dashboard using Python, Pandas, SQL and visualization."
      },
      {
        icon: "📈",
        title: "Intermediate Project",
        description:
          "Build a customer analysis project with data cleaning, exploratory analysis and visualization."
      },
      {
        icon: "🧠",
        title: "Advanced Project",
        description:
          "Build an end-to-end data science solution combining analytics, machine learning and an API."
      }
    ],

    roadmap: [
      ["1", "Python & SQL", "Python, Pandas, NumPy and SQL fundamentals"],
      ["2", "Statistics", "Probability, statistics and data interpretation"],
      ["3", "Data Analysis", "EDA, visualization and feature engineering"],
      ["4", "Machine Learning", "Predictive models and model evaluation"],
      ["5", "Career Preparation", "Portfolio, projects, internships and interviews"]
    ]
  },

  Software_Development: {
    icon: "💻",
    description:
      "A strong path for students who enjoy programming, application development, problem solving and building software products.",

    projects: [
      {
        icon: "🌱",
        title: "Beginner Project",
        description:
          "Build a Student Management System using Java, OOP concepts and a relational database."
      },
      {
        icon: "⚙️",
        title: "Intermediate Project",
        description:
          "Build a REST API using Spring Boot with authentication, database integration and CRUD operations."
      },
      {
        icon: "🚀",
        title: "Advanced Project",
        description:
          "Build a complete full-stack application with React, Spring Boot, PostgreSQL and deployment."
      }
    ],

    roadmap: [
      ["1", "Programming", "Java, Python, OOP and problem solving"],
      ["2", "DSA", "Arrays, strings, recursion, trees and algorithms"],
      ["3", "Backend", "Spring Boot, REST APIs, databases and authentication"],
      ["4", "Full Stack", "React, APIs, PostgreSQL and deployment"],
      ["5", "Career Preparation", "GitHub, projects, internships and coding interviews"]
    ]
  },

  Cloud_Computing: {
    icon: "☁️",
    description:
      "A strong path for students interested in cloud infrastructure, deployment, networking, Linux and scalable applications.",

    projects: [
      {
        icon: "🌱",
        title: "Beginner Project",
        description:
          "Deploy a personal portfolio website to a cloud platform and learn basic Linux and hosting."
      },
      {
        icon: "📦",
        title: "Intermediate Project",
        description:
          "Build a cloud-based file storage application using object storage, Python and REST APIs."
      },
      {
        icon: "🏗️",
        title: "Advanced Project",
        description:
          "Build and deploy a cloud-native application using compute, database, networking and security services."
      }
    ],

    roadmap: [
      ["1", "Foundation", "Linux, networking, programming and cloud basics"],
      ["2", "Cloud Core", "AWS/Azure/GCP, compute, storage and IAM"],
      ["3", "Advanced", "Containers, Docker, Kubernetes and CI/CD"],
      ["4", "Projects", "Deploy practical cloud applications"],
      ["5", "Career Preparation", "Certifications, internships and interviews"]
    ]
  },

  Cybersecurity: {
    icon: "🔐",
    description:
      "A strong path for students interested in protecting systems, networks and applications from security threats.",

    projects: [
      {
        icon: "🌱",
        title: "Beginner Project",
        description:
          "Build a password strength and security auditing tool using Python."
      },
      {
        icon: "🛡️",
        title: "Intermediate Project",
        description:
          "Build a network monitoring or vulnerability assessment project using Python and Linux."
      },
      {
        icon: "🔎",
        title: "Advanced Project",
        description:
          "Build a security monitoring platform that analyzes logs and detects suspicious activity."
      }
    ],

    roadmap: [
      ["1", "Foundation", "Linux, networking, operating systems and security basics"],
      ["2", "Security Core", "Authentication, cryptography and common vulnerabilities"],
      ["3", "Security Tools", "Wireshark, Nmap, Linux security and monitoring"],
      ["4", "Security Projects", "Build practical defensive security projects"],
      ["5", "Career Preparation", "Labs, certifications, internships and interviews"]
    ]
  }
};

export default CAREER_CONTENT;