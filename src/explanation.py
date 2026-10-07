# ============================================================
# CAREER RECOMMENDATION EXPLANATION
# ============================================================

CAREER_NAMES = {
    "AI_ML": "Artificial Intelligence / Machine Learning",
    "Data_Science": "Data Science",
    "Software_Development": "Software Development",
    "Cloud_Computing": "Cloud Computing",
    "Cybersecurity": "Cybersecurity"
}


CAREER_REQUIREMENTS = {

    "AI_ML": {
        "skills": [
            "python_skill",
            "statistics_skill",
            "mathematics_skill",
            "problem_solving",
            "analytical_thinking"
        ],
        "interests": [
            "ai_interest",
            "data_interest"
        ]
    },

    "Data_Science": {
        "skills": [
            "python_skill",
            "sql_skill",
            "statistics_skill",
            "mathematics_skill",
            "analytical_thinking"
        ],
        "interests": [
            "data_interest",
            "ai_interest"
        ]
    },

    "Software_Development": {
        "skills": [
            "java_skill",
            "programming_skill",
            "problem_solving",
            "sql_skill"
        ],
        "interests": [
            "software_interest"
        ]
    },

    "Cloud_Computing": {
        "skills": [
            "cloud_skill",
            "linux_skill",
            "networking_skill",
            "programming_skill"
        ],
        "interests": [
            "cloud_interest",
            "software_interest"
        ]
    },

    "Cybersecurity": {
        "skills": [
            "cybersecurity_skill",
            "linux_skill",
            "networking_skill",
            "problem_solving"
        ],
        "interests": [
            "security_interest"
        ]
    }
}


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


INTEREST_NAMES = {
    "ai_interest": "AI / ML",
    "data_interest": "Data Science",
    "software_interest": "Software Development",
    "cloud_interest": "Cloud Computing",
    "security_interest": "Cybersecurity"
}


def explain_recommendation(career, student_data):

    career_name = CAREER_NAMES.get(career, career)

    requirements = CAREER_REQUIREMENTS.get(career)

    if not requirements:
        return "❌ Explanation is not available for this career."

    lines = []

    lines.append(f"Recommended career: {career_name}")
    lines.append("")
    lines.append(
        "The recommendation is based on the student's "
        "skills, interests and the ML model prediction."
    )

    # --------------------------------------------------------
    # Strong Skills
    # --------------------------------------------------------

    strong_skills = []

    for skill in requirements["skills"]:

        value = student_data.get(skill, 1)

        try:
            value = int(value)
        except (ValueError, TypeError):
            value = 1

        if value >= 4:
            strong_skills.append(
                f"{SKILL_NAMES.get(skill, skill)} "
                f"({value}/5)"
            )

    if strong_skills:

        lines.append("")
        lines.append("💪 Strong matching skills:")

        for skill in strong_skills:
            lines.append(f"   → {skill}")

    # --------------------------------------------------------
    # Moderate Skills
    # --------------------------------------------------------

    moderate_skills = []

    for skill in requirements["skills"]:

        value = student_data.get(skill, 1)

        try:
            value = int(value)
        except (ValueError, TypeError):
            value = 1

        if value == 3:
            moderate_skills.append(
                f"{SKILL_NAMES.get(skill, skill)} (3/5)"
            )

    if moderate_skills:

        lines.append("")
        lines.append("🟡 Skills that can be strengthened:")

        for skill in moderate_skills:
            lines.append(f"   → {skill}")

    # --------------------------------------------------------
    # Weak Skills
    # --------------------------------------------------------

    weak_skills = []

    for skill in requirements["skills"]:

        value = student_data.get(skill, 1)

        try:
            value = int(value)
        except (ValueError, TypeError):
            value = 1

        if value <= 2:
            weak_skills.append(
                f"{SKILL_NAMES.get(skill, skill)} ({value}/5)"
            )

    if weak_skills:

        lines.append("")
        lines.append("🔴 Skills requiring improvement:")

        for skill in weak_skills:
            lines.append(f"   → {skill}")

    # --------------------------------------------------------
    # Interests
    # --------------------------------------------------------

    interests = []

    for interest in requirements["interests"]:

        value = student_data.get(interest, 1)

        try:
            value = int(value)
        except (ValueError, TypeError):
            value = 1

        if value >= 4:
            interests.append(
                f"{INTEREST_NAMES.get(interest, interest)} "
                f"({value}/5)"
            )

    if interests:

        lines.append("")
        lines.append("❤️ Relevant career interests:")

        for interest in interests:
            lines.append(f"   → {interest}")

    # --------------------------------------------------------
    # Final Interpretation
    # --------------------------------------------------------

    lines.append("")
    lines.append(
        f"💡 The ML model selected {career_name} because "
        "it received the highest predicted match among "
        "the available career domains."
    )

    return "\n".join(lines)


if __name__ == "__main__":

    print("Career explanation module loaded successfully.")