from fastapi import APIRouter


router = APIRouter(prefix='/books')


@router.get('/')
def get_books() -> dict[str, str]:
    return {"msg": "book list will go here"}
