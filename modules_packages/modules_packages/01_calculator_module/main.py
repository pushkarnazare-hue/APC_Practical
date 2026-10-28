import calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Choose operation: +  -  *  /")
op = input("Enter operation: ")

if op == "+":
    print("Result:", calculator.add(a, b))
elif op == "-":
    print("Result:", calculator.subtract(a, b))
elif op == "*":
    print("Result:", calculator.multiply(a, b))
elif op == "/":
    print("Result:", calculator.divide(a, b))
else:
    print("Invalid operation")
