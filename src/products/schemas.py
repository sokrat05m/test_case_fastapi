from decimal import Decimal

from pydantic import BaseModel, Field


class ProductSchema(BaseModel):
    product_title: str
    price: float
    discount_price: float

    class Config:
        orm_mode = True


class MinMaxSumSchema(BaseModel):
    min_price: Decimal
    max_price: Decimal
    total_balance_sum: Decimal

    class Config:
        orm_mode = True
