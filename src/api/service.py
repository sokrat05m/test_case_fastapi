from sqlalchemy import select, func, and_, update
from sqlalchemy.orm import Session

from api.schemas import UserCreate

from core.tokenize import hash_password, verify_password
from models import Product, User, Cart, CartItem


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


def create_user_cart(user: User, db: Session):
    db_cart = Cart(user_id=user.id)
    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)
    return db_cart


def create_cart_item(cart_id: int, product_id: int, quantity: int, db: Session):
    db_cart_item = CartItem(cart_id=cart_id, product_id=product_id, quantity=quantity)
    db.add(db_cart_item)
    db.commit()
    db.refresh(db_cart_item)
    return db_cart_item


def update_cart_item_quantity(cart_id: int, product_id: int, quantity: int, db: Session):
    stmt = (update(CartItem).where(and_(CartItem.product_id == product_id, CartItem.cart_id == cart_id))
            .values(quantity=CartItem.quantity + quantity))
    db.execute(stmt)
    db.commit()

