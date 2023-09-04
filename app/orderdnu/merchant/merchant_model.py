from typing import List

from pydantic import BaseModel


class FoodItem(BaseModel):
    id: str
    name: str
    available: bool
    img_url: str
    description: str
    price: int


class CategoryItem(BaseModel):
    id: str
    name: str
    available: bool
    items: List[FoodItem]


class Menu(BaseModel):
    categories: List[CategoryItem]


class MerchantResponse(BaseModel):
    id: str
    name: str
    photo_url: str
    menu: Menu
