# ============================================================
# INTELLIGENT CAREER RECOMMENDATION SYSTEM
# Prediction + Explanation + Skill Gap + Improvements
# + Projects + Personalized Roadmap
# ============================================================

import os
import joblib
import pandas as pd

from explanation import explain_recommendation
from skill_gap import analyze_skill_gap, CAREER_TARGETS
from improvement import get_improvement_suggestions
from projects import recommend_projects
from roadmap import create_roadmap


# ------------------------------------------------------------
# Career Display Names
# ------------------------------------------------------------

CAREER_NAMES = {
    "AI_ML": "Artificial Intelligence / Machine Learning",
    "Data_Science": "Data Science",
    "Software_Development": "Software Development",
    "Cloud_Computing": "Cloud Computing",
    "Cybersecurity": "Cybersecurity"
}


# ------------------------------------------------------------
# Load Trained Model
# ------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "career_recommendation_model.joblib"
)


if not os.path.exists(MODEL_PATH):

    print("\n❌ Trained model not found.")
    print(f"Expected location: {MODEL_PATH}")
    exit()


model = joblib.load(MODEL_PATH)


# ------------------------------------------------------------
# Input Functions
# ------------------------------------------------------------

def get_rating(prompt):
    """Get a valid skill/interest rating from 1 to 5."""

    while True:

        try:

            value = int(input(prompt))

            if 1 <= value <= 5:
                return value

            print(
                "❌ Invalid input! "
                "Please enter a whole number from 1 to 5."
            )

        except ValueError:

            print(
                "❌ Invalid input! "
                "Please enter a whole number from 1 to 5."
            )


def get_cgpa():
    """Get a valid CGPA between 5.5 and 10."""

    while True:

        try:

            value = float(input("Enter CGPA (5.5 - 10): "))

            if 5.5 <= value <= 10:
                return value

            print("❌ Please enter a CGPA between 5.5 and 10.")

        except ValueError:

            print("❌ Please enter a valid numeric CGPA.")


def get_integer(prompt):
    """Get a non-negative integer."""

    while True:

        try:

            value = int(input(prompt))

            if value >= 0:
                return value

            print("❌ Please enter 0 or a positive whole number.")

        except ValueError:

            print("❌ Please enter a valid whole number.")


# ------------------------------------------------------------
# Program Start
# ------------------------------------------------------------

print("\n")
print("=" * 60)
print("      INTELLIGENT CAREER RECOMMENDATION SYSTEM")
print("=" * 60)

print("\nPlease enter the student's information.\n")


# ------------------------------------------------------------
# Education
# ------------------------------------------------------------

print("-" * 60)
print("EDUCATION INFORMATION")
print("-" * 60)

education_level = input(
    "Education Level (Graduation/Post Graduation): "
).strip()

if education_level == "":
    education_level = "Graduation"


# ------------------------------------------------------------
# Academic Information
# ------------------------------------------------------------

print("\n")
print("-" * 60)
print("ACADEMIC INFORMATION")
print("-" * 60)

cgpa = get_cgpa()


# ------------------------------------------------------------
# Technical Skills
# ------------------------------------------------------------

print("\n")
print("-" * 60)
print("TECHNICAL SKILLS")
print("-" * 60)

print("\nRate each skill from 1 to 5:")
print("1 = Beginner")
print("2 = Basic")
print("3 = Intermediate")
print("4 = Strong")
print("5 = Advanced\n")


python_skill = get_rating("Python Skill (1-5): ")
java_skill = get_rating("Java Skill (1-5): ")
sql_skill = get_rating("SQL Skill (1-5): ")
programming_skill = get_rating("Programming Skill (1-5): ")
statistics_skill = get_rating("Statistics Skill (1-5): ")
mathematics_skill = get_rating("Mathematics Skill (1-5): ")
linux_skill = get_rating("Linux Skill (1-5): ")
networking_skill = get_rating("Networking Skill (1-5): ")
cloud_skill = get_rating("Cloud Computing Skill (1-5): ")
cybersecurity_skill = get_rating("Cybersecurity Skill (1-5): ")
problem_solving = get_rating("Problem Solving (1-5): ")
analytical_thinking = get_rating("Analytical Thinking (1-5): ")


# ------------------------------------------------------------
# Career Interests
# ------------------------------------------------------------

print("\n")
print("-" * 60)
print("CAREER INTERESTS")
print("-" * 60)

print("\nRate your interest from 1 to 5:")
print("1 = Very Low")
print("2 = Low")
print("3 = Moderate")
print("4 = High")
print("5 = Very High\n")


