from passlib.context import CryptContext
from typing import Union
from datetime import datetime, timedelta
from jose import jwt

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def hash_password(password) -> str:
    return pwd_context.hash(password)


def verify_paasword(password, hash) -> bool:
    return pwd_context.verify(password, hash)


SECRET_KEY = '123445'
ALGORITHM = 'HS256'


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=1)

    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    return jwt.decode(token, SECRET_KEY)
