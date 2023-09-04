from fastapi import APIRouter

from app.orderdnu.home.v1.home_router import router as home_router

router = APIRouter(prefix="/api/v1/home", tags=["Home"])

router.include_router(home_router)
