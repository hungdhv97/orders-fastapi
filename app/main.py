from fastapi import FastAPI

from app.api.v1.user_router import router as user_router

app = FastAPI()

app.include_router(user_router)
