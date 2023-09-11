from typing import List

from fastapi import APIRouter

from app.clients.grab.grab_client import GrabClient
from app.common.annotation.fastapi_params import CreateMerchantRequestBody, ObjectIdQuery, ObjectIdPath
from app.orderdnu.merchant.merchant_model import MerchantResponse
from app.orderdnu.merchant.merchant_service import MerchantService
from app.orderdnu.user.user_service import UserService

router = APIRouter()

grab_client = GrabClient()
user_service = UserService()
merchant_service = MerchantService(user_service)


@router.post("/", response_model=MerchantResponse)
async def create_merchant(create_merchant_request: CreateMerchantRequestBody) -> MerchantResponse:
    new_merchant = await merchant_service.create_merchant(create_merchant_request.merchant_id,
                                                          create_merchant_request.delivery_type,
                                                          create_merchant_request.user_id)
    client_merchant_info = await grab_client.get_merchant_full_info(create_merchant_request.merchant_id)
    return MerchantResponse.model_validate(
        {"client_merchant_info": client_merchant_info["merchant"], **new_merchant.model_dump()})


@router.get("/", response_model=List[MerchantResponse])
async def get_all_merchants() -> List[MerchantResponse]:
    merchants = await merchant_service.get_all_merchants()
    merchants_response = []
    for merchant in merchants:
        client_merchant_info = await grab_client.get_merchant_full_info(merchant.merchant_id)
        merchants_response.append(
            MerchantResponse.model_validate(
                {"client_merchant_info": client_merchant_info["merchant"], **merchant.model_dump()}))
    return merchants_response


@router.get("/search", response_model=List[MerchantResponse])
async def search_merchants(user_id: ObjectIdQuery):
    merchants = await merchant_service.search_merchants(user_id)
    merchants_response = []
    for merchant in merchants:
        client_merchant_info = await grab_client.get_merchant_full_info(merchant.merchant_id)
        merchants_response.append(
            MerchantResponse.model_validate(
                {"client_merchant_info": client_merchant_info["merchant"], **merchant.model_dump()}))
    return merchants_response


@router.delete("/{merchant_id}", response_model=dict)
async def delete_merchant(merchant_id: ObjectIdPath):
    await merchant_service.delete_merchant(merchant_id)
    return {"message": "Merchant deleted"}
