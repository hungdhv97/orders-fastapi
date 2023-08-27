from mongoengine import Document, StringField, ReferenceField, IntField

from app.documents.user_document import User


class Order(Document):
    user = ReferenceField(User, required=True)
    food_name = StringField(required=True)
    price = IntField(default=0, required=True)
