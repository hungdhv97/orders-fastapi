from typing import Annotated, Any

from fastapi import APIRouter, Path

from app.clients.grab.grab_client import GrabClient
from app.orderdnu.merchant.merchant_service import MerchantService
from app.orderdnu.user.user_service import UserService

router = APIRouter()

grab_client = GrabClient()
user_service = UserService()
merchant_service = MerchantService(grab_client, user_service)


@router.get("/{merchant_id}", response_model=Any)
async def get_merchant_by_id(merchant_id: Annotated[str, Path(example="5-C3C2T8MUVN4HLT")]) -> Any:
    merchant_data = await merchant_service.get_grab_merchant_by_id_full_detail(merchant_id)
    return merchant_data
