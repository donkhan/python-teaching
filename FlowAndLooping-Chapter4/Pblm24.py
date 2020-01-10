n = 5

def print_inner_star(n):
    for i in range(1,n+1):
        print('*',end=' ')
    print()


def print_outer(n):
    for i in range(1,n+1):
        print_inner_star(i)

def print_using_loops(n):
    for i in range(1,n+1):
        for j in range(1, i + 1):
            print('*', end=' ')
        print()


print_using_loops(5)
#print_inner_star(5)

#print("Sana",end=" like chicken pizza ")
#print("Vinny")
