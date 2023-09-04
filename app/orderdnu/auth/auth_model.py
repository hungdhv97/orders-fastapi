from pydantic import BaseModel

from app.orderdnu.user.user_model import UserNameField, PasswordField, FullNameField


class LoginRequest(BaseModel):
    username: UserNameField
    password: PasswordField


class RegisterRequest(BaseModel):
    username: UserNameField
    password: PasswordField
    full_name: FullNameField
