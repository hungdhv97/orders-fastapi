from fastapi import FastAPI
from mongoengine import connect

from app.api.v1.routers.order_router import router as order_router
from app.api.v1.routers.user_router import router as user_router
from app.core.config import settings

connect(host=settings.MONGODB_URI)

tags_metadata = [{"name": "users"}, {"name": "orders"}]

app = FastAPI(
    title="Orders Fast API",
    openapi_tags=tags_metadata
)

app.include_router(user_router, tags=["users"])
app.include_router(order_router, tags=["orders"])
