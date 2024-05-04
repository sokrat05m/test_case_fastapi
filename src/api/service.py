
from sqlalchemy import select, func
from sqlalchemy.orm import Session


from schemas import UserCreate

from src.models import User, Product
from core.tokenize import hash_password, verify_password


def get_user(username: str, db: Session):
    return db.scalars(select(User).where(User.username == username)).first()


def create_user(user: UserCreate, db: Session):
    hashed_password = hash_password(user.password)
    user.password = hashed_password
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(username: str, password: str, db: Session):
    user = get_user(username=username, db=db)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False

    return user


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
