from typing import Any

from fastapi import APIRouter

from app.clients.grab.grab_client import GrabClient
from app.clients.grab.grab_merchant_model import GrabMerchantResponse
from app.common.annotation.fastapi_params import ClientMerchantIdPath

router = APIRouter(prefix="/grab")

grab_client = GrabClient()


@router.get("/merchant/{client_merchant_id}", response_model=Any)
async def get_merchant_full_info(client_merchant_id: ClientMerchantIdPath) -> Any:
    merchant_data = await grab_client.get_merchant_full_info(client_merchant_id)
    return merchant_data


@router.get("/merchant/{client_merchant_id}/dto", response_model=GrabMerchantResponse)
async def get_merchant_dto(client_merchant_id: ClientMerchantIdPath) -> GrabMerchantResponse:
    merchant_data = await grab_client.get_merchant_dto(client_merchant_id)
    return merchant_data
