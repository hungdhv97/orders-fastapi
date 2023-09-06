from pydantic import BaseModel

from app.common.annotation.model_fields import UserNameField, PasswordField, FullNameField, ObjectIdField, \
    OptionalUserNameField, OptionalPasswordField, OptionalFullNameField


class CreateUserRequest(BaseModel):
    username: UserNameField
    password: PasswordField
    full_name: FullNameField


class UserResponse(BaseModel):
    id: ObjectIdField
    username: UserNameField
    full_name: FullNameField


class UpdateUserRequest(BaseModel):
    username: OptionalUserNameField
    password: OptionalPasswordField
    full_name: OptionalFullNameField


class User(BaseModel):
    id: ObjectIdField
    username: UserNameField
    password: PasswordField
    full_name: OptionalFullNameField
