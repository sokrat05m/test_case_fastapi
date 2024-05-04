

from fastapi import APIRouter


from api.deps import SessionDep
from api.schemas import ProductSchema, MinMaxSumSchema
from api.service import get_products, min_max_sum, get_product, get_products_by_category

product_router = APIRouter(prefix='/products')


@product_router.get("/", response_model=list[ProductSchema])
async def get_all_products(db: SessionDep):
    products = get_products(db)
    return products


@product_router.get("/min-max-sum", response_model=MinMaxSumSchema)
async def get_max_min_sum(db: SessionDep):
    result = min_max_sum(db=db)
    return result


@product_router.get("/{product_id}", response_model=ProductSchema)
async def get_product_by_id(product_id: int, db: SessionDep):
    product = get_product(db=db, product_id=product_id)
    return product


@product_router.get("/category/{category_id}", response_model=list[ProductSchema])
async def get_products_by_category_id(category_id: int, db: SessionDep):
    products = get_products_by_category(db=db, category_id=category_id)
    return products
