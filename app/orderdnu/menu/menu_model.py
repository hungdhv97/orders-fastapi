from pydantic import BaseModel


class GrabMenuResponse(BaseModel):
    id: str
    photo_url: str


class MenuResponse(BaseModel):
    id: str
    photo_url: str
