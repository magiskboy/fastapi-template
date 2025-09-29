from contextlib import asynccontextmanager
from typing import cast
import asyncpg
from fastapi import FastAPI, Request, Response
from .db import create_db_pool


@asynccontextmanager
async def lifespan(_: FastAPI):
    db_pool = await create_db_pool(check=True)
    yield {
        'db_pool': db_pool,
    }
    await db_pool.close()


def create_app() -> FastAPI:
    app = FastAPI(
        lifespan=lifespan,
    )

    @app.get('/healthz')
    async def healthz(request: Request):
        async with request.state.db_pool.acquire() as conn:
            conn = cast(asyncpg.Connection, conn)
            await conn.execute('SELECT 42;')

        return Response('ok')

    return app
