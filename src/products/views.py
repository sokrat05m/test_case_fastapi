from fastapi import APIRouter, Depends
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from database.products import Product
from products.crud import get_product, get_products, get_products_by_category
from database.config import get_db
from products.schemas import ProductSchema, MinMaxSumSchema

product_router = APIRouter(prefix='/products')


@product_router.get("/", response_model=list[ProductSchema])
async def get_all_products(db: Session = Depends(get_db)):
    products = get_products(db)
    return products


@product_router.get("/min-max-sum", response_model=MinMaxSumSchema)
async def get_max_min_sum(db: Session = Depends(get_db)):
    min_price = func.min(Product.price).label('min_price')
    max_price = func.max(Product.price).label('max_price')
    total_balance_sum = func.sum(Product.price * Product.product_balance).label('total_balance_sum')
    result = db.execute(select(min_price, max_price, total_balance_sum)).first()
    return result


@product_router.get("/{product_id}", response_model=ProductSchema)
async def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    product = get_product(db=db, product_id=product_id)
    return product


@product_router.get("/category/{category_id}", response_model=list[ProductSchema])
async def get_products_by_category_id(category_id: int, db: Session = Depends(get_db)):
    products = get_products_by_category(db=db, category_id=category_id)
    return products
