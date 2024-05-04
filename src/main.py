from fastapi import FastAPI
from sqladmin import Admin

from admin import CategoryAdmin, SubcategoryAdmin, ProductAdmin, UserAdmin
from api.routes.login import auth_router
from core.config import engine
from api.routes.products import product_router


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
