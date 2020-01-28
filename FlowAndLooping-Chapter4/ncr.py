def factorial(n):
    product = 1
    for i in range(2,n+1):
        product = product * i
    return product


print(factorial(12)//(factorial(6)*factorial(6))/7)

