# skill_gap.py
# Analyzes the student's skill gaps
# for the recommended career.


CAREER_TARGETS = {

    "AI_ML": {
        "python_skill": 4,
        "statistics_skill": 4,
        "mathematics_skill": 4,
        "problem_solving": 4,
        "analytical_thinking": 4
    },

    "Data_Science": {
        "python_skill": 4,
        "sql_skill": 4,
        "statistics_skill": 4,
        "mathematics_skill": 4,
        "analytical_thinking": 4
    },

    "Software_Development": {
        "java_skill": 4,
        "programming_skill": 4,
        "problem_solving": 4,
        "sql_skill": 4
    },

    "Cloud_Computing": {
        "cloud_skill": 4,
        "linux_skill": 4,
        "networking_skill": 4,
        "programming_skill": 4
    },

    "Cybersecurity": {
        "cybersecurity_skill": 4,
        "linux_skill": 4,
        "networking_skill": 4,
        "problem_solving": 4
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


def analyze_skill_gap(career, student_data):

    if career not in CAREER_TARGETS:
        return "No skill gap information available."

    targets = CAREER_TARGETS[career]

    strong_skills = []
    moderate_gaps = []
    major_gaps = []

    for skill, target in targets.items():

        current = student_data.get(skill, 0)

        gap = target - current

        if gap <= 0:
            strong_skills.append(
                (skill, current, target, gap)
            )

        elif gap == 1:
            moderate_gaps.append(
                (skill, current, target, gap)
            )

        else:
            major_gaps.append(
                (skill, current, target, gap)
            )

    explanation = []

    explanation.append("\n")
    explanation.append("=" * 60)
    explanation.append("                 SKILL GAP ANALYSIS")
    explanation.append("=" * 60)

    explanation.append(
        f"\nRecommended Career: "
        f"{career.replace('_', ' ')}"
    )

    if strong_skills:

        explanation.append("\n🟢 STRONG SKILLS:")

        for skill, current, target, gap in strong_skills:

            explanation.append(
                f"   • {SKILL_NAMES[skill]}: "
                f"{current}/5 "
                f"(Target: {target}/5)"
            )

    if moderate_gaps:

        explanation.append("\n🟡 MODERATE GAPS:")

        for skill, current, target, gap in moderate_gaps:

            explanation.append(
                f"   • {SKILL_NAMES[skill]}: "
                f"{current}/5 → Target {target}/5 "
                f"(Gap: {gap})"
            )

    if major_gaps:

        explanation.append("\n🔴 MAJOR GAPS:")

        for skill, current, target, gap in major_gaps:

            explanation.append(
                f"   • {SKILL_NAMES[skill]}: "
                f"{current}/5 → Target {target}/5 "
                f"(Gap: {gap})"
            )

    explanation.append("\n💡 PRIORITY:")

    if major_gaps:

        explanation.append(
            "   Focus first on your major skill gaps."
        )

        for skill, current, target, gap in major_gaps:

            explanation.append(
                f"   → Improve {SKILL_NAMES[skill]}"
            )

    elif moderate_gaps:

        explanation.append(
            "   You have a good foundation. "
            "Focus on your moderate gaps."
        )

        for skill, current, target, gap in moderate_gaps:

            explanation.append(
                f"   → Improve {SKILL_NAMES[skill]}"
            )

    else:

        explanation.append(
            "   🎉 You currently meet or exceed "
            "the target level for all core skills."
        )

    return "\n".join(explanation)