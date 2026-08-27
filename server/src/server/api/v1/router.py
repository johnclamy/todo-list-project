from fastapi import APIRouter
from api.v1.endpoints import books


api_router = APIRouter()


# Include all endpoint routers
api_router.include_router(books.router, tags=["books"])
