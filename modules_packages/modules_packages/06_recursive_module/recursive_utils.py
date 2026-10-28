def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci_series(n):
    series = []
    def fib(k):
        if k <= 1:
            return k
        return fib(k - 1) + fib(k - 2)
    for i in range(n):
        series.append(fib(i))
    return series

def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

def to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return to_binary(n // 2) + str(n % 2)
