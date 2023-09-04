from typing import List, Optional

from fastapi import HTTPException
from mongoengine import NotUniqueError, ValidationError, DoesNotExist
from starlette import status

from app.orderdnu.user.user_document import UserDocument
from app.orderdnu.user.user_model import User


class UserService:
    async def create_user(self, username: str, password: str, full_name: str) -> User:
        try:
            new_user = UserDocument(username=username, password=password, full_name=full_name)
            new_user.save()
            return User.model_validate({"id": str(new_user.id), **new_user.to_mongo()})
        except NotUniqueError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")

    async def get_user_by_id(self, user_id: str) -> User:
        try:
            user = UserDocument.objects.get(id=user_id)
            return User.model_validate({"id": str(user.id), **user.to_mongo()})
        except ValidationError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except DoesNotExist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    async def get_user_by_user_name(self, user_name: str) -> User:
        try:
            user = UserDocument.objects(user_name=user_name).first()
            return User.model_validate({"id": str(user.id), **user.to_mongo()})
        except ValidationError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except DoesNotExist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    async def update_user(self, user_id: str, username: Optional[str], password: Optional[str],
                          full_name: Optional[str]) -> User:
        try:
            user = await self.get_user_by_id(user_id)
            if username:
                user.username = username
            if password:
                user.password = password
            if full_name:
                user.full_name = full_name
            UserDocument(**dict(user)).save()
            return user
        except NotUniqueError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")

    async def delete_user(self, user_id: str) -> None:
        try:
            UserDocument.objects.get(id=user_id).delete()
        except ValidationError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except DoesNotExist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    async def get_users(self, skip: int = 0, limit: int = 10) -> List[User]:
        users = UserDocument.objects.skip(skip).limit(limit)
        return [User.model_validate({"id": str(user.id), **user.to_mongo()}) for user in users]
