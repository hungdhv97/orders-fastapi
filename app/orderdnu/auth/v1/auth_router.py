from typing import Annotated

from fastapi import APIRouter, Body

from app.orderdnu.auth.auth_model import LoginRequest, RegisterRequest
from app.orderdnu.auth.auth_service import HomeService
from app.orderdnu.user.user_model import UserResponse

router = APIRouter()
home_service = HomeService()


@router.post("/login", response_model=UserResponse)
async def login(
        login_request: Annotated[
            LoginRequest,
            Body(
                openapi_examples={
                    "success": {
                        "summary": "Login Nghia account",
                        "value": {
                            "username": "nghia.nguyen4",
                            "password": "1234",
                        }
                    },
                    "wrong_password": {
                        "summary": "Login Nghia wrong password",
                        "value": {
                            "username": "nghia.nguyen4",
                            "password": "wrong_password",
                        }
                    },
                    "non_exist": {
                        "summary": "Login non-exist account",
                        "value": {
                            "username": "non-exist",
                            "password": "1234",
                        }
                    },
                },
            ),
        ]) -> UserResponse:
    user = await home_service.login(login_request.username, login_request.password)
    return UserResponse.model_validate(user.model_dump())


@router.post("/register", response_model=UserResponse)
async def register(
        register_request: Annotated[
            RegisterRequest,
            Body(
                openapi_examples={
                    "account1": {
                        "summary": "Register Nghia account",
                        "value": {
                            "username": "nghia.nguyen4",
                            "password": "1234",
                            "full_name": "Nguyễn Bá Nghĩa",
                        }
                    },
                    "account2": {
                        "summary": "Register Hung account",
                        "value": {
                            "username": "hung.thai",
                            "password": "1234",
                            "full_name": "Thái Doãn Hùng",
                        }
                    },
                    "account3": {
                        "summary": "Register Nam account",
                        "value": {
                            "username": "nam.nguyen12",
                            "password": "1234",
                            "full_name": "Nguyễn Văn Nam",
                        }
                    },
                },
            ),
        ]) -> UserResponse:
    user = await home_service.register(register_request.username, register_request.password, register_request.full_name)
    return UserResponse.model_validate(user.model_dump())
