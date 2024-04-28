from typing import List

from sqlalchemy import String, Float, Integer, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


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
    price: Mapped[float]
    discount_price: Mapped[float]
    product_balance: Mapped[int]
    product_characteristics: Mapped[str] = mapped_column(Text)
    category_id: Mapped[int] = mapped_column(ForeignKey('categories_table.id', ondelete='CASCADE'))
    category: Mapped['Category'] = relationship(back_populates='products')
    subcategory_id: Mapped[int] = mapped_column(ForeignKey('subcategories_table.id', ondelete='CASCADE'))
    subcategory: Mapped['Subcategory'] = relationship(back_populates='products')

    def __repr__(self):
        return self.product_title
