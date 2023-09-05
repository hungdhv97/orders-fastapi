from typing import Any, List

from fastapi import HTTPException
from mongoengine import NotUniqueError
from starlette import status

from app.clients.grab.grab_client import GrabClient
from app.orderdnu.merchant.merchant_document import MerchantDocument
from app.orderdnu.merchant.merchant_model import MerchantClient, DeliveryEnum, Merchant
from app.orderdnu.user.user_document import UserDocument
from app.orderdnu.user.user_service import UserService


class MerchantService:
    def __init__(self, grab_client: GrabClient, user_service: UserService):
        self.grab_client = grab_client
        self.user_service = user_service

    async def get_grab_merchant_by_id(self, merchant_id: str) -> MerchantClient:
        grab_merchant_response = await self.grab_client.get_merchant(merchant_id)
        return MerchantClient.model_validate(grab_merchant_response.model_dump())

    async def get_grab_merchant_by_id_full_detail(self, merchant_id: str) -> Any:
        grab_merchant_response = await self.grab_client.get_merchant_full_detail(merchant_id)
        return grab_merchant_response

    async def create_merchant(self, merchant_id: str, delivery_type: DeliveryEnum, user_id: str) -> Merchant:
        try:
            user = await self.user_service.get_user_by_id(user_id)
            new_merchant = MerchantDocument(merchant_id=merchant_id, delivery_type=delivery_type,
                                            user=UserDocument(**dict(user)))
            new_merchant.save()
            return Merchant.model_validate({"id": str(new_merchant.id), **new_merchant.to_mongo(), "user": user})
        except NotUniqueError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=f"Merchant already exists")

    async def get_all_merchants(self) -> List[Merchant]:
        merchant_documents = MerchantDocument.objects()
        merchants = []
        for merchant_document in merchant_documents:
            user = await self.user_service.get_user_by_id(merchant_document.user.id)
            merchants.append(Merchant.model_validate(
                {"id": str(merchant_document.id), **merchant_document.to_mongo(), "user": user}))
        return merchants

    async def search_merchants(self, user_id: str) -> List[Merchant]:
        user = await self.user_service.get_user_by_id(user_id)
        merchant_documents = MerchantDocument.objects(user=user_id)
        merchants = []
        for merchant_document in merchant_documents:
            merchants.append(Merchant.model_validate(
                {"id": str(merchant_document.id), **merchant_document.to_mongo(), "user": user}))
        return merchants
