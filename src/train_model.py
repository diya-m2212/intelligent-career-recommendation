import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

import joblib


# ============================================================
# 1. PROJECT PATHS
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "career_dataset.csv"
)

MODEL_DIR = os.path.join(
    BASE_DIR,
    "models"
)

os.makedirs(MODEL_DIR, exist_ok=True)


# ============================================================
# 2. LOAD DATASET
# ============================================================

print("=" * 60)
print("CAREER RECOMMENDATION - MODEL TRAINING")
print("=" * 60)

df = pd.read_csv(DATA_PATH)

print(f"\nDataset loaded successfully.")
print(f"Total records: {len(df)}")


# ============================================================
# 3. SEPARATE INPUTS AND TARGET
# ============================================================

# student_id is only an identifier.
# It should NOT be used by the ML model.

X = df.drop(
    columns=["student_id", "career_domain"]
)

y = df["career_domain"]


print("\nInput features:")
print(list(X.columns))

print("\nTarget classes:")
print(sorted(y.unique()))


# ============================================================
# 4. DEFINE CATEGORICAL AND NUMERICAL FEATURES
# ============================================================

categorical_features = [
    "education_level"
]

numerical_features = [
    column
    for column in X.columns
    if column not in categorical_features
]


# ============================================================
# 5. PREPROCESSING
# ============================================================

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(
                handle_unknown="ignore"
            ),
            categorical_features
        ),
        (
            "numerical",
            "passthrough",
            numerical_features
        )
    ]
)


# ============================================================
# 6. TRAIN / TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


print("\nTraining records:", len(X_train))
print("Testing records:", len(X_test))


# ============================================================
# 7. DEFINE ML MODELS
# ============================================================

models = {

    "Logistic Regression": LogisticRegression(
        max_iter=2000,
        random_state=42
    ),

    "Decision Tree": DecisionTreeClassifier(
        max_depth=10,
        random_state=42
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=200,
        max_depth=12,
        random_state=42,
        n_jobs=-1
    )
}


# ============================================================
# 8. TRAIN AND EVALUATE MODELS
# ============================================================

results = {}

trained_pipelines = {}

for model_name, model in models.items():

    print("\n" + "-" * 60)
    print(f"Training: {model_name}")
    print("-" * 60)

    pipeline = Pipeline(
        steps=[
            (
                "preprocessor",
                preprocessor
            ),
            (
                "model",
                model
            )
        ]
    )

    pipeline.fit(
        X_train,
        y_train
    )

    predictions = pipeline.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    results[model_name] = accuracy

    trained_pipelines[model_name] = pipeline

    print(
        f"Accuracy: {accuracy:.4f}"
    )

    print("\nClassification Report:")

    print(
        classification_report(
            y_test,
            predictions
        )
    )


# ============================================================
# 9. COMPARE MODELS
# ============================================================

print("\n" + "=" * 60)
print("MODEL COMPARISON")
print("=" * 60)

for model_name, accuracy in results.items():

    print(
        f"{model_name:<25} "
        f"{accuracy:.4f}"
    )


# ============================================================
# 10. SELECT BEST MODEL
# ============================================================

best_model_name = max(
    results,
    key=results.get
)

best_model = trained_pipelines[
    best_model_name
]

best_accuracy = results[
    best_model_name
]


print("\n" + "=" * 60)
print("BEST MODEL")
print("=" * 60)

print(
    f"Model: {best_model_name}"
)

print(
    f"Accuracy: {best_accuracy:.4f}"
)


# ============================================================
# 11. SAVE BEST MODEL
# ============================================================

model_path = os.path.join(
    MODEL_DIR,
    "career_recommendation_model.joblib"
)

joblib.dump(
    best_model,
    model_path
)

print("\nBest model saved successfully:")
print(model_path)

print("\nTraining completed!")