from models.books import BookCategory, BookPublisher, BookBaseModel
from typing import List


_books: List[BookBaseModel] = [
    BookBaseModel(
        isbn_13="978-1-492-D4522-6",                    
        title="Deep Learning for Coders with fastapi & PyTorch",
        subtitle="AI Applications Without a PhD",                      
        authors=["Jeremy Howard", "Sylvain Gugger"],             
        publisher=BookPublisher.OREILLEY,               
        published_date="2020",
        categories=[BookCategory.MACHINE_LEARNING, BookCategory.PROGRAMMING]
    ),

    BookBaseModel(
        isbn_13="978-1-61729-223-1",                  
        title="Grokking Algorithms",
        subtitle="An illustrated guide for programmers and other curious people",                      
        authors=["Aditya Y. Bhargava"],               
        publisher=BookPublisher.MANNING,               
        published_date="2016",
        categories=[BookCategory.PROGRAMMING]
    ),

    BookBaseModel(
        isbn_13="978-0-596-52684-9",                    
        title="Head First SQL",
        subtitle="A Brain-Friendly Guide",                      
        authors=["Lynn Beighley"],               
        publisher=BookPublisher.OREILLEY,               
        published_date="2007",
        categories=[BookCategory.DATABASES]
    ),
]


def get_book_repository() -> List[BookBaseModel]:
    return _books
