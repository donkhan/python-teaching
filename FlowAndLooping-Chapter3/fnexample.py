
def fib(n):
    i = -1
    j = 1
    count = 2
    print(i)
    print(j)
    while count < n:
        i,j = j,i+j
        print(i)
        count = count + 1


fib(10)