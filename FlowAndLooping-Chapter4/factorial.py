
def odd_even(n):
    # Mod
    if n % 2 == 0:
        return "Even"
    return "Odd"

def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n-1)


def factorial_loop(n):
    product = 1
    for i in range(1, n+1):
        product = product * i
    return product

# 1 + 2 + 3 + 4 + 5
def sum_of_n(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum


print(factorial_loop(5))
print(factorial_recursive(5))
print(sum_of_n(5))

