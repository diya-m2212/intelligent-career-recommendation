# ============================================================
# INTELLIGENT CAREER RECOMMENDATION API
# FastAPI + Machine Learning + PostgreSQL
# ============================================================

from pathlib import Path
from typing import Dict

import joblib
import pandas as pd

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from src.database import get_db
from src.db_service import (
    save_assessment,
    get_assessment_history,
)
from src.explanation import explain_recommendation
from src.improvement import suggest_improvements
from src.projects import recommend_projects
from src.roadmap import create_roadmap
from src.skill_gap import analyze_skill_gap
from src.config import CAREER_NAMES


# ============================================================
# PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent

MODEL_PATH = (
    PROJECT_ROOT
    / "models"
    / "career_recommendation_model.joblib"
)


# ============================================================
# FASTAPI APP
# ============================================================

app = FastAPI(
    title="Intelligent Career Recommendation API",
    description=(
        "Machine-learning based career recommendation "
        "and personalized student roadmap system."
    ),
    version="1.0.0",
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# LOAD ML MODEL
# ============================================================

try:
    model = joblib.load(MODEL_PATH)
    print("✅ ML model loaded successfully.")

except Exception as error:
    model = None
    print("❌ Failed to load ML model.")
    print(f"Reason: {error}")


# ============================================================
# STUDENT INPUT MODEL
# ============================================================

class StudentProfile(BaseModel):
    education_level: str = Field(
        ...,
        description="Graduation or Post Graduation",
    )

    cgpa: float = Field(
        ...,
        ge=5.5,
        le=10.0,
    )

    python_skill: int = Field(
        ...,
        ge=1,
        le=5,
    )

    java_skill: int = Field(
        ...,
        ge=1,
        le=5,
    )

    sql_skill: int = Field(
        ...,
        ge=1,
        le=5,
    )

    programming_skill: int = Field(
        ...,
        ge=1,
        le=5,
    )

    statistics_skill: int = Field(
        ...,
        ge=1,
        le=5,
    )

    mathematics_skill: int = Field(
        ...,
        ge=1,
        le=5,
    )

    linux_skill: int = Field(
        ...,
        ge=1,
        le=5,
    )

    networking_skill: int = Field(
        ...,
        ge=1,
        le=5,
    )

    cloud_skill: int = Field(
        ...,
        ge=1,
        le=5,
    )

    cybersecurity_skill: int = Field(
        ...,
        ge=1,
        le=5,
    )

    problem_solving: int = Field(
        ...,
        ge=1,
        le=5,
    )

    analytical_thinking: int = Field(
        ...,
        ge=1,
        le=5,
    )

    ai_interest: int = Field(
        ...,
        ge=1,
        le=5,
    )

    data_interest: int = Field(
        ...,
        ge=1,
        le=5,
    )

    software_interest: int = Field(
        ...,
        ge=1,
        le=5,
    )

    cloud_interest: int = Field(
        ...,
        ge=1,
        le=5,
    )

    security_interest: int = Field(
        ...,
        ge=1,
        le=5,
    )

    number_of_projects: int = Field(
        ...,
        ge=0,
    )

    number_of_certifications: int = Field(
        ...,
        ge=0,
    )


# ============================================================
# HELPERS
# ============================================================

def clean_text(value) -> str:
    """
    Convert helper-module output into clean text.
    """

    if value is None:
        return ""

    return str(value).strip()


def get_match_scores(student_data: Dict) -> Dict[str, float]:
    """
    Get ML probability scores for every career.
    """

    if model is None:
        raise RuntimeError(
            "ML model is not available."
        )

    input_df = pd.DataFrame([student_data])

    probabilities = model.predict_proba(
        input_df
    )[0]

    classes = model.classes_

    scores = {}

    for career_code, probability in zip(
        classes,
        probabilities,
    ):
        career_name = CAREER_NAMES.get(
            str(career_code),
            str(career_code),
        )

        scores[career_name] = round(
            float(probability) * 100,
            2,
        )

    return dict(
        sorted(
            scores.items(),
            key=lambda item: item[1],
            reverse=True,
        )
    )


# ============================================================
# ROOT ENDPOINT
# ============================================================

@app.get("/")
def root():
    return {
        "message": (
            "Intelligent Career Recommendation "
            "API is running!"
        ),
        "docs": "/docs",
        "version": "1.0.0",
    }


# ============================================================
# HEALTH ENDPOINT
# ============================================================

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "database": "connected through SQLAlchemy",
    }


