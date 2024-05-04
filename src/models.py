from datetime import datetime, timezone
from decimal import Decimal
from typing import List

from sqlalchemy import String, ForeignKey, DECIMAL, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.config import Base


class User(Base):
    __tablename__ = 'users_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))
    phone: Mapped[str] = mapped_column(String(30))


class Category(Base):
    __tablename__ = 'categories_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    category_title: Mapped[str]
    subcategories: Mapped[List['Subcategory']] = relationship(back_populates='parent')
    products: Mapped[List['Product']] = relationship(back_populates='category')

    def __repr__(self):
        return self.category_title


class Subcategory(Base):
    __tablename__ = 'subcategories_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    subcategory_title: Mapped[str] = mapped_column(String)
    parent_id: Mapped[int] = mapped_column(ForeignKey('categories_table.id', ondelete='CASCADE'))
    parent: Mapped['Category'] = relationship(back_populates='subcategories')
    products: Mapped[List['Product']] = relationship(back_populates='subcategory')

    def __repr__(self):
        return self.subcategory_title


class Product(Base):
    __tablename__ = 'products_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    product_title: Mapped[str]
    price: Mapped[Decimal] = mapped_column(DECIMAL(10, 2))
    discount_price: Mapped[Decimal] = mapped_column(DECIMAL(10, 2))
    product_balance: Mapped[int]
    product_characteristics: Mapped[str] = mapped_column(Text)
    category_id: Mapped[int] = mapped_column(ForeignKey('categories_table.id', ondelete='CASCADE'))
    category: Mapped['Category'] = relationship(back_populates='products')
    subcategory_id: Mapped[int | None] = mapped_column(ForeignKey('subcategories_table.id', ondelete='CASCADE'))
    subcategory: Mapped[Subcategory | None] = relationship(back_populates='products')

    def __repr__(self):
        return self.product_title
