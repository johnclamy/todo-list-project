# server/src/server/repositories/books.py
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import Optional, List, Dict, Any
from entities.books import BookEntity, BookCategory, BookPublisher
from models.books import BookCreateModel, BookUpdateModel


class BookRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, book_data: BookCreateModel) -> BookEntity:
        """Create a new book"""
        book_dict = book_data.dict()
        book_dict['categories'] = [cat.value for cat in book_dict.get('categories', [])]
        book_dict['publisher'] = book_dict['publisher'].value
        
        db_book = BookEntity(**book_dict)
        self.db.add(db_book)
        self.db.commit()
        self.db.refresh(db_book)
        return db_book
    
    def get_by_id(self, book_id: int) -> Optional[BookEntity]:
        """Get a book by ID"""
        return self.db.query(BookEntity).filter(BookEntity.id == book_id).first()

    def get_by_isbn(self, isbn_13: str) -> Optional[BookEntity]:
        """Get a book by ISBN-13"""
        return self.db.query(BookEntity).filter(BookEntity.isbn_13 == isbn_13).first()

    def get_all(
        self, 
        skip: int = 0, 
        limit: int = 100,
        search: Optional[str] = None,
        category: Optional[BookCategory] = None,
        publisher: Optional[BookPublisher] = None,
        sort_by: Optional[str] = "title",
        sort_order: Optional[str] = "asc"
    ) -> Dict[str, Any]:
        """Get all books with pagination, filtering, and sorting"""
        query = self.db.query(BookEntity)
        
        # Apply search filter
        if search:
            search_filter = or_(
                BookEntity.title.ilike(f"%{search}%"),
                BookEntity.subtitle.ilike(f"%{search}%"),
                BookEntity.isbn_13.ilike(f"%{search}%"),
                BookEntity.isbn_10.ilike(f"%{search}%")
            )
            query = query.filter(search_filter)
        
        # Apply category filter
        if category:
            query = query.filter(BookEntity.categories.contains([category.value]))
        
        # Apply publisher filter
        if publisher:
            query = query.filter(BookEntity.publisher == publisher.value)
        
        # Get total count
        total = query.count()
        
        # Apply sorting
        if sort_by in ['title', 'published_date', 'page_count', 'created_at']:
            sort_column = getattr(BookEntity, sort_by)
            if sort_order and sort_order.lower() == 'desc':
                query = query.order_by(sort_column.desc())
            else:
                query = query.order_by(sort_column.asc())
        
        # Apply pagination
        items = query.offset(skip).limit(limit).all()
        
        return {
            "items": items,
            "total": total,
            "page": (skip // limit) + 1 if limit > 0 else 1,
            "size": len(items),
            "pages": (total + limit - 1) // limit if limit > 0 else 0
        }

    def update(self, book_id: int, book_data: BookUpdateModel) -> Optional[BookEntity]:
        """Update a book by ID"""
        db_book = self.get_by_id(book_id)
        if not db_book:
            return None
        
        update_data = book_data.dict(exclude_unset=True)
        
        # Handle enum conversions
        if 'categories' in update_data and update_data['categories'] is not None:
            update_data['categories'] = [cat.value for cat in update_data['categories']]
        if 'publisher' in update_data and update_data['publisher'] is not None:
            update_data['publisher'] = update_data['publisher'].value
        
        for field, value in update_data.items():
            setattr(db_book, field, value)
        
        self.db.commit()
        self.db.refresh(db_book)
        return db_book

    def delete(self, book_id: int) -> bool:
        """Delete a book by ID"""
        db_book = self.get_by_id(book_id)
        if not db_book:
            return False
        
        self.db.delete(db_book)
        self.db.commit()
        return True

    def delete_by_isbn(self, isbn_13: str) -> bool:
        """Delete a book by ISBN-13"""
        db_book = self.get_by_isbn(isbn_13)
        if not db_book:
            return False
        
        self.db.delete(db_book)
        self.db.commit()
        return True

    def bulk_create(self, books_data: List[BookCreateModel]) -> List[BookEntity]:
        """Create multiple books at once"""
        created_books = []
        for book_data in books_data:
            book_dict = book_data.dict()
            book_dict['categories'] = [cat.value for cat in book_dict.get('categories', [])]
            book_dict['publisher'] = book_dict['publisher'].value
            db_book = BookEntity(**book_dict)
            self.db.add(db_book)
            created_books.append(db_book)
        
        self.db.commit()
        for book in created_books:
            self.db.refresh(book)
        return created_books

    def get_categories(self) -> List[str]:
        """Get all available categories"""
        return [category.value for category in BookCategory]

    def get_publishers(self) -> List[str]:
        """Get all available publishers"""
        return [publisher.value for publisher in BookPublisher]
