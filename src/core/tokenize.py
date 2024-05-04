from datetime import datetime, timezone, timedelta

from jose import jwt
from passlib.context import CryptContext

from core.config import SECRET_KEY, ALGORITHM

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(data: dict, expire_period: timedelta) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expire_period
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
