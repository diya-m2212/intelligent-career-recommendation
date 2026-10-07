# ============================================================
# PERSONALIZED CAREER ROADMAP
# ============================================================

CAREER_NAMES = {
    "AI_ML": "Artificial Intelligence / Machine Learning",
    "Data_Science": "Data Science",
    "Software_Development": "Software Development",
    "Cloud_Computing": "Cloud Computing",
    "Cybersecurity": "Cybersecurity"
}


# ------------------------------------------------------------
# Career Roadmap Content
# ------------------------------------------------------------

ROADMAPS = {

    "AI_ML": {
        "foundation": [
            "Python programming",
            "NumPy and Pandas",
            "Basic statistics",
            "Basic mathematics for Machine Learning"
        ],
        "core": [
            "Machine Learning fundamentals",
            "Supervised and unsupervised learning",
            "Data preprocessing",
            "Model evaluation",
            "Scikit-learn"
        ],
        "advanced": [
            "Feature engineering",
            "Model optimization",
            "Deep Learning fundamentals",
            "Neural Networks",
            "Natural Language Processing"
        ],
        "projects": [
            "Student Performance Prediction",
            "Career Recommendation System",
            "Image Classification System"
        ],
        "career": [
            "Build a strong GitHub portfolio",
            "Participate in ML projects and competitions",
            "Prepare Machine Learning interview questions",
            "Apply for ML internships and entry-level roles"
        ]
    },

    "Data_Science": {
        "foundation": [
            "Python programming",
            "NumPy and Pandas",
            "Basic statistics",
            "Data visualization"
        ],
        "core": [
            "SQL",
            "Data cleaning",
            "Exploratory Data Analysis",
            "Statistical analysis",
            "Matplotlib and Seaborn",
            "Scikit-learn"
        ],
        "advanced": [
            "Feature engineering",
            "Machine Learning",
            "Advanced statistics",
            "Time-series analysis",
            "Business analytics"
        ],
        "projects": [
            "Student Data Analysis Dashboard",
            "Sales Data Analytics System",
            "Business Intelligence Analytics Platform"
        ],
        "career": [
            "Build a data analytics portfolio",
            "Publish projects on GitHub",
            "Practice SQL and data-analysis interview questions",
            "Apply for Data Analyst and Data Science internships"
        ]
    },

    "Software_Development": {
        "foundation": [
            "Programming fundamentals",
            "Object-Oriented Programming",
            "Java or Python",
            "Data Structures and Algorithms"
        ],
        "core": [
            "Java development",
            "SQL and databases",
            "REST APIs",
            "Git and GitHub",
            "Spring Boot"
        ],
        "advanced": [
            "System design fundamentals",
            "Authentication and authorization",
            "Microservices",
            "Cloud deployment",
            "Testing and debugging"
        ],
        "projects": [
            "Student Management System",
            "Resource Booking API",
            "Full-Stack Job Recommendation Platform"
        ],
        "career": [
            "Build a strong GitHub portfolio",
            "Practice DSA regularly",
            "Prepare Java and backend interview questions",
            "Apply for Software Developer internships and entry-level roles"
        ]
    },

    "Cloud_Computing": {
        "foundation": [
            "Computer networking fundamentals",
            "Linux fundamentals",
            "Programming fundamentals",
            "Cloud computing concepts"
        ],
        "core": [
            "AWS fundamentals",
            "EC2",
            "S3",
            "IAM",
            "VPC",
            "Cloud databases"
        ],
        "advanced": [
            "Docker",
            "Kubernetes",
            "Infrastructure as Code",
            "CI/CD",
            "Cloud security",
            "Cloud architecture"
        ],
        "projects": [
            "Cloud Hosted Portfolio",
            "Cloud-Based File Storage System",
            "Cloud-Native Application Deployment"
        ],
        "career": [
            "Build AWS projects",
            "Earn relevant cloud certifications",
            "Practice Linux and networking",
            "Apply for Cloud Engineer and DevOps internships"
        ]
    },

    "Cybersecurity": {
        "foundation": [
            "Networking fundamentals",
            "Linux fundamentals",
            "Operating system fundamentals",
            "Cybersecurity basics"
        ],
        "core": [
            "Network security",
            "Authentication and authorization",
            "Cryptography fundamentals",
            "Web security",
            "Security monitoring"
        ],
        "advanced": [
            "Ethical hacking",
            "Penetration testing",
            "Digital forensics",
            "Security operations",
            "Incident response"
        ],
        "projects": [
            "Password Security Analyzer",
            "Network Monitoring Tool",
            "Security Monitoring Dashboard"
        ],
        "career": [
            "Build cybersecurity projects",
            "Practice on legal security labs",
            "Prepare networking and security interview questions",
            "Apply for Cybersecurity internships and entry-level roles"
        ]
    }
}


