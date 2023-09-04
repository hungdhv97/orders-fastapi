from typing import Optional

from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    username: str
    password: str
    full_name: str


class UserResponse(BaseModel):
    id: str
    username: str
    full_name: Optional[str] = None


class UpdateUserRequest(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    full_name: Optional[str] = None


class User(BaseModel):
    id: str
    username: str
    password: str
    full_name: Optional[str] = None
