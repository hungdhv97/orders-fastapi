from fastapi import APIRouter

from app.common.annotation.fastapi_params import LoginRequestBody, RegisterRequestBody
from app.orderdnu.auth.auth_service import AuthService
from app.orderdnu.user.user_model import UserResponse
from app.orderdnu.user.user_service import UserService

router = APIRouter()

user_service = UserService()
auth_service = AuthService(user_service)


@router.post("/login", response_model=UserResponse)
async def login(login_request: LoginRequestBody) -> UserResponse:
    user = await auth_service.login(login_request.username, login_request.password)
    return UserResponse.model_validate(user.model_dump())


@router.post("/register", response_model=UserResponse)
async def register(register_request: RegisterRequestBody) -> UserResponse:
    user = await auth_service.register(register_request.username, register_request.password, register_request.full_name)
    return UserResponse.model_validate(user.model_dump())
