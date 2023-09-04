from typing import List

from pydantic import BaseModel, Field


class GrabFoodItem(BaseModel):
    id: str = Field(..., alias="ID")
    name: str
    available: bool = Field(default=True)
    img_url: str = Field(..., alias="imgHref")
    description: str = Field(default="")
    price: int = Field(..., alias="priceInMinorUnit")


class GrabCategoryItem(BaseModel):
    id: str = Field(default="", alias="ID")
    name: str
    available: bool
    items: List[GrabFoodItem]


class GrabMenu(BaseModel):
    categories: List[GrabCategoryItem]


class GrabMerchantResponse(BaseModel):
    id: str = Field(..., alias="ID")
    name: str
    photo_url: str = Field(..., alias="photoHref")
    menu: GrabMenu