ai_interest = get_rating("AI / ML Interest (1-5): ")
data_interest = get_rating("Data Science Interest (1-5): ")
software_interest = get_rating("Software Development Interest (1-5): ")
cloud_interest = get_rating("Cloud Computing Interest (1-5): ")
security_interest = get_rating("Cybersecurity Interest (1-5): ")


# ------------------------------------------------------------
# Experience Information
# ------------------------------------------------------------

print("\n")
print("-" * 60)
print("EXPERIENCE INFORMATION")
print("-" * 60)

number_of_projects = get_integer(
    "Number of Projects Completed: "
)

number_of_certifications = get_integer(
    "Number of Certifications: "
)


# ------------------------------------------------------------
# Build Student Data
# ------------------------------------------------------------

student_data = {

    "education_level": education_level,

    "cgpa": cgpa,

    "python_skill": python_skill,
    "java_skill": java_skill,
    "sql_skill": sql_skill,
    "programming_skill": programming_skill,
    "statistics_skill": statistics_skill,
    "mathematics_skill": mathematics_skill,
    "linux_skill": linux_skill,
    "networking_skill": networking_skill,
    "cloud_skill": cloud_skill,
    "cybersecurity_skill": cybersecurity_skill,
    "problem_solving": problem_solving,
    "analytical_thinking": analytical_thinking,

    "ai_interest": ai_interest,
    "data_interest": data_interest,
    "software_interest": software_interest,
    "cloud_interest": cloud_interest,
    "security_interest": security_interest,

    "number_of_projects": number_of_projects,
    "number_of_certifications": number_of_certifications
}


# ------------------------------------------------------------
# Create DataFrame
# ------------------------------------------------------------

student_df = pd.DataFrame([student_data])


# ------------------------------------------------------------
# Career Prediction
# ------------------------------------------------------------

predicted_career = model.predict(student_df)[0]

career_name = CAREER_NAMES.get(
    predicted_career,
    predicted_career
)


# ------------------------------------------------------------
# Prediction Result
# ------------------------------------------------------------

print("\n")
print("=" * 60)
print("              CAREER RECOMMENDATION")
print("=" * 60)

print("\nRecommended Career:")
print(f"👉 {career_name}")


# ------------------------------------------------------------
# Match Scores
# ------------------------------------------------------------

print("\n")
print("-" * 60)
print("CAREER MATCH SCORES")
print("-" * 60)

try:

    probabilities = model.predict_proba(student_df)[0]

    class_names = model.classes_

    career_scores = []

    for career, probability in zip(
        class_names,
        probabilities
    ):

        career_scores.append(
            (
                career,
                float(probability) * 100
            )
        )

    career_scores.sort(
        key=lambda x: x[1],
        reverse=True
    )

    for career, score in career_scores:

        display_name = CAREER_NAMES.get(
            career,
            career
        )

        print(
            f"   {display_name}: {score:.2f}%"
        )

except AttributeError:

    print(
        "\n⚠️ Match scores are not available "
        "for this model."
    )


# ------------------------------------------------------------
# Explanation
# ------------------------------------------------------------

print("\n")
print("=" * 60)
print("              WHY THIS CAREER?")
print("=" * 60)

explanation_result = explain_recommendation(
    predicted_career,
    student_data
)

print(explanation_result)


# ------------------------------------------------------------
# Skill Gap Analysis
# ------------------------------------------------------------

print("\n")
print("=" * 60)
print("              SKILL GAP ANALYSIS")
print("=" * 60)

skill_gap_result = analyze_skill_gap(
    predicted_career,
    student_data
)

print(skill_gap_result)


# ------------------------------------------------------------
# Improvement Suggestions
# ------------------------------------------------------------

print("\n")
print("=" * 60)
print("           IMPROVEMENT SUGGESTIONS")
print("=" * 60)

get_improvement_suggestions(
    predicted_career,
    student_data,
    CAREER_TARGETS
)


# ------------------------------------------------------------
# Project Recommendations
# ------------------------------------------------------------

print("\n")
print("=" * 60)
print("             PROJECT RECOMMENDATIONS")
print("=" * 60)

project_result = recommend_projects(
    predicted_career,
    student_data
)

print(project_result)


# ------------------------------------------------------------
# Personalized Career Roadmap
# ------------------------------------------------------------

# create_roadmap() already prints its own complete heading.
# Therefore, we do not print another heading here.

create_roadmap(
    predicted_career,
    student_data
)


# ------------------------------------------------------------
# Completion Message
# ------------------------------------------------------------

print("\n")
print("=" * 60)
print("       PREDICTION COMPLETED SUCCESSFULLY!")
print("=" * 60)

print(
    "\n🎯 The system analyzed the student's "
    "skills, interests, experience, and academic profile."
)

print(
    "💡 The recommendation, skill gaps, improvements, "
    "projects, and roadmap were generated successfully."
)

print("\n")