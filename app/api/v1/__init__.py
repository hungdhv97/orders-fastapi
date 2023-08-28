from fastapi import APIRouter

from app.api.v1.routers.menu_router import router as menu_router
from app.api.v1.routers.order_router import router as order_router
from app.api.v1.routers.user_router import router as user_router

router = APIRouter(prefix="/api/v1")

router.include_router(menu_router, tags=["Menus"])
router.include_router(user_router, tags=["Users"])
router.include_router(order_router, tags=["Orders"])
