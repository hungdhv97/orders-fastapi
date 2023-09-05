from mongoengine import Document, StringField, ReferenceField, EnumField

from app.orderdnu.merchant.merchant_model import DeliveryEnum
from app.orderdnu.user.user_document import UserDocument


class MerchantDocument(Document):
    merchant_id = StringField(required=True)
    delivery_type = EnumField(DeliveryEnum, default=DeliveryEnum.GRAB, required=True)
    user = ReferenceField(UserDocument, required=True)

    meta = {
        'indexes': [
            {'fields': ('merchant_id', 'delivery_type', 'user'), 'unique': True}
        ]
    }
