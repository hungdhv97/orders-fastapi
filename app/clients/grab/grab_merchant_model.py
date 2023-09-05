from typing import List

from pydantic import BaseModel, Field


class GrabFoodItem(BaseModel):
    ID: str
    name: str
    available: bool = True
    imgHref: str
    description: str = ""
    priceInMinorUnit: int


class GrabCategoryItem(BaseModel):
    ID: str = Field(default="")
    name: str
    available: bool
    items: List[GrabFoodItem]


class GrabMenu(BaseModel):
    categories: List[GrabCategoryItem]


class GrabMerchantResponse(BaseModel):
    ID: str
    name: str
    photoHref: str
    menu: GrabMenu
