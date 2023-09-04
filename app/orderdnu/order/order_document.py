from mongoengine import Document, StringField, ReferenceField, IntField

from app.orderdnu.user.user_document import UserDocument


class OrderDocument(Document):
    user = ReferenceField(UserDocument, required=True)
    food_name = StringField(required=True)
    price = IntField(default=0, required=True)
