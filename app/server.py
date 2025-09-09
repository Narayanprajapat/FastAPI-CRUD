from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from app.api import routers
from app.utils.logger import logging
from app.db.session import engine, Base


logger = logging.getLogger(name="server.py")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    logger.info("Stopping")


app = FastAPI(title="Stantech.ai Assessment", lifespan=lifespan)


@app.middleware("http")
async def log_middleware(request: Request, call_next):
    logger.info(f"Accessing {request.url.path}")
    response = await call_next(request)
    logger.info(f"Finished {request.url.path}")
    return response


app.add_middleware(
    CORSMiddleware,
    **{
        "allow_origins": [],  # list of allowed origins
        "allow_credentials": True,
        "allow_methods": ["*"],  # ["GET", "POST"] if you want to restrict
        "allow_headers": ["*"],  # ["Authorization", "Content-Type"] if restricted)
    },
)


app.include_router(router=routers, prefix="/api/v1")
