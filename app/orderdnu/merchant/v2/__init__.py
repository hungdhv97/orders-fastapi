from fastapi import APIRouter

from app.orderdnu.merchant.v2.merchant_router import router as merchant_router

router = APIRouter(prefix="/api/v2/merchants", tags=["Merchants"])

router.include_router(merchant_router)
