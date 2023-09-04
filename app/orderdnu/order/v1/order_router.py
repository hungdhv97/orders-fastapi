from typing import List

from fastapi import APIRouter, HTTPException
from mongoengine import NotUniqueError, DoesNotExist, ValidationError
from starlette import status

from app.orderdnu.order.order_document import OrderDocument
from app.orderdnu.order.order_model import OrderResponse, CreateOrderRequest, UpdateOrderRequest
from app.orderdnu.order.order_service import OrderService
from app.orderdnu.user.user_document import UserDocument

router = APIRouter()
order_service = OrderService()

@router.post("/", response_model=OrderResponse)
async def create_order(order: CreateOrderRequest) -> OrderResponse:
    new_order = await order_service.create_order(order.user_id, order.food_name, order.price )
    return OrderResponse.model_validate(new_order.model_dump())

@router.get("/{order_id}", response_model=OrderResponse)
async def get_order(order_id: str) -> OrderResponse:
    order = OrderDocument.objects(id=order_id).first()
    if order:
        return OrderResponse(id=str(order.id), **order.to_mongo())
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")


@router.put("/{order_id}", response_model=OrderResponse)
async def update_order(order_id: str, order_update: UpdateOrderRequest) -> OrderResponse:
    order = OrderDocument.objects(id=order_id).first()
    if order:
        for attr, value in order_update.model_dump().items():
            if value is not None:
                setattr(order, attr, value)
        order.save()
        return OrderResponse(**order.to_mongo())
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")


@router.delete("/{order_id}", response_model=dict)
async def delete_order(order_id: str):
    order = OrderDocument.objects(id=order_id).first()
    if order:
        order.delete()
        return {"message": "Order deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")


@router.get("/", response_model=List[OrderResponse])
async def get_orders(skip: int = 0, limit: int = 10) -> List[OrderResponse]:
    orders = OrderDocument.objects.skip(skip).limit(limit)
    return [OrderResponse(id=str(order.id), user_id=str(order.user.id), **order.to_mongo()) for order in orders]
