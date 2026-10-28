from banking import account, transaction, loan

acc = account.create_account("Ravi", 5000)
transaction.deposit(acc, 2000)
transaction.withdraw(acc, 1000)

print("Account:", acc["name"])
print("Balance:", account.get_balance(acc))
print("Monthly EMI:", loan.calculate_emi(100000, 8, 5))
