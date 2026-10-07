# ============================================================
# DATABASE CONNECTION
# Intelligent Career Recommendation System
# ============================================================

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base


# ------------------------------------------------------------
# Load environment variables
# ------------------------------------------------------------

load_dotenv()


# ------------------------------------------------------------
# Database configuration
# ------------------------------------------------------------

DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST", "127.0.0.1")
DATABASE_PORT = os.getenv("DATABASE_PORT", "5433")
DATABASE_NAME = os.getenv(
    "DATABASE_NAME",
    "career_recommendation",
)


# ------------------------------------------------------------
# Check required configuration
# ------------------------------------------------------------

required_settings = {
    "DATABASE_USER": DATABASE_USER,
    "DATABASE_PASSWORD": DATABASE_PASSWORD,
    "DATABASE_HOST": DATABASE_HOST,
    "DATABASE_PORT": DATABASE_PORT,
    "DATABASE_NAME": DATABASE_NAME,
}

missing_settings = [
    name
    for name, value in required_settings.items()
    if not value
]

if missing_settings:
    raise RuntimeError(
        "Missing database configuration in .env: "
        + ", ".join(missing_settings)
    )


# ------------------------------------------------------------
# PostgreSQL connection URL
# ------------------------------------------------------------

DATABASE_URL = (
    f"postgresql+psycopg://"
    f"{DATABASE_USER}:"
    f"{DATABASE_PASSWORD}@"
    f"{DATABASE_HOST}:"
    f"{DATABASE_PORT}/"
    f"{DATABASE_NAME}"
)


# ------------------------------------------------------------
# SQLAlchemy engine
# ------------------------------------------------------------

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)


# ------------------------------------------------------------
# Session factory
# ------------------------------------------------------------

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


# ------------------------------------------------------------
# Base class for database models
# ------------------------------------------------------------

Base = declarative_base()


# ------------------------------------------------------------
# FastAPI database dependency
# ------------------------------------------------------------

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# ------------------------------------------------------------
# Test database connection
# ------------------------------------------------------------

def test_database_connection():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        print("✅ PostgreSQL connection successful.")
        return True

    except Exception as error:
        print("❌ PostgreSQL connection failed.")
        print(f"Reason: {error}")
        return False


# ------------------------------------------------------------
# Run test when file is executed directly
# ------------------------------------------------------------

if __name__ == "__main__":
    test_database_connection()