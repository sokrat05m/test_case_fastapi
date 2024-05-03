from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    username: str = Field(min_length=4, max_length=30)
    first_name: str
    last_name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(min_length=5)
    phone: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str




