from typing import List, Optional

from fastapi import HTTPException
from mongoengine import NotUniqueError, ValidationError, DoesNotExist
from starlette import status

from app.documents.user_document import User


class UserService:
    def create_user(self, username: str, full_name: Optional[str]) -> User:
        try:
            new_user = User(username=username, full_name=full_name)
            new_user.save()
            return new_user
        except NotUniqueError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")

    def get_user(self, user_id: str) -> User:
        try:
            user = User.objects.get(id=user_id)
            return user
        except ValidationError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except DoesNotExist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    def update_user(self, user_id: str, username: Optional[str], full_name: Optional[str]) -> User:
        try:
            user = self.get_user(user_id)
            if username:
                user.username = username
            if full_name:
                user.full_name = full_name
            user.save()
            return user
        except NotUniqueError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")

    def delete_user(self, user_id: str):
        try:
            user = self.get_user(user_id)
            user.delete()
        except DoesNotExist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    def get_users(self, skip: int = 0, limit: int = 10) -> List[User]:
        users = User.objects.skip(skip).limit(limit)
        return users
