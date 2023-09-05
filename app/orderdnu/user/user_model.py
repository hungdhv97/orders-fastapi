from typing import Optional, Annotated

from pydantic import BaseModel, Field

ObjectIdField = Annotated[str, Field(examples=["64f6318231e3ac649c61d2e8"])]
UserNameField = Annotated[str, Field(examples=["nghia.nguyen4"])]
PasswordField = Annotated[str, Field(examples=["1234"])]
FullNameField = Annotated[str, Field(examples=["Nguyễn Bá Nghĩa"])]

OptionalUserNameField = Annotated[Optional[str], Field(default=None, examples=["nghia.nguyen4"])]
OptionalPasswordField = Annotated[Optional[str], Field(default=None, examples=["1234"])]
OptionalFullNameField = Annotated[Optional[str], Field(default=None, examples=["Nguyễn Bá Nghĩa"])]


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
