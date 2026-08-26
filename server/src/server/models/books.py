# Pydantic schema representing the data structure

from pydantic import BaseModel
from typing import List, Optional


# Base schema (shared attributes)
class BookBaseModel(BaseModel):
    isbn_13: str                      # Official unique key
    title: str                        # Core display field
    authors: List[str]                # Supports multiple authors
    publisher: str                    # For publication reference
    published_date: str               # Often 'YYYY' or 'YYYY-MM-DD'
    
    # Recommended secondary fields for a functional app
    isbn_10: Optional[str] = None     # For legacy lookups
    page_count: Optional[int] = None  # Useful for reading trackers
    categories: List[str] = field(default_factory=list) # e.g., ["Fiction", "History"]
    image_url: Optional[str] = None  # To display book covers in your UI

