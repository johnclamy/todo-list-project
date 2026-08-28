from models.books import BookCategory, BookPublisher, BookBaseModel
from typing import List


_books: List[BookBaseModel] = [
    BookBaseModel(
        isbn_13="9781492045526",                    
        title="Deep Learning for Coders with fastapi & PyTorch",
        subtitle="AI Applications Without a PhD",                      
        authors=["Jeremy Howard", "Sylvain Gugger"],             
        publisher=BookPublisher.OREILLEY,
        isbn_10=None,
        page_count=None,               
        published_date="2020",
        categories=[BookCategory.MACHINE_LEARNING, BookCategory.PROGRAMMING],
        image_url=None
    ),

    BookBaseModel(
        isbn_13="9781617292231",                  
        title="Grokking Algorithms",
        subtitle="An illustrated guide for programmers and other curious people",                      
        authors=["Aditya Y. Bhargava"],               
        publisher=BookPublisher.MANNING,
        isbn_10=None,
        page_count=None,               
        published_date="2016",
        categories=[BookCategory.PROGRAMMING],
        image_url=None
    ),

    BookBaseModel(
        isbn_13="9780596526849",                    
        title="Head First SQL",
        subtitle="A Brain-Friendly Guide",                      
        authors=["Lynn Beighley"],               
        publisher=BookPublisher.OREILLEY,
        isbn_10=None,
        page_count=None,               
        published_date="2007",
        categories=[BookCategory.DATABASES],
        image_url=None
    ),
]


def get_book_repository() -> List[BookBaseModel]:
    return _books
