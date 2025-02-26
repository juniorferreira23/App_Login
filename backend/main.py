from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from Validator import email_validator, password_validator
from Model import Users, db
from bcrypt import hashpw, gensalt, checkpw
from passlib.context import CryptContext


class Token(BaseModel):
    access_token: str
    token_type: str

class LoginSchema(BaseModel):
    email: str
    password: str
    
class RegisterSchema(LoginSchema):
    full_name: str
    re_password: str


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


@app.post('/register')
def register_user(data: RegisterSchema) -> dict:
    try:
        validator = email_validator(data.username)
        if validator:
            return {'message': validator}
        validator = password_validator(data.password, data.re_password)
        if validator:
            return {'message': validator}
        exists_email = db.session.query(Users).filter(Users.username == data.username).one_or_none()
        if exists_email:
            return {'message': 'Email already registered'}
        hash_pwd = hashpw(data.password.encode(), gensalt())
        user = Users(username=data.username, password=hash_pwd)
        db.session.add(user)
        db.session.commit()
        return {'message': 'Users registered successfully'}
    except Exception as e:
        return {'error': f'Error: Unable to save data: {e}'}


@app.post('/login')
def login(data: LoginSchema) -> dict:
    validator = email_validator(data.username)
    if validator:
        return {'message': validator}
    validator = password_validator(data.password)
    if validator:                
        return {'message': validator}
    user = db.session.query(Users).filter(Users.username == data.username).one_or_none()
    if not user:
        return {'message': 'Invalid Users'}
    if not checkpw(data.password.encode(), user.password.encode()):
        return {'message': 'Incorrect password'}
    
    ...