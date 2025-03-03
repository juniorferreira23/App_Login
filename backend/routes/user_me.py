from typing import Annotated
from fastapi import APIRouter, Depends
from models.user_model import Users
from core.auth import authenticate_token
from repositories.user_repo import get_user_by_username

router = APIRouter()

@router.get('/user/me')
def read_user_me(current_user: Annotated[Users, Depends(authenticate_token)]):
    user = get_user_by_username(current_user.username)
    return user