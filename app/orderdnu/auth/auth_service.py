from fastapi import HTTPException
from mongoengine import NotUniqueError
from starlette import status

from app.orderdnu.user.user_document import UserDocument
from app.orderdnu.user.user_model import User
from app.orderdnu.user.user_service import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    async def login(self, username: str, password: str) -> User:
        user = await self.user_service.get_user_by_username(username)
        if password != user.password:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Wrong password")
        return user

    async def register(self, username: str, password: str, full_name: str) -> User:
        try:
            new_user = UserDocument(username=username, password=password, full_name=full_name)
            new_user.save()
            return User.model_validate({"id": str(new_user.id), **new_user.to_mongo()})
        except NotUniqueError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")
