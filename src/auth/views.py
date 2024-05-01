from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from auth.schemas import Token
from auth.service import authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from database.config import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login')
auth_router = APIRouter(prefix="/login")


@auth_router.get('/')
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)) -> Token:
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={'user': user.username}, expire_period=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")
