import json

from fastapi import APIRouter

from app.models.user import User

router = APIRouter()


@router.get("/")
def read_root():
    return json.loads(User.objects.all().to_json())
