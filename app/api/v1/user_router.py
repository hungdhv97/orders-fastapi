from typing import List

from fastapi import APIRouter, HTTPException
from mongoengine import NotUniqueError
from starlette import status

from app.documents.user_document import User
from app.models.user_model import UserResponse, CreateUserRequest, UpdateUserRequest

router = APIRouter()


@router.post("/user/", response_model=UserResponse)
async def create_user(user: CreateUserRequest) -> UserResponse:
    try:
        new_user = User(**user.model_dump())
        new_user.save()
        return UserResponse(id=str(new_user.id), **user.model_dump())
    except NotUniqueError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")


@router.get("/user/{user_id}", response_model=UserResponse)
async def get_user(user_id: str) -> UserResponse:
    user = User.objects(id=user_id).first()
    if user:
        return UserResponse(id=str(user.id), **user.to_mongo())
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@router.put("/user/{user_id}", response_model=UserResponse)
async def update_user(user_id: str, user_update: UpdateUserRequest) -> UserResponse:
    user = User.objects(id=user_id).first()
    if user:
        for attr, value in user_update.model_dump().items():
            if value is not None:
                setattr(user, attr, value)
        user.save()
        return UserResponse(id=str(user.id), **user.to_mongo())
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@router.delete("/user/{user_id}", response_model=dict)
async def delete_user(user_id: str):
    user = User.objects(id=user_id).first()
    if user:
        user.delete()
        return {"message": "User deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@router.get("/users/", response_model=List[UserResponse])
async def get_users(skip: int = 0, limit: int = 10) -> List[UserResponse]:
    users = User.objects.skip(skip).limit(limit)
    return [UserResponse(id=str(user.id), **user.to_mongo()) for user in users]
