from datetime import timedelta, datetime, timezone
from typing import Annotated

from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.orm import Session

from auth.schemas import TokenData
from auth.views import oauth2_scheme
from database.config import get_db
from database.users import User

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def get_user(username: str, db: Session = Depends(get_db)):
    return db.scalars(select(User).where(User.username == username)).first()


def authenticate_user(username: str, password: str, db: Session = Depends(get_db)):
    user = get_user(username=username, db=db)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False

    return user


def create_access_token(data: dict, expire_period: timedelta):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expire_period
    to_encode.update({'expire': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('user')
        if username is None:
            raise exception
        token_data = TokenData(username=username)
    except JWTError:
        raise exception
    user = get_user(username=username, db=db)
    if user is None:
        raise exception
    return user


