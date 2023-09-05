from enum import Enum
from typing import List, Annotated

from pydantic import BaseModel, Field

from app.orderdnu.user.user_model import UserResponse, ObjectIdField, User


class FoodItem(BaseModel):
    id: str
    name: str
    available: bool
    img_url: str
    description: str
    price: int


class CategoryItem(BaseModel):
    id: str
    name: str
    available: bool
    items: List[FoodItem]


class Menu(BaseModel):
    categories: List[CategoryItem]


class MerchantClient(BaseModel):
    id: str
    name: str
    photo_url: str
    menu: Menu


##################################################

class DeliveryEnum(str, Enum):
    GRAB = 'grab'
    SHOPEE = 'shopee'


MerchantIdField = Annotated[str, Field(examples=["5-C3C2T8MUVN4HLT"])]
DeliveryTypeField = Annotated[DeliveryEnum, Field(examples=[DeliveryEnum.GRAB])]


class CreateMerchantRequest(BaseModel):
    merchant_id: MerchantIdField
    delivery_type: DeliveryTypeField
    user_id: ObjectIdField


class Merchant(BaseModel):
    id: ObjectIdField
    merchant_id: MerchantIdField
    delivery_type: DeliveryTypeField
    user: User


class MerchantResponse(BaseModel):
    id: ObjectIdField
    delivery_type: DeliveryEnum
    user: UserResponse
    merchant_info: dict
