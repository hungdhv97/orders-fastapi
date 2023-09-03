from mongoengine import Document, connect, StringField
from pydantic import BaseModel, Field, model_validator

connect(host="mongodb+srv://pyopywhiz:pyopywhiz@pyopywhiz.ws73uvc.mongodb.net/orders")


# <editor-fold desc="Description">
class SomeDocument(Document):
    # id = StringField(primary_key=True, default=str(uuid4()))
    name = StringField()


# </editor-fold>

class BaseModel(BaseModel):
    @model_validator(mode="before")
    @classmethod
    def _set_person_id(cls, data):
        document_id = data.get("_id")
        if document_id:
            data["id"] = str(document_id)
        return data


class SomeModel(BaseModel):
    id: str = Field(..., alias="merchant.ID")
    name: str


document = SomeDocument(name="hung").save()
model = SomeModel(**{"merchant.ID": "123", "name": "hung"})

print(model)
