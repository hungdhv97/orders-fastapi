from typing import List, Annotated

from fastapi import APIRouter, Path, Body

from app.orderdnu.user.openapi_examples import CREATE_USER_EXAMPLES, UPDATE_USER_EXAMPLES
from app.orderdnu.user.user_model import UserResponse, CreateUserRequest, UpdateUserRequest
from app.orderdnu.user.user_service import UserService

router = APIRouter()
user_service = UserService()

UserNamePath = Annotated[str, Path(example="nghia.nguyen4")]
UserIdPath = Annotated[str, Path(example="64f6318231e3ac649c61d2e8")]
CreateUserRequestBody = Annotated[CreateUserRequest, Body(openapi_examples=CREATE_USER_EXAMPLES)]
UpdateUserRequestBody = Annotated[UpdateUserRequest, Body(openapi_examples=UPDATE_USER_EXAMPLES)]


@router.post("/", response_model=UserResponse)
async def create_user(create_user_request: CreateUserRequestBody) -> UserResponse:
    new_user = await user_service.create_user(create_user_request.username, create_user_request.password,
                                              create_user_request.full_name)
    return UserResponse.model_validate(new_user.model_dump())


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: UserIdPath) -> UserResponse:
    user = await user_service.get_user_by_id(user_id)
    return UserResponse.model_validate(user.model_dump())


@router.get("/username/{username}", response_model=UserResponse)
async def get_user(username: UserNamePath) -> UserResponse:
    user = await user_service.get_user_by_username(username)
    return UserResponse.model_validate(user.model_dump())


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: UserIdPath,
                      update_user_request: UpdateUserRequestBody) -> UserResponse:
    user = await user_service.update_user(user_id, update_user_request.username, update_user_request.password,
                                          update_user_request.full_name)
    return UserResponse.model_validate(user.model_dump())


@router.delete("/{user_id}", response_model=dict)
async def delete_user(user_id: UserIdPath) -> dict:
    await user_service.delete_user(user_id)
    return {"message": "User deleted"}


@router.get("/", response_model=List[UserResponse])
async def get_users(skip: int = 0, limit: int = 10) -> List[UserResponse]:
    users = await user_service.get_users(skip, limit)
    return [UserResponse.model_validate(user.model_dump()) for user in users]


@router.get("/{merchant_id}", response_model=Any)
async def get_merchant_by_id(merchant_id: Annotated[str, Path(example="5-C3C2T8MUVN4HLT")]) -> Any:
    merchant_data = await merchant_service.get_grab_merchant_by_id_full_detail(merchant_id)
    return merchant_data
