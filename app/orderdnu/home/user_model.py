from typing import Optional

from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    username: str
    full_name: Optional[str] = None


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
