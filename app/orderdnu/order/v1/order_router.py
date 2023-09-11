from typing import List

from fastapi import APIRouter

from app.common.annotation.fastapi_params import CreateOrderRequestBody, UpdateOrderRequestBody
from app.orderdnu.merchant.merchant_service import MerchantService
from app.orderdnu.order.order_model import OrderResponse
from app.orderdnu.order.order_service import OrderService
from app.orderdnu.user.user_service import UserService

router = APIRouter()
user_service = UserService()
merchant_service = MerchantService(user_service)
order_service = OrderService(user_service, merchant_service)


@router.post("/", response_model=OrderResponse)
async def create_order(order: CreateOrderRequestBody) -> OrderResponse:
    new_order = await order_service.create_order(order.user_id, order.food_name, order.price)
    return OrderResponse.model_validate(new_order.model_dump())


@router.get("/{order_id}", response_model=OrderResponse)
async def get_order(order_id: str) -> OrderResponse:
    order = await order_service.get_order(order_id)
    return OrderResponse.model_validate(order.model_dump())


@router.put("/{order_id}", response_model=OrderResponse)
async def update_order(order_id: str, order_update: UpdateOrderRequestBody) -> OrderResponse:
    order = await order_service.update_order(order_id, order_update.food_name, order_update.price)
    return OrderResponse.model_validate(order.model_dump())


@router.delete("/{order_id}", response_model=dict)
async def delete_order(order_id: str) -> dict:
    await order_service.delete_order(order_id)
    return {"message": "Order deleted"}


@router.get("/", response_model=List[OrderResponse])
async def get_orders(skip: int = 0, limit: int = 10) -> List[OrderResponse]:
    orders = await order_service.get_orders(skip, limit)
    return [OrderResponse.model_validate(order.model_dump()) for order in orders]