# ------------------------------------------------------------
# Skill Names
# ------------------------------------------------------------

SKILL_NAMES = {
    "python_skill": "Python",
    "java_skill": "Java",
    "sql_skill": "SQL",
    "programming_skill": "Programming",
    "statistics_skill": "Statistics",
    "mathematics_skill": "Mathematics",
    "linux_skill": "Linux",
    "networking_skill": "Networking",
    "cloud_skill": "Cloud Computing",
    "cybersecurity_skill": "Cybersecurity",
    "problem_solving": "Problem Solving",
    "analytical_thinking": "Analytical Thinking"
}


# ------------------------------------------------------------
# Career Skill Requirements
# ------------------------------------------------------------

CAREER_SKILLS = {

    "AI_ML": [
        "python_skill",
        "statistics_skill",
        "mathematics_skill",
        "problem_solving",
        "analytical_thinking"
    ],

    "Data_Science": [
        "python_skill",
        "sql_skill",
        "statistics_skill",
        "mathematics_skill",
        "analytical_thinking"
    ],

    "Software_Development": [
        "java_skill",
        "programming_skill",
        "problem_solving",
        "sql_skill"
    ],

    "Cloud_Computing": [
        "cloud_skill",
        "linux_skill",
        "networking_skill",
        "programming_skill"
    ],

    "Cybersecurity": [
        "cybersecurity_skill",
        "linux_skill",
        "networking_skill",
        "problem_solving"
    ]
}


# ------------------------------------------------------------
# Helper Functions
# ------------------------------------------------------------

def get_skill_level(student_data, skill):
    """Return the student's skill rating safely."""

    value = student_data.get(skill, 1)

    try:
        return int(value)
    except (ValueError, TypeError):
        return 1


def get_skill_priority(student_data, career):
    """
    Identify skills that should receive priority.

    Rating:
    1–2  -> Major improvement
    3    -> Moderate improvement
    4–5  -> Strong
    """

    skills = CAREER_SKILLS.get(career, [])

    major_gaps = []
    moderate_gaps = []
    strong_skills = []

    for skill in skills:

        level = get_skill_level(student_data, skill)
        skill_name = SKILL_NAMES.get(skill, skill)

        if level <= 2:
            major_gaps.append((skill, skill_name, level))

        elif level == 3:
            moderate_gaps.append((skill, skill_name, level))

        else:
            strong_skills.append((skill, skill_name, level))

    return major_gaps, moderate_gaps, strong_skills


def get_personalized_foundation(student_data, career):
    """
    Create a personalized foundation phase based on
    the student's weakest career-related skills.
    """

    major_gaps, moderate_gaps, strong_skills = get_skill_priority(
        student_data,
        career
    )

    foundation = []

    for _, skill_name, level in major_gaps:
        foundation.append(
            f"Improve {skill_name} fundamentals (current level: {level}/5)"
        )

    for _, skill_name, level in moderate_gaps:
        foundation.append(
            f"Strengthen {skill_name} (current level: {level}/5)"
        )

    if not foundation:
        foundation = ROADMAPS[career]["foundation"].copy()

    return foundation


def get_personalized_core(student_data, career):
    """
    Build the core learning phase while highlighting
    skills that need improvement.
    """

    major_gaps, moderate_gaps, strong_skills = get_skill_priority(
        student_data,
        career
    )

    core = []

    for _, skill_name, level in major_gaps:
        core.append(
            f"Practice {skill_name} through hands-on exercises"
        )

    for _, skill_name, level in moderate_gaps:
        core.append(
            f"Apply {skill_name} in small practical projects"
        )

    core.extend(ROADMAPS[career]["core"])

    unique_core = []

    for item in core:
        if item not in unique_core:
            unique_core.append(item)

    return unique_core


def get_personalized_projects(student_data, career):
    """
    Recommend project difficulty according to
    the student's current project experience.
    """

    number_of_projects = student_data.get("number_of_projects", 0)

    try:
        number_of_projects = int(number_of_projects)
    except (ValueError, TypeError):
        number_of_projects = 0

    projects = ROADMAPS[career]["projects"]

    if number_of_projects == 0:
        return [projects[0]]

    elif number_of_projects <= 2:
        return projects[:2]

    else:
        return projects


