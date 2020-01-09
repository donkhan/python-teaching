def factorial(n):
    product = 1
    for i in range(2,n+1):
        product = product * i
    return product

print(factorial(5))

#5c2

print(factorial(5)//(factorial(3)*factorial(2)))

