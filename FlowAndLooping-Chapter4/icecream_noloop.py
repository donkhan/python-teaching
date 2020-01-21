# combination_with_repetition

l = list()
print(l)
l.append(3)
l.append(4)
l.append('A')
print(l)

def cwr(n,r,l):
    c = 0
    for i in range(0,n+1):
        nl = list(l)
        nl.append(i)
        if r == 1:
            if sum(nl) == 10:
                print(nl)
                c = c + 1
        else:
            c = c + cwr(n, r - 1, nl)
    return c

print("Total Possibilities",cwr(10,2,list()))

'''
import itertools


l = list(itertools.combinations_with_replacement(['V','M',"C"],10))
print(l)
print(len(l))

'''