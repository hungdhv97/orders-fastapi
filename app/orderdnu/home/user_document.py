from mongoengine import Document, StringField


class UserDocument(Document):
    username = StringField(required=True, unique=True)
    full_name = StringField()
