
def inner(n):
    s = 0
    for i in range(1,n+1):
        s = s + i
    return s


def outer(n):
    s = 0
    for i in range(1,n+1):
        s += inner(i)
    return s


print(outer(5))

