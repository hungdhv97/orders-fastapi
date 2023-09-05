from typing import Annotated

from fastapi import APIRouter, Path, Body

from app.clients.grab.grab_client import GrabClient
from app.orderdnu.merchant.merchant_model import MerchantClient, MerchantResponse, CreateMerchantRequest
from app.orderdnu.merchant.merchant_service import MerchantService
from app.orderdnu.merchant.openapi_examples import CREATE_MERCHANT_EXAMPLES
from app.orderdnu.user.user_service import UserService

router = APIRouter()

grab_client = GrabClient()
user_service = UserService()
merchant_service = MerchantService(grab_client, user_service)

CreateMerchantRequestBody = Annotated[CreateMerchantRequest, Body(openapi_examples=CREATE_MERCHANT_EXAMPLES)]


@router.post("/", response_model=MerchantResponse)
async def create_merchant(create_merchant_request: CreateMerchantRequestBody) -> MerchantResponse:
    new_merchant = await merchant_service.create_merchant(create_merchant_request.merchant_id,
                                                          create_merchant_request.delivery_type,
                                                          create_merchant_request.user_id)
    merchant_info = await merchant_service.get_grab_merchant_by_id_full_detail(create_merchant_request.merchant_id)
    return MerchantResponse.model_validate({"merchant_info": merchant_info["merchant"], **new_merchant.model_dump()})


@router.get("/{merchant_id}", response_model=MerchantClient)
async def get_merchant_by_id(merchant_id: Annotated[str, Path(example="5-C3C2T8MUVN4HLT")]) -> MerchantClient:
    merchant_data = await merchant_service.get_grab_merchant_by_id(merchant_id)
    return merchant_data
