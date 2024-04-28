from fastapi import FastAPI, Depends
from sqladmin import Admin, ModelView
from sqlalchemy.orm import Session

from database.crud import get_product_by_id
from database.database import engine, get_db
from database.products import Category, Subcategory, Product
from database.schemas import ProductSchema

app = FastAPI()

admin = Admin(app, engine)


class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.id, Category.category_title]


class SubcategoryAdmin(ModelView, model=Subcategory):
    column_list = [Subcategory.id, Subcategory.subcategory_title]


class ProductAdmin(ModelView, model=Product):
    column_list = [Product.id, Product.product_title]


admin.add_view(CategoryAdmin)
admin.add_view(SubcategoryAdmin)
admin.add_view(ProductAdmin)


@app.get("/products/{product_id}", response_model=ProductSchema)
async def get_product(product_id: int, db: Session = Depends(get_db)):
    product = get_product_by_id(db=db, product_id=product_id)
    return product

