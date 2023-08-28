from fastapi import FastAPI
from mongoengine import connect
from starlette.middleware.cors import CORSMiddleware

from app.api.v1.routers.client_router import router as client_router
from app.api.v1.routers.order_router import router as order_router
from app.api.v1.routers.user_router import router as user_router
from app.core.config import settings

connect(host=settings.MONGODB_URI)

app = FastAPI(
    title="Orders Fast API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

app.include_router(client_router, tags=["Clients"])
app.include_router(user_router, tags=["Users"])
app.include_router(order_router, tags=["Orders"])
