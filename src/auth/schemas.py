from pydantic import BaseModel, EmailStr, field_validator


class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: EmailStr


class UserInDB(UserBase):
    password: str
    phone: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
