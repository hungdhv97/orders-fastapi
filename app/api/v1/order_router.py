from typing import List

from fastapi import APIRouter, HTTPException
from mongoengine import NotUniqueError, DoesNotExist, ValidationError
from starlette import status

from app.documents.order_document import Order
from app.documents.user_document import User
from app.models.order_model import OrderResponse, CreateOrderRequest, UpdateOrderRequest

router = APIRouter()


@router.post("/order/", response_model=OrderResponse)
async def create_order(order: CreateOrderRequest) -> OrderResponse:
    try:
        try:
            user = User.objects.get(id=order.user_id)
        except ValidationError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except DoesNotExist:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User does not exist")

        new_order = Order(user=user, food_name=order.food_name, price=order.price)
        new_order.save()
        return OrderResponse(id=str(new_order.id), user_id=str(user.id), food_name=order.food_name, price=order.price)
    except NotUniqueError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Order already exists")


@router.get("/order/{orderid}", response_model=OrderResponse)
async def get_order(orderid: str) -> OrderResponse:
    order = Order.objects(id=orderid).first()
    if order:
        return OrderResponse(id=str(order.id), **order.to_mongo())
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")


@router.put("/order/{orderid}", response_model=OrderResponse)
async def update_order(orderid: str, order_update: UpdateOrderRequest) -> OrderResponse:
    order = Order.objects(id=orderid).first()
    if order:
        for attr, value in order_update.model_dump().items():
            if value is not None:
                setattr(order, attr, value)
        order.save()
        return OrderResponse(**order.to_mongo())
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")


@router.delete("/order/{orderid}", response_model=dict)
async def delete_order(orderid: str):
    order = Order.objects(id=orderid).first()
    if order:
        order.delete()
        return {"message": "Order deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")


@router.get("/orders/", response_model=List[OrderResponse])
async def get_orders(skip: int = 0, limit: int = 10) -> List[OrderResponse]:
    orders = Order.objects.skip(skip).limit(limit)
    return [OrderResponse(id=str(order.id), user_id=str(order.user.id), **order.to_mongo()) for order in orders]
