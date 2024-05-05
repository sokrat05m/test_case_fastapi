from sqladmin import ModelView

from models import Category, Subcategory, Product, User, Cart


class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.id, Category.category_title]


class SubcategoryAdmin(ModelView, model=Subcategory):
    column_list = [Subcategory.id, Subcategory.subcategory_title]


class ProductAdmin(ModelView, model=Product):
    column_list = [Product.id, Product.product_title]


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username]


class CartAdmin(ModelView, model=Cart):
    column_list = [Cart.id, Cart.user]

