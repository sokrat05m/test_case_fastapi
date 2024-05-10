from decimal import Decimal
from typing import List

from pydantic import BaseModel, Field, EmailStr


class UserBaseSchema(BaseModel):
    username: str = Field(min_length=4, max_length=30)
    first_name: str
    last_name: str
    email: EmailStr


class UserCreateSchema(UserBaseSchema):
    password: str = Field(min_length=5)
    phone: str

    class Config:
        orm_mode = True


class TokenBaseSchema(BaseModel):
    access_token: str
    token_type: str


class ProductBaseSchema(BaseModel):
    product_title: str
    price: Decimal = Field(gt=0)
    discount_price: Decimal = Field(gt=0)

    class Config:
        orm_mode = True


class MinMaxSumSchema(BaseModel):
    min_price: Decimal
    max_price: Decimal
    total_balance_sum: Decimal


class CartItemBaseSchema(BaseModel):
    product_id: int
    quantity: int


class CartBaseSchema(BaseModel):
    user_id: int
    products: List['CartItemBaseSchema']
