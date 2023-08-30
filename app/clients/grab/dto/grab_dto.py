from pydantic import BaseModel


class Merchant(BaseModel):
    ID: str


class GrabMenuDto(BaseModel):
    merchant: Merchant
