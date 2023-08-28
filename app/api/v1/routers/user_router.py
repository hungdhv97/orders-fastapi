from typing import List

import httpx
from fastapi import APIRouter

from app.models.user_model import UserResponse, CreateUserRequest, UpdateUserRequest
from app.services.user_service import UserService

router = APIRouter()
user_service = UserService()


@router.get("/fetch_merchant_data/")
async def fetch_merchant_data():
    url = "https://portal.grab.com/foodweb/v2/merchants/5-C3C2T8MUVN4HLT"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

    return response.json()


@router.post("/user/", response_model=UserResponse)
async def create_user(user: CreateUserRequest) -> UserResponse:
    new_user = user_service.create_user(user.username, user.full_name)
    return UserResponse(id=str(new_user.id), username=new_user.username, full_name=new_user.full_name)


@router.get("/user/{user_id}", response_model=UserResponse)
async def get_user(user_id: str) -> UserResponse:
    user = user_service.get_user(user_id)
    return UserResponse(id=str(user.id), username=user.username, full_name=user.full_name)


@router.put("/user/{user_id}", response_model=UserResponse)
async def update_user(user_id: str, user_update: UpdateUserRequest) -> UserResponse:
    user = user_service.update_user(user_id, user_update.username, user_update.full_name)
    return UserResponse(id=str(user.id), username=user.username, full_name=user.full_name)


@router.delete("/user/{user_id}", response_model=dict)
async def delete_user(user_id: str):
    user_service.delete_user(user_id)
    return {"message": "User deleted"}


@router.get("/users/", response_model=List[UserResponse])
async def get_users(skip: int = 0, limit: int = 10) -> List[UserResponse]:
    users = user_service.get_users(skip, limit)
    return [UserResponse(id=str(user.id), username=user.username, full_name=user.full_name) for user in users]
