# ============================================================
# CREATE DATABASE TABLES
# Intelligent Career Recommendation System
# ============================================================

from src.database import Base, engine
from src.db_models import Student, Recommendation


def create_tables():
    print("Creating database tables...")

    Base.metadata.create_all(
        bind=engine
    )

    print("✅ Database tables created successfully.")


if __name__ == "__main__":
    create_tables()