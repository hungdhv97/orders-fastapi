from mongoengine import Document, StringField, ReferenceField

from app.orderdnu.user.user_document import UserDocument


class MerchantDocument(Document):
    id: StringField(required=True, primary_key=True)
    user = ReferenceField(UserDocument)
