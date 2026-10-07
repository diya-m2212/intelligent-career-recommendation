import os
import numpy as np
import pandas as pd

# Make results reproducible
np.random.seed(42)

# ---------------------------------------------------
# Project paths
# ---------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)

# ---------------------------------------------------
# Career domains
# ---------------------------------------------------

CAREER_PROFILES = {
    "AI_ML": {
        "python_skill": 4.5,
        "java_skill": 2.5,
        "sql_skill": 3.5,
        "programming_skill": 4.5,
        "statistics_skill": 4.5,
        "mathematics_skill": 4.5,
        "linux_skill": 3.0,
        "networking_skill": 2.0,
        "cloud_skill": 2.5,
        "cybersecurity_skill": 1.5,
        "problem_solving": 4.5,
        "analytical_thinking": 4.5,
        "ai_interest": 5.0,
        "data_interest": 4.5,
        "software_interest": 3.5,
        "cloud_interest": 2.5,
        "security_interest": 1.5,
    },

    "Data_Science": {
        "python_skill": 4.0,
        "java_skill": 2.0,
        "sql_skill": 4.5,
        "programming_skill": 3.5,
        "statistics_skill": 5.0,
        "mathematics_skill": 4.5,
        "linux_skill": 2.5,
        "networking_skill": 1.5,
        "cloud_skill": 2.5,
        "cybersecurity_skill": 1.5,
        "problem_solving": 4.5,
        "analytical_thinking": 5.0,
        "ai_interest": 4.0,
        "data_interest": 5.0,
        "software_interest": 2.5,
        "cloud_interest": 2.0,
        "security_interest": 1.5,
    },

    "Software_Development": {
        "python_skill": 3.5,
        "java_skill": 4.5,
        "sql_skill": 4.0,
        "programming_skill": 5.0,
        "statistics_skill": 2.5,
        "mathematics_skill": 3.0,
        "linux_skill": 3.5,
        "networking_skill": 2.5,
        "cloud_skill": 3.0,
        "cybersecurity_skill": 2.0,
        "problem_solving": 5.0,
        "analytical_thinking": 4.0,
        "ai_interest": 2.5,
        "data_interest": 3.0,
        "software_interest": 5.0,
        "cloud_interest": 3.5,
        "security_interest": 2.0,
    },

    "Cloud_Computing": {
        "python_skill": 3.0,
        "java_skill": 2.5,
        "sql_skill": 3.0,
        "programming_skill": 3.5,
        "statistics_skill": 2.0,
        "mathematics_skill": 2.5,
        "linux_skill": 4.5,
        "networking_skill": 5.0,
        "cloud_skill": 5.0,
        "cybersecurity_skill": 3.5,
        "problem_solving": 4.0,
        "analytical_thinking": 4.0,
        "ai_interest": 1.5,
        "data_interest": 2.0,
        "software_interest": 3.0,
        "cloud_interest": 5.0,
        "security_interest": 3.5,
    },

    "Cybersecurity": {
        "python_skill": 3.0,
        "java_skill": 2.0,
        "sql_skill": 3.0,
        "programming_skill": 3.5,
        "statistics_skill": 2.0,
        "mathematics_skill": 2.5,
        "linux_skill": 4.5,
        "networking_skill": 5.0,
        "cloud_skill": 3.5,
        "cybersecurity_skill": 5.0,
        "problem_solving": 4.5,
        "analytical_thinking": 4.5,
        "ai_interest": 1.5,
        "data_interest": 2.0,
        "software_interest": 2.5,
        "cloud_interest": 3.5,
        "security_interest": 5.0,
    },
}

# ---------------------------------------------------
# Generate student records
# ---------------------------------------------------

records = []

students_per_career = 200

for career, profile in CAREER_PROFILES.items():

    for _ in range(students_per_career):

        # Education level
        education_level = np.random.choice(
            ["Graduation", "Post-Graduation"],
            p=[0.55, 0.45]
        )

        # Academic performance
        cgpa = np.clip(
            np.random.normal(7.8, 0.9),
            5.5,
            10.0
        )

        row = {
            "education_level": education_level,
            "cgpa": round(cgpa, 2)
        }

        # Generate skill and interest ratings
        for feature, average in profile.items():

            value = np.random.normal(average, 0.75)

            value = np.clip(value, 1, 5)

            row[feature] = round(value, 1)

        # Practical experience
        number_of_projects = int(
            np.clip(
                np.random.poisson(2.5),
                0,
                8
            )
        )

        number_of_certifications = int(
            np.clip(
                np.random.poisson(1.5),
                0,
                6
            )
        )

        row["number_of_projects"] = number_of_projects
        row["number_of_certifications"] = number_of_certifications

        # Target
        row["career_domain"] = career

        records.append(row)


# ---------------------------------------------------
# Create DataFrame
# ---------------------------------------------------

df = pd.DataFrame(records)

# Shuffle the dataset
df = df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

# Add student ID
df.insert(
    0,
    "student_id",
    range(1, len(df) + 1)
)

# ---------------------------------------------------
# Save dataset
# ---------------------------------------------------

output_path = os.path.join(
    DATA_DIR,
    "career_dataset.csv"
)

df.to_csv(
    output_path,
    index=False
)

# ---------------------------------------------------
# Display information
# ---------------------------------------------------

print("=" * 60)
print("CAREER RECOMMENDATION DATASET GENERATED")
print("=" * 60)

print(f"\nTotal students: {len(df)}")

print("\nCareer distribution:")
print(df["career_domain"].value_counts())

print("\nDataset shape:")
print(df.shape)

print("\nFirst 5 records:")
print(df.head())

print(f"\nDataset saved successfully at:")
print(output_path)

print("\nDone!")