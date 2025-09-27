from typing import cast

import asyncpg

from .settings import get_settings


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
