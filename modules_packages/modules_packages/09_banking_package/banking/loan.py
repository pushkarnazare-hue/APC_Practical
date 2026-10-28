def calculate_emi(principal, rate, years):
    monthly_rate = rate / (12 * 100)
    months = years * 12
    if monthly_rate == 0:
        return principal / months
    emi = principal * monthly_rate * (1 + monthly_rate) ** months
    emi /= ((1 + monthly_rate) ** months - 1)
    return emi
