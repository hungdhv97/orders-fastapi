from typing import Optional

from pydantic import BaseModel


class OrderResponse(BaseModel):
    id: str
    user_id: str
    food_name: str
    price: int


class CreateOrderRequest(BaseModel):
    user_id: str
    food_name: str
    price: int


class UpdateOrderRequest(BaseModel):
    food_name: Optional[str]
    price: Optional[int]


class Order(BaseModel):
    id: str
    user_id: str
    food_name: str
    price: int