# ============================================================
# CAREERS ENDPOINT
# ============================================================

# ============================================================
# ASSESSMENT HISTORY ENDPOINT
# ============================================================

@app.get("/api/assessments")
def get_assessments(
    db: Session = Depends(get_db),
):
    """
    Return all saved student assessments
    and their recommendations.
    """

    try:
        history = get_assessment_history(db)

        return {
            "total_assessments": len(history),
            "assessments": history,
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=(
                "Could not load assessment history: "
                f"{error}"
            ),
        )

# ============================================================
# RECOMMENDATION ENDPOINT
# ============================================================

@app.post("/api/recommend")
def recommend_career(
    profile: StudentProfile,
    db: Session = Depends(get_db),
):
    if model is None:
        raise HTTPException(
            status_code=500,
            detail="ML model is not loaded.",
        )

    # --------------------------------------------------------
    # Convert Pydantic object to dictionary
    # --------------------------------------------------------

    student_data = profile.model_dump()

    # --------------------------------------------------------
    # ML prediction
    # --------------------------------------------------------

    try:
        prediction = model.predict(
            pd.DataFrame([student_data])
        )[0]

        career_code = str(prediction)

        recommended_career = CAREER_NAMES.get(
            career_code,
            career_code,
        )

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {error}",
        )

    # --------------------------------------------------------
    # Career match scores
    # --------------------------------------------------------

    try:
        match_scores = get_match_scores(
            student_data
        )

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=(
                "Could not calculate match scores: "
                f"{error}"
            ),
        )

    # --------------------------------------------------------
    # Top score
    # --------------------------------------------------------

    top_match_score = round(
        max(match_scores.values()),
        2,
    )

    # --------------------------------------------------------
    # Explanations
    # --------------------------------------------------------

    try:
        why_this_career = clean_text(
            explain_recommendation(
                career_code,
                student_data,
            )
        )

        skill_gap_analysis = clean_text(
            analyze_skill_gap(
                career_code,
                student_data,
            )
        )

        improvement_suggestions = clean_text(
            suggest_improvements(
                career_code,
                student_data,
            )
        )

        recommended_projects = clean_text(
            recommend_projects(
                career_code,
                student_data,
            )
        )

        personalized_roadmap = clean_text(
            create_roadmap(
                career_code,
                student_data,
            )
        )

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=(
                "Failed to generate career guidance: "
                f"{error}"
            ),
        )

    # --------------------------------------------------------
    # Save assessment to PostgreSQL
    # --------------------------------------------------------

    try:
        database_result = save_assessment(
            db=db,
            student_data=student_data,
            recommendation_data={
                "recommended_career":
                    recommended_career,

                "career_code":
                    career_code,

                "top_match_score":
                    top_match_score,

                "match_scores":
                    match_scores,
            },
        )

    except Exception as error:
        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=(
                "Recommendation was generated, "
                "but saving to PostgreSQL failed: "
                f"{error}"
            ),
        )

    # --------------------------------------------------------
    # Final API response
    # --------------------------------------------------------

    return {
        "student_id":
            database_result["student_id"],

        "recommendation_id":
            database_result["recommendation_id"],

        "recommended_career":
            recommended_career,

        "career_code":
            career_code,

        "match_scores":
            match_scores,

        "top_match_score":
            top_match_score,

        "why_this_career":
            why_this_career,

        "skill_gap_analysis":
            skill_gap_analysis,

        "improvement_suggestions":
            improvement_suggestions,

        "recommended_projects":
            recommended_projects,

        "personalized_roadmap":
            personalized_roadmap,
    }