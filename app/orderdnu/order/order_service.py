from typing import List, Optional

from fastapi import HTTPException
from mongoengine import NotUniqueError, DoesNotExist, ValidationError
from starlette import status

from app.orderdnu.merchant.merchant_service import MerchantService
from app.orderdnu.order.order_document import OrderDocument
from app.orderdnu.order.order_model import Order
from app.orderdnu.user.user_document import UserDocument
from app.orderdnu.user.user_service import UserService


class OrderService:
    def __init__(self, user_service: UserService, merchant_service: MerchantService):
        self.user_service = user_service
        self.merchant_service = merchant_service

    async def create_order(self, user_id: str, food_name: str, price: int) -> Order:
        try:
            user = await self.user_service.get_user_by_id(user_id)
            new_order = OrderDocument(user=UserDocument(**dict(user)), food_name=food_name, price=price)
            new_order.save()
            return Order.model_validate(
                {"id": str(new_order.id), "user_id": str(new_order.user.id), **new_order.to_mongo()})
        except NotUniqueError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Order already exists")

    async def get_order(self, order_id: str) -> Order:
        try:
            order = UserDocument.objects.get(id=order_id)
            return Order.model_validate({"id": str(order.id), "user_id": str(order.user.id), **order.to_mongo()})
        except ValidationError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except DoesNotExist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")

    async def get_orders(self, skip: int = 0, limit: int = 10) -> List[Order]:
        orders = OrderDocument.objects.skip(skip).limit(limit)
        return [Order.model_validate({"id": str(order.id), "user_id": str(order.user.id), **order.to_mongo()}) for order
                in orders]

    async def update_order(self, order_id: str, food_name: Optional[str], price: Optional[int]) -> Order:
        order = await self.get_order(order_id)
        user = await self.user_service.get_user_by_id(order.user_id)
        if food_name:
            order.food_name = food_name
        if price:
            order.price = price
        UserDocument(user=UserDocument(**dict(user)), **dict(order)).save()
        return order

    async def delete_order(self, order_id: str) -> None:
        try:
            OrderDocument.objects.get(id=order_id).delete()
        except ValidationError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except DoesNotExist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
