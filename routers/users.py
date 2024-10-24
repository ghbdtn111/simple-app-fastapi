from pydantic import BaseModel
from fastapi import APIRouter, HTTPException

users = dict()


class User(BaseModel):
    email: str
    fio: str


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{email}")
async def get_user(email: str):
    try:
        user = users[email]
    except KeyError:
        raise HTTPException(404)
    return user


@router.post('/')
async def add_user(user: User):
    users[user.email] = user.fio
    return 'Пользователь добавлен'
