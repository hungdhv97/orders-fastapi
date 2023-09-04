from typing import Optional

from pydantic import BaseModel


class LoginRequest(BaseModel):
    username: str
    password: str


class SignUpRequest(BaseModel):
    username: str
    password: str
    full_name: str

class UserResponse(BaseModel):
    id: str
    username: str
    full_name: Optional[str] = None


class UpdateUserRequest(BaseModel):
    username: Optional[str] = None
    full_name: Optional[str] = None


class User(BaseModel):
    id: str
    username: str
    full_name: Optional[str] = None