def get_personalized_career_preparation(student_data, career):
    """
    Add career preparation based on project and certification experience.
    """

    number_of_projects = student_data.get("number_of_projects", 0)

    number_of_certifications = student_data.get(
        "number_of_certifications",
        0
    )

    try:
        number_of_projects = int(number_of_projects)
    except (ValueError, TypeError):
        number_of_projects = 0

    try:
        number_of_certifications = int(number_of_certifications)
    except (ValueError, TypeError):
        number_of_certifications = 0

    career_items = []

    if number_of_projects < 2:
        career_items.append(
            "Build at least 2 strong portfolio projects"
        )

    if number_of_certifications == 0:
        career_items.append(
            "Consider earning a relevant beginner certification"
        )

    career_items.extend(ROADMAPS[career]["career"])

    unique_items = []

    for item in career_items:
        if item not in unique_items:
            unique_items.append(item)

    return unique_items


# ------------------------------------------------------------
# Main Roadmap Function
# ------------------------------------------------------------

def create_roadmap(career, student_data):

    if career not in ROADMAPS:
        return "\n❌ Roadmap not available for this career."

    career_name = CAREER_NAMES.get(career, career)

    foundation = get_personalized_foundation(
        student_data,
        career
    )

    core = get_personalized_core(
        student_data,
        career
    )

    advanced = ROADMAPS[career]["advanced"]

    projects = get_personalized_projects(
        student_data,
        career
    )

    career_preparation = get_personalized_career_preparation(
        student_data,
        career
    )

    major_gaps, moderate_gaps, strong_skills = get_skill_priority(
        student_data,
        career
    )

    # --------------------------------------------------------
    # Build roadmap text
    # --------------------------------------------------------

    result = []

    result.append("")
    result.append("=" * 60)
    result.append("             PERSONALIZED CAREER ROADMAP")
    result.append("=" * 60)

    result.append("")
    result.append("Recommended Career:")
    result.append(f"👉 {career_name}")

    # --------------------------------------------------------
    # PERSONALIZATION SUMMARY
    # --------------------------------------------------------

    result.append("")
    result.append("-" * 60)
    result.append("PERSONALIZATION SUMMARY")
    result.append("-" * 60)

    if major_gaps:
        result.append("")
        result.append("🔴 High-priority skills to improve:")

        for _, skill_name, level in major_gaps:
            result.append(
                f"   → {skill_name}: {level}/5"
            )

    if moderate_gaps:
        result.append("")
        result.append("🟡 Skills to strengthen:")

        for _, skill_name, level in moderate_gaps:
            result.append(
                f"   → {skill_name}: {level}/5"
            )

    if strong_skills:
        result.append("")
        result.append("🟢 Strong career-related skills:")

        for _, skill_name, level in strong_skills:
            result.append(
                f"   → {skill_name}: {level}/5"
            )

    # --------------------------------------------------------
    # PHASE 1
    # --------------------------------------------------------

    result.append("")
    result.append("-" * 60)
    result.append("PHASE 1 — PERSONALIZED FOUNDATION")
    result.append("-" * 60)

    result.append("")
    result.append("Focus first on:")

    for index, item in enumerate(foundation, start=1):
        result.append(f"   {index}. {item}")

    # --------------------------------------------------------
    # PHASE 2
    # --------------------------------------------------------

    result.append("")
    result.append("-" * 60)
    result.append("PHASE 2 — CORE SKILLS")
    result.append("-" * 60)

    result.append("")
    result.append("Develop the following skills:")

    for item in core:
        result.append(f"   → {item}")

    # --------------------------------------------------------
    # PHASE 3
    # --------------------------------------------------------

    result.append("")
    result.append("-" * 60)
    result.append("PHASE 3 — ADVANCED SKILLS")
    result.append("-" * 60)

    result.append("")
    result.append("After strengthening your foundation:")

    for item in advanced:
        result.append(f"   → {item}")

    # --------------------------------------------------------
    # PHASE 4
    # --------------------------------------------------------

    result.append("")
    result.append("-" * 60)
    result.append("PHASE 4 — RECOMMENDED PROJECTS")
    result.append("-" * 60)

    result.append("")
    result.append("Based on your current project experience:")

    for item in projects:
        result.append(f"   🚀 {item}")

    # --------------------------------------------------------
    # PHASE 5
    # --------------------------------------------------------

    result.append("")
    result.append("-" * 60)
    result.append("PHASE 5 — CAREER PREPARATION")
    result.append("-" * 60)

    result.append("")
    result.append("Recommended next steps:")

    for item in career_preparation:
        result.append(f"   → {item}")

    # --------------------------------------------------------
    # COMPLETION
    # --------------------------------------------------------

    result.append("")
    result.append("=" * 60)
    result.append("              ROADMAP COMPLETE")
    result.append("=" * 60)

    result.append("")
    result.append(
        "💡 Focus on your highest-priority skill gaps first, "
        "then gradually move toward advanced topics and projects."
    )

    result.append("=" * 60)

    return "\n".join(result)