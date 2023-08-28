from fastapi import FastAPI
from mongoengine import connect
from starlette.middleware.cors import CORSMiddleware

from app.api.v1 import router as v1_router
from app.core.config import settings

connect(host=settings.MONGODB_URI)

app = FastAPI(
    title="Orders Fast API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

app.include_router(v1_router)
