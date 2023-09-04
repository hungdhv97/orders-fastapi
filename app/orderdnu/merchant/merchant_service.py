from app.clients.grab.grab_client import GrabClient
from app.orderdnu.merchant.merchant_model import MerchantResponse


class MenuService:
    def __init__(self, grab_client: GrabClient):
        self.grab_client = grab_client

    async def get_menus_grab(self, merchant_id: str) -> MerchantResponse:
        grab_merchant_response = await self.grab_client.get_menus(merchant_id)
        return MerchantResponse.model_validate(grab_merchant_response.model_dump())
