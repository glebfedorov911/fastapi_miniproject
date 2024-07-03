from fastapi import FastAPI

import uvicorn

from contextlib import asynccontextmanager

from core.models import db_helper, Base
from core.config import settings

from car.views import router as cars_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

app = FastAPI(lifespan=lifespan)
app.include_router(cars_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)