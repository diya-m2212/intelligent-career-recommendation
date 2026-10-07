# ============================================================
# CONFIGURATION FOR INTELLIGENT CAREER RECOMMENDATION SYSTEM
# ============================================================


# ------------------------------------------------------------
# CAREER DISPLAY NAMES
# ------------------------------------------------------------

CAREER_NAMES = {
    "AI_ML": "Artificial Intelligence / Machine Learning",
    "Data_Science": "Data Science",
    "Software_Development": "Software Development",
    "Cloud_Computing": "Cloud Computing",
    "Cybersecurity": "Cybersecurity",
}


# ------------------------------------------------------------
# SKILL NAMES
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
    "analytical_thinking": "Analytical Thinking",
}


# ------------------------------------------------------------
# INTEREST NAMES
# ------------------------------------------------------------

INTEREST_NAMES = {
    "ai_interest": "AI / Machine Learning",
    "data_interest": "Data Science",
    "software_interest": "Software Development",
    "cloud_interest": "Cloud Computing",
    "security_interest": "Cybersecurity",
}


# ------------------------------------------------------------
# CAREER REQUIREMENTS
# ------------------------------------------------------------

CAREER_REQUIREMENTS = {

    "AI_ML": {
        "skills": [
            "python_skill",
            "statistics_skill",
            "mathematics_skill",
            "programming_skill",
            "analytical_thinking",
            "problem_solving",
        ],
        "interests": [
            "ai_interest",
        ],
    },

    "Data_Science": {
        "skills": [
            "python_skill",
            "sql_skill",
            "statistics_skill",
            "mathematics_skill",
            "analytical_thinking",
            "programming_skill",
        ],
        "interests": [
            "data_interest",
        ],
    },

    "Software_Development": {
        "skills": [
            "java_skill",
            "python_skill",
            "programming_skill",
            "sql_skill",
            "problem_solving",
        ],
        "interests": [
            "software_interest",
        ],
    },

    "Cloud_Computing": {
        "skills": [
            "linux_skill",
            "networking_skill",
            "cloud_skill",
            "programming_skill",
            "problem_solving",
        ],
        "interests": [
            "cloud_interest",
        ],
    },

    "Cybersecurity": {
        "skills": [
            "linux_skill",
            "networking_skill",
            "cybersecurity_skill",
            "programming_skill",
            "problem_solving",
            "analytical_thinking",
        ],
        "interests": [
            "security_interest",
        ],
    },
}


# ------------------------------------------------------------
# TARGET SKILL LEVELS
# ------------------------------------------------------------
# 1 = Beginner
# 2 = Basic
# 3 = Intermediate
# 4 = Good
# 5 = Advanced
#
# These targets are used by the skill-gap and improvement
# modules.
# ------------------------------------------------------------

CAREER_TARGETS = {

    "AI_ML": {
        "python_skill": 4,
        "statistics_skill": 4,
        "mathematics_skill": 4,
        "programming_skill": 4,
        "analytical_thinking": 4,
        "problem_solving": 4,
    },

    "Data_Science": {
        "python_skill": 4,
        "sql_skill": 4,
        "statistics_skill": 4,
        "mathematics_skill": 4,
        "analytical_thinking": 4,
        "programming_skill": 4,
    },

    "Software_Development": {
        "java_skill": 4,
        "python_skill": 3,
        "programming_skill": 4,
        "sql_skill": 3,
        "problem_solving": 4,
    },

    "Cloud_Computing": {
        "linux_skill": 4,
        "networking_skill": 4,
        "cloud_skill": 4,
        "programming_skill": 4,
        "problem_solving": 4,
    },

    "Cybersecurity": {
        "linux_skill": 4,
        "networking_skill": 4,
        "cybersecurity_skill": 4,
        "programming_skill": 4,
        "problem_solving": 4,
        "analytical_thinking": 4,
    },
}