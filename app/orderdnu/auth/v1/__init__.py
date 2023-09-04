from fastapi import APIRouter

from app.orderdnu.auth.v1.auth_router import router as auth_router

router = APIRouter(prefix="/api/v1/auth", tags=["Auth"])

router.include_router(auth_router)
