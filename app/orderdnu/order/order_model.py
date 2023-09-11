from typing import List

from pydantic import BaseModel

from app.common.annotation.model_fields import ObjectIdField, ProductNameField, PriceField, QuantityField, \
    TotalPriceField, DateTimeField


class OrderItem(BaseModel):
    id: ObjectIdField
    product_name: ProductNameField
    price: PriceField
    quantity: QuantityField


class Order(BaseModel):
    id: ObjectIdField
    user_id: ObjectIdField
    merchant_id: ObjectIdField
    items: List[OrderItem]
    total_price: TotalPriceField
    order_date: DateTimeField


class OrderResponse(BaseModel):
    id: ObjectIdField
    user_id: ObjectIdField
    merchant_id: ObjectIdField
    items: List[OrderItem]
    total_price: TotalPriceField
    order_date: DateTimeField


class CreateOrderItem(BaseModel):
    product_name: ProductNameField
    price: PriceField
    quantity: QuantityField


class CreateOrderRequest(BaseModel):
    user_id: ObjectIdField
    merchant_id: ObjectIdField
    items: List[CreateOrderItem]


class UpdateOrderItem(BaseModel):
    product_name: ProductNameField
    price: PriceField
    quantity: QuantityField


class UpdateOrderRequest(BaseModel):
    id: ObjectIdField
    user_id: ObjectIdField
    merchant_id: ObjectIdField
    items: List[UpdateOrderItem]
