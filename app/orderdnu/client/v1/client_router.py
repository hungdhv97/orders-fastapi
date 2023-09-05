from typing import Annotated, Any

from fastapi import APIRouter, Path

from app.clients.grab.grab_client import GrabClient
from app.clients.grab.grab_merchant_model import GrabMerchantResponse

router = APIRouter()

grab_client = GrabClient()

ClientMerchantIdPath = Annotated[str, Path(example="5-C3C2T8MUVN4HLT")]


@router.get("/grab/merchant/{client_merchant_id}", response_model=Any)
async def get_merchant_full_info(client_merchant_id: ClientMerchantIdPath) -> Any:
    merchant_data = await grab_client.get_merchant_full_info(client_merchant_id)
    return merchant_data


@router.get("/grab/merchant/{client_merchant_id}/dto", response_model=GrabMerchantResponse)
async def get_merchant_dto(client_merchant_id: ClientMerchantIdPath) -> GrabMerchantResponse:
    merchant_data = await grab_client.get_merchant_dto(client_merchant_id)
    return merchant_data
