from fastapi import APIRouter

from app.models.user import User

router = APIRouter()


@router.get("/")
def read_root():
    return [{**user.to_mongo(), "_id": str(user.id)} for user in User.objects]
