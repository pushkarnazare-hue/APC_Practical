def generate_invoice(order):
    print("----- INVOICE -----")
    for item in order["items"]:
        print(item["product"]["name"], "x", item["quantity"])
    print("Total:", order["total"])
