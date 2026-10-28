def add_to_cart(cart, product, quantity):
    cart.append({"product": product, "quantity": quantity})

def cart_total(cart):
    return sum(item["product"]["price"] * item["quantity"] for item in cart)
