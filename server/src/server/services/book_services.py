# server/src/server/services/book_service.py
from typing import Optional, List, Dict, Any
from models.books import BookCreateModel, BookUpdateModel, BookResponseModel
from entities.books import BookCategory, BookPublisher
from repositories.book_repository import BookRepository
from sqlalchemy.orm import Session


class BookService:
    """Business logic layer between API and repository"""
    
    def __init__(self, db: Session):
        self.repository = BookRepository(db)

    def create_book(self, book_data: BookCreateModel) -> BookResponseModel:
        """Create a new book with business logic"""
        # Check if book already exists
        existing = self.repository.get_by_isbn(book_data.isbn_13)
        if existing:
            raise ValueError(f"Book with ISBN-13 {book_data.isbn_13} already exists")
        
        # Additional business logic can go here
        # e.g., validate author names, normalize data, etc.
        
        db_book = self.repository.create(book_data)
        return BookResponseModel(**db_book.to_dict())

    def get_book(self, book_id: int) -> Optional[BookResponseModel]:
        """Get a book by ID"""
        db_book = self.repository.get_by_id(book_id)
        if not db_book:
            return None
        return BookResponseModel(**db_book.to_dict())

    def get_books(
        self,
        skip: int = 0,
        limit: int = 100,
        search: Optional[str] = None,
        category: Optional[BookCategory] = None,
        publisher: Optional[BookPublisher] = None,
        sort_by: Optional[str] = "title",
        sort_order: Optional[str] = "asc"
    ) -> Dict[str, Any]:
        """Get all books with filters"""
        result = self.repository.get_all(
            skip=skip,
            limit=limit,
            search=search,
            category=category,
            publisher=publisher,
            sort_by=sort_by,
            sort_order=sort_order
        )
        # Convert entities to response objects
        result["items"] = [BookResponseModel(**book.to_dict()) for book in result["items"]]
        return result

    def update_book(self, book_id: int, book_data: BookUpdateModel) -> Optional[BookResponseModel]:
        """Update a book"""
        db_book = self.repository.update(book_id, book_data)
        if not db_book:
            return None
        return BookResponseModel(**db_book.to_dict())

    def delete_book(self, book_id: int) -> bool:
        """Delete a book"""
        return self.repository.delete(book_id)

    def delete_book_by_isbn(self, isbn_13: str) -> bool:
        """Delete a book by ISBN"""
        return self.repository.delete_by_isbn(isbn_13)

    def bulk_create_books(self, books_data: List[BookCreateModel]) -> List[BookResponseModel]:
        """Create multiple books"""
        # Check for duplicates
        for book in books_data:
            existing = self.repository.get_by_isbn(book.isbn_13)
            if existing:
                raise ValueError(f"Book with ISBN-13 {book.isbn_13} already exists")
        
        db_books = self.repository.bulk_create(books_data)
        return [BookResponseModel(**book.to_dict()) for book in db_books]
