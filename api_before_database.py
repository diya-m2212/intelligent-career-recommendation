from typing import Dict

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from src.config import CAREER_NAMES
from src.explanation import explain_recommendation
from src.skill_gap import analyze_skill_gap
from src.improvement import suggest_improvements
from src.projects import recommend_projects
from src.roadmap import create_roadmap


app = FastAPI(
    title="Intelligent Career Recommendation System",
    description=(
        "ML-powered career recommendation API for students. "
        "The system analyzes academic performance, technical skills, "
        "interests, projects, and certifications."
    ),
    version="1.0.0",
)


# ============================================================
# CORS CONFIGURATION
# Allows the React frontend to communicate with FastAPI.
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# LOAD MACHINE LEARNING MODEL
# ============================================================

MODEL_PATH = "models/career_recommendation_model.joblib"

try:
    model = joblib.load(MODEL_PATH)
    print("ML model loaded successfully.")
except Exception as e:
    model = None
    print(f"WARNING: Could not load model: {e}")


# ============================================================
# STUDENT INPUT MODEL
# ============================================================

class StudentProfile(BaseModel):
    education_level: str = Field(
        ...,
        description="Education level, for example Graduation or Post Graduation",
    )

    cgpa: float = Field(..., ge=5.5, le=10.0)

    python_skill: int = Field(..., ge=1, le=5)
    java_skill: int = Field(..., ge=1, le=5)
    sql_skill: int = Field(..., ge=1, le=5)
    programming_skill: int = Field(..., ge=1, le=5)

    statistics_skill: int = Field(..., ge=1, le=5)
    mathematics_skill: int = Field(..., ge=1, le=5)

    linux_skill: int = Field(..., ge=1, le=5)
    networking_skill: int = Field(..., ge=1, le=5)
    cloud_skill: int = Field(..., ge=1, le=5)
    cybersecurity_skill: int = Field(..., ge=1, le=5)

    problem_solving: int = Field(..., ge=1, le=5)
    analytical_thinking: int = Field(..., ge=1, le=5)

    ai_interest: int = Field(..., ge=1, le=5)
    data_interest: int = Field(..., ge=1, le=5)
    software_interest: int = Field(..., ge=1, le=5)
    cloud_interest: int = Field(..., ge=1, le=5)
    security_interest: int = Field(..., ge=1, le=5)

    number_of_projects: int = Field(..., ge=0)
    number_of_certifications: int = Field(..., ge=0)


# ============================================================
# MATCH SCORE CALCULATION
# ============================================================

def get_match_scores(student_data: Dict) -> Dict[str, float]:
    input_data = pd.DataFrame([student_data])

    probabilities = model.predict_proba(input_data)[0]
    classes = model.classes_

    scores = {}

    for career, probability in zip(classes, probabilities):
        display_name = CAREER_NAMES.get(career, career)

        scores[display_name] = round(
            float(probability) * 100,
            2
        )

    return dict(
        sorted(
            scores.items(),
            key=lambda item: item[1],
            reverse=True
        )
    )


# ============================================================
# TEXT CLEANING
# ============================================================

def clean_text(text):
    if text is None:
        return ""

    return str(text)


# ============================================================
# ROOT ENDPOINT
# ============================================================

@app.get("/")
def root():
    return {
        "message": "Intelligent Career Recommendation API is running!",
        "docs": "/docs",
        "version": "1.0.0",
    }


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_loaded": model is not None,
    }


# ============================================================
# CAREER LIST
# ============================================================

@app.get("/api/careers")
def get_careers():
    return {
        "careers": list(CAREER_NAMES.values())
    }


# ============================================================
# CAREER RECOMMENDATION
# ============================================================

@app.post("/api/recommend")
def recommend_career(student: StudentProfile):

    if model is None:
        raise HTTPException(
            status_code=500,
            detail="ML model could not be loaded.",
        )

    # Convert Pydantic object into dictionary
    student_data = student.model_dump()

    # Convert student data into DataFrame
    input_data = pd.DataFrame([student_data])

    # --------------------------------------------------------
    # ML PREDICTION
    # --------------------------------------------------------

    prediction = model.predict(input_data)[0]

    predicted_career = str(prediction)

    career_display_name = CAREER_NAMES.get(
        predicted_career,
        predicted_career
    )

    # --------------------------------------------------------
    # MATCH SCORES
    # --------------------------------------------------------

    match_scores = get_match_scores(student_data)

    # --------------------------------------------------------
    # EXPLANATION
    # --------------------------------------------------------

    explanation = explain_recommendation(
        predicted_career,
        student_data
    )

    # --------------------------------------------------------
    # SKILL GAP
    # --------------------------------------------------------

    skill_gap = analyze_skill_gap(
        predicted_career,
        student_data
    )

    # --------------------------------------------------------
    # IMPROVEMENT SUGGESTIONS
    # --------------------------------------------------------

    improvements = suggest_improvements(
        predicted_career,
        student_data
    )

    # --------------------------------------------------------
    # PROJECT RECOMMENDATIONS
    # --------------------------------------------------------

    projects = recommend_projects(
        predicted_career,
        student_data
    )

    # --------------------------------------------------------
    # PERSONALIZED ROADMAP
    # --------------------------------------------------------

    roadmap = create_roadmap(
        predicted_career,
        student_data
    )

    # --------------------------------------------------------
    # FINAL RESPONSE
    # --------------------------------------------------------

    return {
        "success": True,

        "recommended_career": career_display_name,

        "career_code": predicted_career,

        "match_scores": match_scores,

        "why_this_career": clean_text(
            explanation
        ),

        "skill_gap_analysis": clean_text(
            skill_gap
        ),

        "improvement_suggestions": clean_text(
            improvements
        ),

        "recommended_projects": clean_text(
            projects
        ),

        "personalized_roadmap": clean_text(
            roadmap
        ),
    }