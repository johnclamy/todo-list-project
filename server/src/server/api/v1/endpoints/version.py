from fastapi import APIRouter


router = APIRouter(prefix='/version')


@router.get('/')
def get_books() -> dict[str, str | bool]:
    return {
        "version": "v1",
        "status": "development",
        "deprecated": False
    }
