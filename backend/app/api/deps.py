from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.core.config import SECRET_KEY, ALGORITHM
from app.schemas import TokenData
from jwt.exceptions import InvalidTokenError
from app.crud import get_user_by_username

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


async def authenticate_token(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_expection = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Invalid username or password',
        headers={'WWW-Authenticate': 'Bearer'}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username = payload.get('sub')
        if not username:
            raise credentials_expection
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_expection
    user = get_user_by_username(token_data.username)
    if not user:
        raise credentials_expection
    return user