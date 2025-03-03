from fastapi import APIRouter, HTTPException, status
from schemas.register_schema import RegisterSchema
from utils.validators import validate_register
from repositories.user_repo import get_user_by_username
from core.security import get_password_hash
from models.user_model import Users, db

router = APIRouter()

@router.post('/register')
async def register_user(data: RegisterSchema) -> dict:
    validator = validate_register(data.full_name, data.username, data.password, data.re_password)
    if validator:
        raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=validator
    )
    exists_username = get_user_by_username(data.username)
    if exists_username:
        raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail='Email already exists'
    )
    hash_pwd = get_password_hash(data.password)
    user = Users(full_name=data.full_name ,username=data.username, password=hash_pwd)
    db.session.add(user)
    db.session.commit()
    return {'message': 'Users registered successfully'}
