import os
import pandas as pd


# ---------------------------------------------------
# Locate dataset
# ---------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "career_dataset.csv"
)


# ---------------------------------------------------
# Load dataset
# ---------------------------------------------------

df = pd.read_csv(DATA_PATH)


# ---------------------------------------------------
# Basic information
# ---------------------------------------------------

print("=" * 60)
print("DATASET INSPECTION")
print("=" * 60)

print("\n1. Dataset shape:")
print(df.shape)


# ---------------------------------------------------
# Columns
# ---------------------------------------------------

print("\n2. Columns:")
for column in df.columns:
    print("-", column)


# ---------------------------------------------------
# Data types
# ---------------------------------------------------

print("\n3. Data types:")
print(df.dtypes)


# ---------------------------------------------------
# Missing values
# ---------------------------------------------------

print("\n4. Missing values:")
print(df.isnull().sum())


# ---------------------------------------------------
# Duplicate rows
# ---------------------------------------------------

print("\n5. Duplicate rows:")
print(df.duplicated().sum())


# ---------------------------------------------------
# Career distribution
# ---------------------------------------------------

print("\n6. Career distribution:")
print(df["career_domain"].value_counts())


# ---------------------------------------------------
# Rating validation
# ---------------------------------------------------

rating_columns = [
    "python_skill",
    "java_skill",
    "sql_skill",
    "programming_skill",
    "statistics_skill",
    "mathematics_skill",
    "linux_skill",
    "networking_skill",
    "cloud_skill",
    "cybersecurity_skill",
    "problem_solving",
    "analytical_thinking",
    "ai_interest",
    "data_interest",
    "software_interest",
    "cloud_interest",
    "security_interest",
]


print("\n7. Rating range check:")

for column in rating_columns:

    minimum = df[column].min()
    maximum = df[column].max()

    print(
        f"{column}: min={minimum}, max={maximum}"
    )


# ---------------------------------------------------
# CGPA validation
# ---------------------------------------------------

print("\n8. CGPA range:")
print("Minimum:", df["cgpa"].min())
print("Maximum:", df["cgpa"].max())


# ---------------------------------------------------
# Projects and certifications
# ---------------------------------------------------

print("\n9. Project range:")
print(
    "Minimum:",
    df["number_of_projects"].min()
)

print(
    "Maximum:",
    df["number_of_projects"].max()
)


print("\n10. Certification range:")
print(
    "Minimum:",
    df["number_of_certifications"].min()
)

print(
    "Maximum:",
    df["number_of_certifications"].max()
)


# ---------------------------------------------------
# First records
# ---------------------------------------------------

print("\n11. First 5 records:")
print(df.head())


# ---------------------------------------------------
# Final message
# ---------------------------------------------------

print("\n" + "=" * 60)
print("DATASET INSPECTION COMPLETED")
print("=" * 60)