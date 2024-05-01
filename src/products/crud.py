from sqlalchemy import select
from sqlalchemy.orm import Session

from database.products import Product


def get_products(db: Session):
    return db.scalars(select(Product)).all()


def get_product(db: Session, product_id: int):
    return db.scalars(select(Product).where(Product.id == product_id)).first()


def get_products_by_category(db: Session, category_id: int):
    return db.scalars(select(Product).where(Product.category_id == category_id)).all()
