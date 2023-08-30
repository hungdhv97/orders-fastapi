from typing import Any, Callable, Annotated
from uuid import uuid4

from bson import ObjectId
from mongoengine import Document, connect, StringField
from pydantic import BaseModel, Field, GetJsonSchemaHandler, root_validator, model_validator
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema

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
    id: str
    name: str




document = SomeDocument(name="hung").save()
model = SomeModel(**document.to_mongo())

print(model)
