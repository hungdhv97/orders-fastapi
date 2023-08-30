from fastapi import APIRouter

from app.orderdnu.menu.v1.menu_grab_router import router as menu_grab_router

router = APIRouter(prefix="/api/v1/menus", tags=["Menus"])

router.include_router(menu_grab_router)
