from sqlalchemy import select, func
from sqlalchemy.orm import Session

from database.products import Product


def get_products(db: Session):
    return db.scalars(select(Product)).all()


def get_product(db: Session, product_id: int):
    return db.scalars(select(Product).where(Product.id == product_id)).first()


def get_products_by_category(db: Session, category_id: int):
    return db.scalars(select(Product).where(Product.category_id == category_id)).all()


def min_max_sum(db: Session):
    min_price = func.min(Product.price).label('min_price')
    max_price = func.max(Product.price).label('max_price')
    total_balance_sum = func.sum(Product.price * Product.product_balance).label('total_balance_sum')
    return db.execute(select(min_price, max_price, total_balance_sum)).first()