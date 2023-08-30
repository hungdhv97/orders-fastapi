from fastapi import FastAPI
from mongoengine import connect
from starlette.middleware.cors import CORSMiddleware

from app.common.settings.config import settings
from app.orderdnu.menu.v1 import router as menu_v1_router
from app.orderdnu.order.v1 import router as order_v1_router
from app.orderdnu.user.v1 import router as user_v1_router

connect(host=settings.MONGODB_URI)

app = FastAPI(
    title="OrderDnU Fast API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

app.include_router(menu_v1_router)
app.include_router(user_v1_router)
app.include_router(order_v1_router)
