# ============================================================
# DATABASE SERVICE
# Intelligent Career Recommendation System
# ============================================================

from sqlalchemy.orm import Session

from src.db_models import Student, Recommendation


# ============================================================
# SAVE STUDENT + RECOMMENDATION
# ============================================================

def save_assessment(
    db: Session,
    student_data: dict,
    recommendation_data: dict,
):
    """
    Save one complete career assessment.
    """

    student = Student(
        education_level=student_data["education_level"],
        cgpa=student_data["cgpa"],
        number_of_projects=student_data[
            "number_of_projects"
        ],
        number_of_certifications=student_data[
            "number_of_certifications"
        ],

        python_skill=student_data["python_skill"],
        java_skill=student_data["java_skill"],
        sql_skill=student_data["sql_skill"],
        programming_skill=student_data[
            "programming_skill"
        ],
        statistics_skill=student_data[
            "statistics_skill"
        ],
        mathematics_skill=student_data[
            "mathematics_skill"
        ],
        linux_skill=student_data["linux_skill"],
        networking_skill=student_data[
            "networking_skill"
        ],
        cloud_skill=student_data["cloud_skill"],
        cybersecurity_skill=student_data[
            "cybersecurity_skill"
        ],
        problem_solving=student_data[
            "problem_solving"
        ],
        analytical_thinking=student_data[
            "analytical_thinking"
        ],

        ai_interest=student_data["ai_interest"],
        data_interest=student_data["data_interest"],
        software_interest=student_data[
            "software_interest"
        ],
        cloud_interest=student_data[
            "cloud_interest"
        ],
        security_interest=student_data[
            "security_interest"
        ],
    )

    db.add(student)
    db.flush()

    recommendation = Recommendation(
        student_id=student.id,
        recommended_career=recommendation_data[
            "recommended_career"
        ],
        career_code=recommendation_data[
            "career_code"
        ],
        top_match_score=recommendation_data[
            "top_match_score"
        ],
        match_scores=recommendation_data[
            "match_scores"
        ],
    )

    db.add(recommendation)

    db.commit()

    db.refresh(student)
    db.refresh(recommendation)

    return {
        "student_id": student.id,
        "recommendation_id": recommendation.id,
    }


# ============================================================
# GET STUDENT BY ID
# ============================================================

def get_student_by_id(
    db: Session,
    student_id: int,
):
    return (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )


# ============================================================
# GET RECOMMENDATION BY ID
# ============================================================

def get_recommendation_by_id(
    db: Session,
    recommendation_id: int,
):
    return (
        db.query(Recommendation)
        .filter(
            Recommendation.id
            == recommendation_id
        )
        .first()
    )


# ============================================================
# GET ASSESSMENT HISTORY
# ============================================================

def get_assessment_history(
    db: Session,
):
    """
    Return saved students together with their
    recommendations, newest first.
    """

    rows = (
        db.query(Student, Recommendation)
        .join(
            Recommendation,
            Recommendation.student_id
            == Student.id,
        )
        .order_by(
            Student.id.desc()
        )
        .all()
    )

    history = []

    for student, recommendation in rows:
        history.append(
            {
                "student_id": student.id,
                "education_level":
                    student.education_level,
                "cgpa": student.cgpa,
                "number_of_projects":
                    student.number_of_projects,
                "number_of_certifications":
                    student.number_of_certifications,

                "recommended_career":
                    recommendation.recommended_career,
                "career_code":
                    recommendation.career_code,
                "top_match_score":
                    recommendation.top_match_score,
                "match_scores":
                    recommendation.match_scores,

                "created_at":
                    student.created_at.isoformat()
                    if student.created_at
                    else None,
            }
        )

    return history