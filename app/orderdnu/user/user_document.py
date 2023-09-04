from mongoengine import Document, StringField


class UserDocument(Document):
    username = StringField(required=True, unique=True)
    password = StringField()
    full_name = StringField()
