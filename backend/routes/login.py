from typing import Annotated
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from schemas.token_schema import Token
from utils.validators import validate_credentials
from repositories.user_repo import get_user_by_username
from core.security import verify_password
from config import ACCESS_TOKEN_EXPIRE_MINUTES
from core.auth import create_access_token

router = APIRouter()

@router.post('/token')
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    validator = validate_credentials(form_data.username, form_data.password)
    if validator:
        raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=validator
    )
    user = get_user_by_username(form_data.username)
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid username or password',
            headers={'WWW-Authenticate': 'Bearer'}
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={'sub': user.username}, expires_delta=access_token_expires)
    return Token(access_token=access_token, token_type='bearer')