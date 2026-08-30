# server/src/server/database/connection.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from entities.books import Base
from typing import Generator
import os


# Database configuration - you can use environment variables
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./books.db")


# Create engine with appropriate settings
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in SQLALCHEMY_DATABASE_URL else {},
    echo=False  # Set to True for SQL logging
)


# Create session local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_tables():
    """Create all database tables"""
    Base.metadata.create_all(bind=engine)


def drop_tables():
    """Drop all database tables (use with caution!)"""
    Base.metadata.drop_all(bind=engine)


def get_db() -> Generator[Session, None, None]:
    """Get database session dependency"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Optional: Context manager for database sessions
from contextlib import contextmanager

@contextmanager
def get_db_context():
    """Context manager for database sessions"""
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
