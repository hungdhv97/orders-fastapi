from datetime import datetime

from mongoengine import Document, StringField, ReferenceField, IntField, FloatField, ListField, DateTimeField

from app.orderdnu.merchant.merchant_document import MerchantDocument
from app.orderdnu.user.user_document import UserDocument


class OrderItemDocument(Document):
    product_name = StringField(required=True)
    price = FloatField(required=True)
    quantity = IntField(default=1)


class OrderDocument(Document):
    user = ReferenceField(UserDocument, required=True)
    merchant = ReferenceField(MerchantDocument, required=True)
    items = ListField(ReferenceField(OrderItemDocument))
    total_price = FloatField(required=True)
    order_date = DateTimeField(default=datetime.utcnow)
    note = StringField(default="")
