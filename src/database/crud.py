from sqlalchemy import select
from sqlalchemy.orm import Session

from database.products import Product


def get_product_by_id(db: Session, product_id: int):
    return db.scalars(select(Product).where(Product.id == product_id)).first()

