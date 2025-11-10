from typing import cast
from typing import cast, AsyncGenerator

import asyncpg
from fastapi import Request

from .settings import get_settings


async def get_db_conn(request: Request) -> AsyncGenerator[asyncpg.Connection, None]:
    async with request.app.state.db_pool.acquire() as conn:
        yield conn


async def create_db_pool(check: bool = True):
    settings = get_settings()
    db_pool = await asyncpg.create_pool(
        dsn=settings.database_uri,
    )

    if check:
        async with db_pool.acquire() as conn:
            conn = cast(asyncpg.Connection, conn)
            await conn.execute('SELECT 42;')

    return db_pool
