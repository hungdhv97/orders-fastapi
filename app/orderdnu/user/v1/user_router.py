from typing import List, Annotated

from fastapi import APIRouter, Path

from app.orderdnu.user.user_model import UserResponse, CreateUserRequest, UpdateUserRequest
from app.orderdnu.user.user_service import UserService

router = APIRouter()
user_service = UserService()


@router.post("/", response_model=UserResponse)
async def create_user(user: CreateUserRequest) -> UserResponse:
    new_user = await user_service.create_user(user.username, user.password, user.full_name)
    return UserResponse.model_validate(new_user.model_dump())


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: Annotated[str, Path(example="64f56d85faf1cf89b48f3c5f")]) -> UserResponse:
    user = await user_service.get_user_by_id(user_id)
    return UserResponse.model_validate(user.model_dump())


@router.get("/{username}", response_model=UserResponse)
async def get_user(username: Annotated[str, Path(example="nghia.nguyen4")]) -> UserResponse:
    user = await user_service.get_user_by_username(username)
    return UserResponse.model_validate(user.model_dump())


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: Annotated[str, Path(example="64f56d85faf1cf89b48f3c5f")],
                      user_update: UpdateUserRequest) -> UserResponse:
    user = await user_service.update_user(user_id, user_update.username, user_update.full_name)
    return UserResponse.model_validate(user.model_dump())


@router.delete("/{user_id}", response_model=dict)
async def delete_user(user_id: Annotated[str, Path(example="64f56d85faf1cf89b48f3c5f")]) -> dict:
    await user_service.delete_user(user_id)
    return {"message": "User deleted"}


@router.get("/", response_model=List[UserResponse])
async def get_users(skip: int = 0, limit: int = 10) -> List[UserResponse]:
    users = await user_service.get_users(skip, limit)
    return [UserResponse.model_validate(user.model_dump()) for user in users]
