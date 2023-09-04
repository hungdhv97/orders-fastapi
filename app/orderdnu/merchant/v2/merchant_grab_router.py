from typing import Annotated

from fastapi import APIRouter, Path

from app.clients.grab.grab_client import GrabClient
from app.orderdnu.merchant.merchant_model import MerchantResponse
from app.orderdnu.merchant.merchant_service import MerchantService

router = APIRouter()

grab_client = GrabClient()
merchant_service = MerchantService(grab_client)


@router.get("/{merchant_id}", response_model=MerchantResponse)
async def get_merchant_by_id(merchant_id: Annotated[str, Path(example="5-C3C2T8MUVN4HLT")]) -> MerchantResponse:
    merchant_data = await merchant_service.get_grab_merchant_by_id(merchant_id)
    return merchant_data
