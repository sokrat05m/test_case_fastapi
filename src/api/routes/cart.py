from fastapi import APIRouter

from api.deps import CurrentUserDep, SessionDep
from api.schemas import CartItemBaseSchema, CartSchema
from api.service import create_user_cart, create_cart_item, update_cart_item_quantity

cart_router = APIRouter()


@cart_router.post("/add-to-cart", response_model=CartSchema)
async def add_product_to_cart(cart_item: CartItemBaseSchema, user: CurrentUserDep, db: SessionDep):
    if user.cart:
        user_cart = user.cart
    else:
        user_cart = create_user_cart(user, db)

    for product in user_cart.products:
        if product.product_id == cart_item.product_id:
            update_cart_item_quantity(cart_id=user_cart.id, product_id=cart_item.product_id,
                                      quantity=cart_item.quantity, db=db)
            break
    else:
        item = create_cart_item(cart_id=user_cart.id, product_id=cart_item.product_id,
                                quantity=cart_item.quantity, db=db)
        user_cart.products.append(item)

    return user_cart
