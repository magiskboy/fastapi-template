from contextlib import asynccontextmanager
from fastapi import FastAPI
from .db import create_db_pool
from .health.views import health_router
from .pet_router import pet_router


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

    app.include_router(health_router)
    app.include_router(pet_router)

    return app
