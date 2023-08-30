from pydantic import BaseModel


class MenuResponse(BaseModel):
    photo_url: str
