from typing import Any

from app.clients.grab.grab_client import GrabClient
from app.orderdnu.merchant.merchant_model import MerchantResponse


class MerchantService:
    def __init__(self, grab_client: GrabClient):
        self.grab_client = grab_client

    async def get_grab_merchant_by_id(self, merchant_id: str) -> MerchantResponse:
        grab_merchant_response = await self.grab_client.get_merchant(merchant_id)
        return MerchantResponse.model_validate(grab_merchant_response.model_dump())

    async def get_grab_merchant_by_id_full_detail(self, merchant_id: str) -> Any:
        grab_merchant_response = await self.grab_client.get_merchant_full_detail(merchant_id)
        return grab_merchant_response
