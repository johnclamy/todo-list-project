# server/src/server/entities/books.py
from sqlalchemy import Column, String, Integer, JSON, Enum as SQLEnum, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone
from server.models.books import BookCategory, BookPublisher


Base = declarative_base()


class BookEntity(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    isbn_13 = Column(String(13), unique=True, index=True, nullable=False)
    title = Column(String(255), nullable=False)
    subtitle = Column(String(255), nullable=True)
    authors = Column(JSON, nullable=False)  # Store as JSON array
    publisher = Column(SQLEnum(BookPublisher), nullable=False)
    published_date = Column(String(20), nullable=False)
    isbn_10 = Column(String(10), nullable=True)
    page_count = Column(Integer, nullable=True)
    categories = Column(JSON, nullable=False, default=list)  # Store as JSON array
    image_url = Column(String(500), nullable=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    def to_dict(self):
        """Convert entity to dictionary"""

        publisher_value = (
            self.publisher.value
            if self.publisher is not None and isinstance(self.publisher, BookPublisher)
            else self.publisher
        )
        created_at_value = self.created_at.isoformat() if self.created_at is not None else None
        updated_at_value = self.updated_at.isoformat() if self.updated_at is not None else None

        return {
            "id": self.id,
            "isbn_13": self.isbn_13,
            "title": self.title,
            "subtitle": self.subtitle,
            "authors": self.authors,
            "publisher": publisher_value,
            "published_date": self.published_date,
            "isbn_10": self.isbn_10,
            "page_count": self.page_count,
            "categories": self.categories,
            "image_url": self.image_url,
            "created_at": created_at_value,
            "updated_at": updated_at_value,
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Create entity from dictionary"""
        # Convert enum values back to enum objects if needed
        if 'publisher' in data and data['publisher']:
            data['publisher'] = BookPublisher(data['publisher'])
        return cls(**data)
