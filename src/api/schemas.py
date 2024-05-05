from decimal import Decimal
from typing import List

from pydantic import BaseModel, Field, EmailStr


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


class ProductSchema(BaseModel):
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


class CartSchema(BaseModel):
    user_id: int
    products: List['CartItemBaseSchema']
