from typing import Any

import httpx
from fastapi import HTTPException

from app.clients.grab.grab_merchant_model import GrabMerchantResponse


class GrabClient:
    def __init__(self):
        self.client = httpx.AsyncClient()
        self.base_url = "https://portal.grab.com/foodweb/v2/merchants/"

    async def get_merchant_dto(self, merchant_id: str) -> GrabMerchantResponse:
        url = f"{self.base_url}{merchant_id}"
        try:
            response = await self.client.get(url)
            response.raise_for_status()
            response = response.json()
            return GrabMerchantResponse.model_validate(response["merchant"])
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                raise HTTPException(status_code=404, detail="Merchant not found")
            else:
                raise HTTPException(status_code=500, detail="Internal server error")

    async def get_merchant_full_info(self, merchant_id: str) -> Any:
        url = f"{self.base_url}{merchant_id}"
        try:
            response = await self.client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                raise HTTPException(status_code=404, detail="Merchant not found")
            else:
                raise HTTPException(status_code=500, detail="Internal server error")
