import os
from dotenv import load_dotenv
from typing import Annotated
from datetime import datetime, timedelta, timezone

import jwt
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from Validator import email_validator, password_validator
from Model import Users, db
# from bcrypt import hashpw, gensalt, checkpw
from passlib.context import CryptContext
from jwt.exceptions import InvalidTokenError

load_dotenv()


class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: str

class RegisterSchema(BaseModel):
    full_name: str
    username: str
    password: str
    re_password: str
    

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

origins = [
    'http://localhost:3000',
    'http://127.0.0.1:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv('SECRET_KEY'), algorithm=os.getenv('ALGORITHM'))
    return encoded_jwt

async def authenticate_token(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_expection = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Invalid username or password',
        headers={'WWW-Authenticate': 'Bearer'}
    )
    try:
        payload = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=os.getenv('ALGORITHM'))
        username = payload.get('sub')
        if not username:
            raise credentials_expection
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_expection
    user = db.session.query(Users).filter(Users.username == token_data.username).one_or_none()
    if not user:
        raise credentials_expection
    return user

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


@app.post('/register')
async def register_user(data: RegisterSchema) -> dict:
    try:
        validator = email_validator(data.username)
        if validator:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=validator
        )
        validator = password_validator(data.password, data.re_password)
        if validator:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=validator
        )
        exists_username = db.session.query(Users).filter(Users.username == data.username).one_or_none()
        if exists_username:
            raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Email already exists'
        )
        # hash_pwd = hashpw(data.password.encode(), gensalt())
        hash_pwd = get_password_hash(data.password)
        user = Users(full_name=data.full_name ,username=data.username, password=hash_pwd)
        db.session.add(user)
        db.session.commit()
        return {'message': 'Users registered successfully'}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Internal server error'
        )


@app.post('/token')
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    validator = email_validator(form_data.username)
    if validator:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=validator
        )
    validator = password_validator(form_data.password)
    if validator:                
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=validator
        )
    user = db.session.query(Users).filter(Users.username == form_data.username).one_or_none()
    # if not user or not checkpw(form_data.password.encode(), user.password.encode()):
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid username or password',
            headers={'WWW-Authenticate': 'Bearer'}
        )
    access_token_expires = timedelta(minutes=int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')))
    access_token = create_access_token(data={'sub': user.username}, expires_delta=access_token_expires)
    return Token(access_token=access_token, token_type='bearer')

@app.get('/users/me')
def read_user_me(current_user: Annotated[Users, Depends(authenticate_token)]):
    user = db.session.query(Users).filter(Users.username == current_user.username).one_or_none()
    return user