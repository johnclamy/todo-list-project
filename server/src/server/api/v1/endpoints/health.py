from fastapi import APIRouter


router = APIRouter(prefix='/health')


@router.get('/')
def get_books() -> dict[str, list[str]]:
    return {"health check": ["API is running", "No errors detected"]}
