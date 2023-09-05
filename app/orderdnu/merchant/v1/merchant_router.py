from typing import Annotated, List

from fastapi import APIRouter, Body, Query, Path

from app.clients.grab.grab_client import GrabClient
from app.orderdnu.merchant.merchant_model import MerchantResponse, CreateMerchantRequest
from app.orderdnu.merchant.merchant_service import MerchantService
from app.orderdnu.merchant.openapi_examples import CREATE_MERCHANT_EXAMPLES
from app.orderdnu.user.user_service import UserService

router = APIRouter()

grab_client = GrabClient()
user_service = UserService()
merchant_service = MerchantService(user_service)

CreateMerchantRequestBody = Annotated[CreateMerchantRequest, Body(openapi_examples=CREATE_MERCHANT_EXAMPLES)]
ObjectIdQuery = Annotated[str, Query(example="64f6318231e3ac649c61d2e8")]
MerchantIdPath = Annotated[str, Path(example="5-C3C2T8MUVN4HLT")]


@router.post("/", response_model=MerchantResponse)
async def create_merchant(create_merchant_request: CreateMerchantRequestBody) -> MerchantResponse:
    new_merchant = await merchant_service.create_merchant(create_merchant_request.merchant_id,
                                                          create_merchant_request.delivery_type,
                                                          create_merchant_request.user_id)
    merchant_info = await grab_client.get_merchant_full_info(create_merchant_request.merchant_id)
    return MerchantResponse.model_validate({"merchant_info": merchant_info["merchant"], **new_merchant.model_dump()})


@router.get("/", response_model=List[MerchantResponse])
async def get_all_merchants() -> List[MerchantResponse]:
    merchants = await merchant_service.get_all_merchants()
    merchants_response = []
    for merchant in merchants:
        merchant_info = await grab_client.get_merchant_full_info(merchant.merchant_id)
        merchants_response.append(
            MerchantResponse.model_validate({"merchant_info": merchant_info["merchant"], **merchant.model_dump()}))
    return merchants_response


@router.get("/search", response_model=List[MerchantResponse])
async def search_merchants(user_id: ObjectIdQuery):
    merchants = await merchant_service.search_merchants(user_id)
    merchants_response = []
    for merchant in merchants:
        merchant_info = await grab_client.get_merchant_full_info(merchant.merchant_id)
        merchants_response.append(
            MerchantResponse.model_validate({"merchant_info": merchant_info["merchant"], **merchant.model_dump()}))
    return merchants_response


@router.delete("/{merchant_id}", response_model=dict)
async def delete_merchant(merchant_id: MerchantIdPath):
    await merchant_service.delete_merchant(merchant_id)
    return {"message": "Merchant deleted"}
