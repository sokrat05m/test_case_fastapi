from fastapi import FastAPI
from sqladmin import Admin, ModelView

from admin import CategoryAdmin, SubcategoryAdmin, ProductAdmin, UserAdmin
from auth.views import auth_router
from database.config import engine
from database.products import Category, Subcategory, Product
from products.views import product_router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(product_router)
    app.include_router(auth_router)
    return app


app = create_app()
admin = Admin(app, engine)
admin.add_view(CategoryAdmin)
admin.add_view(SubcategoryAdmin)
admin.add_view(ProductAdmin)
admin.add_view(UserAdmin)
