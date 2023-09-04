from typing import List, Optional

from fastapi import HTTPException
from mongoengine import NotUniqueError, ValidationError, DoesNotExist
from starlette import status

from app.orderdnu.user.user_document import UserDocument
from app.orderdnu.user.user_model import UserModel


class UserService:
    def create_user(self, username: str, full_name: Optional[str]) -> UserModel:
        try:
            new_user = UserDocument(username=username, full_name=full_name)
            new_user.save()
            return UserModel.model_validate({"id": str(new_user.id), **new_user.to_mongo()})
        except NotUniqueError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")

    def get_user(self, user_id: str) -> UserModel:
        try:
            user = UserDocument.objects.get(id=user_id)
            return UserModel.model_validate({"id": str(user.id), **user.to_mongo()})
        except ValidationError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except DoesNotExist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    def update_user(self, user_id: str, username: Optional[str], full_name: Optional[str]) -> UserModel:
        try:
            user = UserDocument.objects.get(id=user_id)
            if username:
                user.username = username
            if full_name:
                user.full_name = full_name
            user.save()
            return UserModel.model_validate({"id": str(user.id), **user.to_mongo()})
        except ValidationError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except DoesNotExist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        except NotUniqueError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")

    def delete_user(self, user_id: str) -> None:
        try:
            user = UserDocument.objects.get(id=user_id)
            user.delete()
        except ValidationError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except DoesNotExist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    def get_users(self, skip: int = 0, limit: int = 10) -> List[UserModel]:
        users = UserDocument.objects.skip(skip).limit(limit)
        return [UserModel.model_validate({"id": str(user.id), **user.to_mongo()}) for user in users]
