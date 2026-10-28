def create_account(name, initial_balance=0):
    return {"name": name, "balance": initial_balance}

def get_balance(account):
    return account["balance"]
