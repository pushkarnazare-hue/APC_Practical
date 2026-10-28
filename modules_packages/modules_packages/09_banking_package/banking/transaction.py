def deposit(account, amount):
    account["balance"] += amount
    return account["balance"]

def withdraw(account, amount):
    if amount > account["balance"]:
        return "Insufficient balance"
    account["balance"] -= amount
    return account["balance"]
