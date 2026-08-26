# Pydantic schema representing the data structure

from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Optional


# Define the allowed tech genres/categories
class BookCategory(str, Enum):
    SYSTEMS = "Fiction"
    WEB_DEVELOPMENT = "Non-Fiction"
    MOBILE = "Fantasy"
    AI_AGENTS = "Science Fiction"
    MYSTERY = "Mystery"
    HISTORY = "History"
    BIOGRAPHY = "Biography"


# Base schema (shared attributes)
class BookBaseModel(BaseModel):
    isbn_13: str                     
    title: str                        
    authors: List[str]                
    publisher: str                    
    published_date: str               # Often 'YYYY' or 'YYYY-MM-DD' 

    # Recommended secondary fields
    isbn_10: Optional[str] = None     # For legacy lookups
    page_count: Optional[int] = None  # Useful for reading trackers
    # Enforces that every book in the list must be a valid BookCategory
    categories: List[BookCategory] = Field(default_factory=list)
    image_url: Optional[str] = None   # To display book covers in your UI

