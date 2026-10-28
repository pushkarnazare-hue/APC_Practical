from products import catalog
from customers import registration, profile
from orders import cart, order_processing
from payments import payment, invoice

products = []
customers = []
orders = []
shopping_cart = []

catalog.add_product(products, 1, "Laptop", 50000)
registration.register_customer(customers, 1, "Ravi", "ravi@example.com")

cart.add_to_cart(shopping_cart, products[0], 1)
order = order_processing.place_order(orders, customers[0], shopping_cart)

payment.process_payment(order["total"])
invoice.generate_invoice(order)
