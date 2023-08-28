from typing import Any

import httpx
from fastapi import APIRouter

router = APIRouter()


@router.get("/fetch_merchant_data/")
async def fetch_merchant_data() -> Any:
    url = "https://portal.grab.com/foodweb/v2/merchants/5-C3C2T8MUVN4HLT"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()

    return response.json()
