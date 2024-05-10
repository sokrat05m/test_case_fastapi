from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm


from api.deps import SessionDep, CurrentUserDep
from api.schemas import TokenBaseSchema, UserCreateSchema, UserBaseSchema
from api.service import authenticate_user, get_user, create_user
from core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from core.tokenize import create_access_token

auth_router = APIRouter()


@auth_router.post('/login')
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: SessionDep) \
        -> TokenBaseSchema:
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = create_access_token(
        data={'sub': user.username}, expire_period=access_token_expires
    )

    return TokenBaseSchema(access_token=access_token, token_type="bearer")


@auth_router.post('/register')
async def register_user(user: UserCreateSchema, db: SessionDep):
    user_exists = get_user(username=user.username, db=db)
    if user_exists:
        raise HTTPException(status_code=400, detail="User already registered")

    create_user(user=user, db=db)
    return {"message": "user created successfully"}


@auth_router.get("/users/me/", response_model=UserBaseSchema)
async def read_users_me(current_user: CurrentUserDep):
    return current_user
