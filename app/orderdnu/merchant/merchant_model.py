from pydantic import BaseModel

from app.common.annotation.model_fields import MerchantIdField, DeliveryTypeField, ObjectIdField
from app.orderdnu.merchant.merchant_enum import DeliveryEnum
from app.orderdnu.user.user_model import UserResponse, User


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
    client_client_merchant_info: dict
