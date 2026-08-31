# server/src/server/api/v1/endpoints/books.py
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import Optional, List
from database.connection import get_db
from models.books import (
    BookCreateModel, BookUpdateModel, BookResponseModel,
    BookListResponseModel, BookCategory, BookPublisher
)
from services.book_services import BookService


router = APIRouter(prefix='/books')


@router.get('/')
async def get_books() -> dict[str, str]:
    return {"msg": "book list will go here"}
