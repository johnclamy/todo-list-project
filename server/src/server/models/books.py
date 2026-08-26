# Pydantic schema representing the data structure

from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Optional


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
    isbn_13: str                     
    title: str
    subtitle: str                        
    authors: List[str]                
    publisher: BookPublisher                    
    published_date: str               # Often 'YYYY' or 'YYYY-MM-DD' 

    # Recommended secondary fields
    isbn_10: Optional[str] = None     # For legacy lookups
    page_count: Optional[int] = None  # Useful for reading trackers
    # Enforces that every book in the list must be a valid BookCategory
    categories: List[BookCategory] = Field(default_factory=list)
    image_url: Optional[str] = None   # To display book covers in your UI
