import salary

basic = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))

gross = salary.gross_salary(basic, allowances)
ded = salary.deductions(gross)
net = salary.net_salary(basic, allowances)

print("Gross salary:", gross)
print("Deductions:", ded)
print("Net salary:", net)
