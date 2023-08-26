from fastapi import FastAPI
from mongoengine import connect

from app.api.v1.user_router import router as user_router
from app.core.config import settings

connect(host=settings.MONGODB_URI)

app = FastAPI()

app.include_router(user_router)
