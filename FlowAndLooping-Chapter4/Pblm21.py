import math

x = 5
n = 3
s = 0

for i in range(0,n+1):
    p = pow(x,i)
    f = math.factorial(i+1)
    s = pow(-1,i)
    t =  p*s / f
    print(p, f, s,t)
    s += t

print(s)