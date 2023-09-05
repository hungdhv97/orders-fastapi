from mongoengine import Document, StringField, ReferenceField, EnumField

from app.orderdnu.merchant.merchant_model import DeliveryEnum
from app.orderdnu.user.user_document import UserDocument


class MerchantDocument(Document):
    merchant_id = StringField(required=True, unique_with='delivery_type')
    delivery_type = EnumField(DeliveryEnum, default=DeliveryEnum.GRAB, required=True, unique_with='user')
    user = ReferenceField(UserDocument)
