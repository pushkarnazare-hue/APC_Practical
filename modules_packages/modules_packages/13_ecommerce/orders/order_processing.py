def place_order(orders, customer, cart):
    order = {"customer": customer, "items": cart, "total": sum(i["product"]["price"] * i["quantity"] for i in cart)}
    orders.append(order)
    return order
