from fastapi import APIRouter

from app.clients.grab.grab_client import GrabClient
from app.orderdnu.merchant.merchant_model import MerchantResponse
from app.orderdnu.merchant.merchant_service import MenuService

router = APIRouter()

grab_client = GrabClient()
menu_service = MenuService(grab_client)


@router.get("/grab/merchants/{merchant_id}", response_model=MerchantResponse)
async def get_menus_grab(merchant_id: str) -> MerchantResponse:
    """5-C3C2T8MUVN4HLT"""
    menu_data = await menu_service.get_menus_grab(merchant_id)
    return menu_data
