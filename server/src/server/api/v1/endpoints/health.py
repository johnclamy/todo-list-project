# server/src/server/api/v1/endpoints/health.py
import platform
import psutil
from datetime import datetime, timezone
from fastapi import APIRouter, status


router = APIRouter(prefix='/health')


@router.get(
    '/',
    status_code=status.HTTP_200_OK,
    summary='Health check',
    description='Check if the API is running and healthy'
)
async def health_check() -> dict [str, str | dict]:
    """Health check endpoint."""
    return {
        'status': 'healthy',
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'version': 'v1',
        'uptime': 'N/A'  # You can track uptime with a startup timer
    }


@router.get(
    '/detailed',
    status_code=status.HTTP_200_OK,
    summary='Detailed health check',
    description='Get detailed system and application health information'
)
async def detailed_health():
    """Detailed health check with system information."""
    return {
        'status': 'healthy',
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'system': {
            'platform': platform.platform(),
            'python_version': platform.python_version(),
            'cpu_count': psutil.cpu_count(),
            'memory_usag': psutil.virtual_memory().percent
        },
        'application': {
            'name': 'Book Management API',
            'version': '1.0.0'
        }
    }
