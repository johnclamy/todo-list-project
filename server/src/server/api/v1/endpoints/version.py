# server/src/server/api/v1/endpoints/verison.py
from fastapi import APIRouter


router = APIRouter(prefix='/version')


@router.get('/')
async def get_version() -> dict[str, str | bool]:
    return {
        "version": "v1",
        "status": "development",
        "deprecated": False
    }
