from fastapi import APIRouter

from app.orderdnu.order.v1.order_router import router as order_router

router = APIRouter(prefix="/api/v1/orders", tags=["Orders"])

router.include_router(order_router)
