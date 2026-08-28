#server/src/server/api/v1/router.py
from fastapi import APIRouter
from api.v1.endpoints import books, health, version


api_router = APIRouter()


# Include all endpoint routers
api_router.include_router(version.router, tags=["version"])
api_router.include_router(health.router, tags=["health"])
api_router.include_router(books.router, tags=["books"])
