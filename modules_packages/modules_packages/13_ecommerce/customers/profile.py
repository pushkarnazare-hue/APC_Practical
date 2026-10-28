def get_customer(customers, customer_id):
    for c in customers:
        if c["id"] == customer_id:
            return c
    return None
