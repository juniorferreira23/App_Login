from pydantic import BaseModel

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
