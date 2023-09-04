from fastapi import HTTPException
from mongoengine import NotUniqueError
from starlette import status

from app.orderdnu.order.order_document import OrderDocument
from app.orderdnu.order.order_model import Order
from app.orderdnu.user.user_document import UserDocument
from app.orderdnu.user.user_service import UserService

user_service = UserService()


class OrderService:
    async def create_order(self, user_id: str, food_name: str, price: int) -> Order:
        try:
            user = await user_service.get_user(user_id)
            new_order = OrderDocument(user=UserDocument(**dict(user)), food_name=food_name, price=price)
            new_order.save()
            return Order.model_validate({"id": str(new_order.id), "user_id": str(new_order.user.id), **new_order.to_mongo()})
        except NotUniqueError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Order already exists")

    async def get_order(self) -> Order:
        pass

    async def get_orders(self) -> Order:
        pass

    async def update_order(self) -> Order:
        pass

    async def delete_order(self) -> Order:
        pass
