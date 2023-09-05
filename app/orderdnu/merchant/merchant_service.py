from typing import List

from fastapi import HTTPException
from mongoengine import NotUniqueError, ValidationError, DoesNotExist
from starlette import status

from app.orderdnu.merchant.merchant_document import MerchantDocument
from app.orderdnu.merchant.merchant_model import DeliveryEnum, Merchant
from app.orderdnu.user.user_document import UserDocument
from app.orderdnu.user.user_service import UserService


class MerchantService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

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

    async def delete_merchant(self, merchant_id: str) -> None:
        try:
            MerchantDocument.objects.get(id=merchant_id).delete()
        except ValidationError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except DoesNotExist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Merchant not found")
