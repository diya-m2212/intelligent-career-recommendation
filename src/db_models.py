# ============================================================
# DATABASE MODELS
# Intelligent Career Recommendation & Student Roadmap System
# ============================================================

from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    JSON,
    String,
)

from sqlalchemy.orm import relationship

from src.database import Base


# ============================================================
# STUDENT TABLE
# ============================================================

class Student(Base):
    __tablename__ = "students"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    # Academic information
    education_level = Column(
        String(50),
        nullable=False,
    )

    cgpa = Column(
        Float,
        nullable=False,
    )

    number_of_projects = Column(
        Integer,
        nullable=False,
        default=0,
    )

    number_of_certifications = Column(
        Integer,
        nullable=False,
        default=0,
    )

    # Technical skills
    python_skill = Column(Integer, nullable=False)
    java_skill = Column(Integer, nullable=False)
    sql_skill = Column(Integer, nullable=False)
    programming_skill = Column(Integer, nullable=False)
    statistics_skill = Column(Integer, nullable=False)
    mathematics_skill = Column(Integer, nullable=False)
    linux_skill = Column(Integer, nullable=False)
    networking_skill = Column(Integer, nullable=False)
    cloud_skill = Column(Integer, nullable=False)
    cybersecurity_skill = Column(Integer, nullable=False)
    problem_solving = Column(Integer, nullable=False)
    analytical_thinking = Column(Integer, nullable=False)

    # Career interests
    ai_interest = Column(Integer, nullable=False)
    data_interest = Column(Integer, nullable=False)
    software_interest = Column(Integer, nullable=False)
    cloud_interest = Column(Integer, nullable=False)
    security_interest = Column(Integer, nullable=False)

    # Timestamp
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    # Relationship
    recommendations = relationship(
        "Recommendation",
        back_populates="student",
        cascade="all, delete-orphan",
    )


# ============================================================
# RECOMMENDATION TABLE
# ============================================================

class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    student_id = Column(
        Integer,
        ForeignKey(
            "students.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )

    recommended_career = Column(
        String(100),
        nullable=False,
    )

    career_code = Column(
        String(50),
        nullable=False,
    )

    top_match_score = Column(
        Float,
        nullable=False,
    )

    match_scores = Column(
        JSON,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    student = relationship(
        "Student",
        back_populates="recommendations",
    )