from fastapi import APIRouter

from app.clients.grab.grab_client import GrabClient
from app.orderdnu.menu.menu_model import MenuResponse
from app.orderdnu.menu.menu_service import MenuService

router = APIRouter()

grab_client = GrabClient()
menu_service = MenuService(grab_client)


@router.get("/grab/merchants/{merchant_id}", response_model=MenuResponse)
async def get_menus_grab(merchant_id: str) -> MenuResponse:
    """5-C3C2T8MUVN4HLT"""
    menu_data = await menu_service.get_menus_grab(merchant_id)
    return menu_data
