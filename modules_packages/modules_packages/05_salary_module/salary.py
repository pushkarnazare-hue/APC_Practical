def gross_salary(basic, allowances):
    return basic + allowances

def deductions(gross, deduction_rate=0.1):
    return gross * deduction_rate

def net_salary(basic, allowances, deduction_rate=0.1):
    gross = gross_salary(basic, allowances)
    ded = deductions(gross, deduction_rate)
    return gross - ded
