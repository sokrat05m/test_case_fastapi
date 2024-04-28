from pydantic import BaseModel


class ProductSchema(BaseModel):
    product_title: str
    price: float
    discount_price: float

    class Config:
        orm_mode = True
