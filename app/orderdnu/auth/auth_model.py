from pydantic import BaseModel

from app.common.annotation.model_fields import UserNameField, PasswordField, FullNameField


class LoginRequest(BaseModel):
    username: UserNameField
    password: PasswordField


class RegisterRequest(BaseModel):
    username: UserNameField
    password: PasswordField
    full_name: FullNameField
