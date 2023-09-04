from fastapi import APIRouter

from app.orderdnu.merchant.v1.merchant_grab_router import router as merchant_grab_router

router = APIRouter(prefix="/api/v1/grab/merchant", tags=["Merchants"])

router.include_router(merchant_grab_router)
