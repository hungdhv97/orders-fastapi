from fastapi import APIRouter

from app.orderdnu.user.v1.user_router import router as user_router

router = APIRouter(prefix="/api/v1/users", tags=["Users (Optional)"])

router.include_router(user_router)
