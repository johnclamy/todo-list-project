# server/src/server/models/books.py
# Pydantic schema representing the data structure

from enum import Enum
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from datetime import datetime


# Define the allowed tech genres/categories
class BookCategory(str, Enum):
    SYSTEMS = "Systems"
    WEB_DEVELOPMENT = "Web Development"
    MOBILE_DEVELOPMENT = "Mobile Development"
    AI_AGENTS = "AI Agents"
    MACHINE_LEARNING = "Machine Learning"
    DATABASES = "Databases"
    PROGRAMMING = "Programming"


# Define the allowed tech publishers
class BookPublisher(str, Enum):
    MANNING = "Manning Publications Co"
    OREILLEY = "O'Reilly Media Inc."
    PACKT = "Packt Publishing Ltd"


# Base schema (shared attributes)
class BookBaseModel(BaseModel):
    isbn_13: str = Field(..., min_length=13, max_length=13, description="ISBN-13 identifier as a string prop")                    
    title: str = Field(..., min_length=1, max_length=255)
    subtitle: Optional[str] = Field(None, max_length=255)                        
    authors: List[str] = Field(..., min_length=1)               
    publisher: BookPublisher                    
    published_date: str = Field(..., pattern=r'^\d{4}(-\d{2}-\d{2})?$', description="YYYY or YYYY-MM-DD") 

    # Recommended secondary fields
    isbn_10: Optional[str] = Field(None, min_length=10, max_length=10)
    page_count: Optional[int] = Field(None, gt=0)
    categories: List[BookCategory] = Field(default_factory=list)
    image_url: Optional[str] = Field(None, max_length=500)   

    @field_validator('isbn_13')
    @classmethod
    def validate_isbn_13(cls, v):
        if not v.isdigit():
            raise ValueError('ISBN-13 must contain only digits')
        return v


class BookCreateModel(BookBaseModel):
    pass


class BookUpdateModel(BaseModel):
    isbn_13: Optional[str] = Field(None, min_length=13, max_length=13)
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    subtitle: Optional[str] = Field(None, max_length=255)
    authors: Optional[List[str]] = Field(None, min_length=1)
    publisher: Optional[BookPublisher] = None
    published_date: Optional[str] = Field(None, pattern=r'^\d{4}(-\d{2}-\d{2})?$')
    isbn_10: Optional[str] = Field(None, min_length=10, max_length=10)
    page_count: Optional[int] = Field(None, gt=0)
    categories: Optional[List[BookCategory]] = None
    image_url: Optional[str] = Field(None, max_length=500)


class BookResponseModel(BookBaseModel):
    id: int
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True


class BookListResponseModel(BaseModel):
    items: List[BookResponseModel]
    total: int
    page: int
    size: int
    pages: int
