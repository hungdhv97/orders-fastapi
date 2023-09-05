from fastapi import FastAPI
from mongoengine import connect
from starlette.middleware.cors import CORSMiddleware

from app.common.settings.config import settings
from app.orderdnu.client.v1 import router as auth_v1_router
from app.orderdnu.merchant.v1 import router as merchant_v1_router
from app.orderdnu.merchant.v2 import router as merchant_v2_router
from app.orderdnu.order.v1 import router as order_v1_router
from app.orderdnu.user.v1 import router as user_v1_router

connect(host=settings.MONGODB_URI)

app = FastAPI(
    title="OrderDnU Fast API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_v1_router)
app.include_router(client_v1_router)
app.include_router(merchant_v1_router)
app.include_router(merchant_v2_router)
app.include_router(user_v1_router)
app.include_router(order_v1_router)
