# ============================================================
# CAREER IMPROVEMENT SUGGESTIONS
# ============================================================

from src.config import CAREER_TARGETS


# ------------------------------------------------------------
# Skill Display Names
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
# Improvement Suggestions
# ------------------------------------------------------------

IMPROVEMENT_SUGGESTIONS = {

    "python_skill": [
        "Practice Python fundamentals and object-oriented programming.",
        "Build small Python automation projects.",
        "Practice NumPy and Pandas.",
        "Solve Python programming problems regularly.",
    ],

    "java_skill": [
        "Strengthen Java OOP concepts.",
        "Practice collections, exceptions and file handling.",
        "Learn Java Streams and modern Java features.",
        "Build backend applications using Spring Boot.",
    ],

    "sql_skill": [
        "Practice SELECT, WHERE, GROUP BY and JOIN queries.",
        "Learn subqueries and aggregate functions.",
        "Practice database design and normalization.",
        "Build projects using PostgreSQL or MySQL.",
    ],

    "programming_skill": [
        "Strengthen programming fundamentals.",
        "Practice functions, loops, conditions and data structures.",
        "Solve DSA problems regularly.",
        "Build small applications to improve coding confidence.",
    ],

    "statistics_skill": [
        "Revise mean, median, variance and standard deviation.",
        "Learn probability fundamentals.",
        "Practice statistical analysis using Python.",
        "Study hypothesis testing and correlation.",
    ],

    "mathematics_skill": [
        "Strengthen algebra and mathematical fundamentals.",
        "Study linear algebra basics.",
        "Learn probability concepts.",
        "Practice mathematics used in Machine Learning.",
    ],

    "linux_skill": [
        "Learn Linux commands and file-system navigation.",
        "Practice permissions and process management.",
        "Learn shell scripting basics.",
        "Use Linux regularly for development.",
    ],

    "networking_skill": [
        "Learn TCP/IP fundamentals.",
        "Study IP addressing and subnetting.",
        "Understand DNS, HTTP and HTTPS.",
        "Practice networking using tools such as ping and traceroute.",
    ],

    "cloud_skill": [
        "Learn cloud computing fundamentals.",
        "Start with AWS core services.",
        "Practice EC2, S3 and IAM.",
        "Learn VPC and basic cloud architecture.",
        "Deploy a small application to the cloud.",
    ],

    "cybersecurity_skill": [
        "Learn cybersecurity fundamentals.",
        "Study authentication and authorization.",
        "Learn common web security vulnerabilities.",
        "Practice cybersecurity in legal lab environments.",
        "Study basic cryptography and network security.",
    ],

    "problem_solving": [
        "Solve programming problems regularly.",
        "Practice breaking large problems into smaller tasks.",
        "Work on algorithm and DSA problems.",
        "Build projects that require logical decision-making.",
    ],

    "analytical_thinking": [
        "Practice analyzing datasets and technical problems.",
        "Break complex problems into smaller components.",
        "Compare multiple solutions before choosing one.",
        "Work on case studies and analytical projects.",
    ],
}


# ------------------------------------------------------------
# Main Function
# ------------------------------------------------------------

def suggest_improvements(career, student_data):
    """
    Generate career improvement suggestions based on
    the student's skill gaps.

    Returns:
        String containing improvement suggestions.
    """

    # --------------------------------------------------------
    # Get target skills for selected career
    # --------------------------------------------------------

    if career not in CAREER_TARGETS:
        return "❌ Career targets not found."

    targets = CAREER_TARGETS[career]

    # --------------------------------------------------------
    # Calculate skill gaps
    # --------------------------------------------------------

    gaps = []

    for skill, target_level in targets.items():

        current_level = student_data.get(skill, 1)

        try:
            current_level = int(current_level)
        except (ValueError, TypeError):
            current_level = 1

        try:
            target_level = int(target_level)
        except (ValueError, TypeError):
            continue

        gap = target_level - current_level

        if gap > 0:
            gaps.append(
                (
                    skill,
                    current_level,
                    target_level,
                    gap,
                )
            )

    # --------------------------------------------------------
    # Build output
    # --------------------------------------------------------

    result = []

    # --------------------------------------------------------
    # No improvement gaps
    # --------------------------------------------------------

    if not gaps:

        result.append("🎉 Excellent!")

        result.append(
            "You currently meet or exceed the target "
            "skill levels for your recommended career."
        )

        result.append("")
        result.append("Recommended next steps:")

        result.append(
            "   → Build advanced projects"
        )

        result.append(
            "   → Gain practical industry experience"
        )

        result.append(
            "   → Participate in internships or competitions"
        )

        result.append(
            "   → Prepare for technical interviews"
        )

        return "\n".join(result)

    # --------------------------------------------------------
    # Sort by largest gap
    # --------------------------------------------------------

    gaps.sort(
        key=lambda item: item[3],
        reverse=True
    )

    result.append("Focus on the following areas:")
    result.append("")

    # --------------------------------------------------------
    # Display Suggestions
    # --------------------------------------------------------

    for skill, current_level, target_level, gap in gaps:

        skill_name = SKILL_NAMES.get(
            skill,
            skill
        )

        if gap >= 2:
            priority = "HIGH PRIORITY"
        else:
            priority = "MEDIUM PRIORITY"

        result.append(
            f"🔹 {skill_name} "
            f"({current_level}/5 → {target_level}/5)"
        )

        result.append(
            f"   Priority: {priority}"
        )

        suggestions = IMPROVEMENT_SUGGESTIONS.get(
            skill,
            [
                f"Practice {skill_name} through "
                "hands-on exercises and projects."
            ]
        )

        for suggestion in suggestions:
            result.append(
                f"   → {suggestion}"
            )

        result.append("")

    return "\n".join(result)


# ------------------------------------------------------------
# Backward Compatibility
# ------------------------------------------------------------

def get_improvement_suggestions(
    career,
    student_data,
    career_targets=None
):
    """
    Compatibility wrapper for the older function name.

    The current system uses suggest_improvements().
    """

    return suggest_improvements(
        career,
        student_data
    )


# ------------------------------------------------------------
# Standalone Test
# ------------------------------------------------------------

if __name__ == "__main__":

    print("=" * 60)
    print("CAREER IMPROVEMENT MODULE")
    print("=" * 60)

    sample_student = {
        "python_skill": 2,
        "java_skill": 3,
        "sql_skill": 2,
        "programming_skill": 3,
        "statistics_skill": 2,
        "mathematics_skill": 2,
        "linux_skill": 2,
        "networking_skill": 2,
        "cloud_skill": 2,
        "cybersecurity_skill": 2,
        "problem_solving": 3,
        "analytical_thinking": 3,
    }

    print(
        suggest_improvements(
            "Cloud_Computing",
            sample_student
        )
    )