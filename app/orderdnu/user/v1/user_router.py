from typing import List

from fastapi import APIRouter

from app.common.annotation.fastapi_params import CreateUserRequestBody, ObjectIdPath, UserNamePath, \
    UpdateUserRequestBody
from app.orderdnu.user.user_model import UserResponse
from app.orderdnu.user.user_service import UserService

router = APIRouter()
user_service = UserService()


@router.post("/", response_model=UserResponse)
async def create_user(create_user_request: CreateUserRequestBody) -> UserResponse:
    new_user = await user_service.create_user(create_user_request.username, create_user_request.password,
                                              create_user_request.full_name)
    return UserResponse.model_validate(new_user.model_dump())


@router.get("/", response_model=List[UserResponse])
async def get_users(skip: int = 0, limit: int = 10) -> List[UserResponse]:
    users = await user_service.get_users(skip, limit)
    return [UserResponse.model_validate(user.model_dump()) for user in users]


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: ObjectIdPath) -> UserResponse:
    user = await user_service.get_user_by_id(user_id)
    return UserResponse.model_validate(user.model_dump())


@router.get("/username/{username}", response_model=UserResponse)
async def get_user(username: UserNamePath) -> UserResponse:
    user = await user_service.get_user_by_username(username)
    return UserResponse.model_validate(user.model_dump())


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: ObjectIdPath,
                      update_user_request: UpdateUserRequestBody) -> UserResponse:
    user = await user_service.update_user(user_id, update_user_request.username, update_user_request.password,
                                          update_user_request.full_name)
    return UserResponse.model_validate(user.model_dump())


@router.delete("/{user_id}", response_model=dict)
async def delete_user(user_id: ObjectIdPath) -> dict:
    await user_service.delete_user(user_id)
    return {"message": "User deleted"}
