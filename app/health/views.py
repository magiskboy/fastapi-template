import logging

import asyncpg
from fastapi import APIRouter, Depends, Response
from starlette import status

from ..db import get_db_conn

health_router = APIRouter(
    tags=['health'],
)

logger = logging.getLogger(__name__)


@health_router.get(
    '/healthz',
    status_code=status.HTTP_200_OK,
)
async def healthz(
    conn: asyncpg.Connection = Depends(get_db_conn),
) -> Response:
    try:
        await conn.execute('SELECT 42;')
    except Exception:
        logger.exception('Failed to connect to database')
        return Response(
            'Connection to database failed',
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        )

    return Response('ok')
