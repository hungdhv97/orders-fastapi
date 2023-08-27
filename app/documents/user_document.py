from mongoengine import Document, StringField


class User(Document):
    username = StringField(required=True, unique=True)
    full_name = StringField()
