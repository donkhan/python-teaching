import numpy as np

a = np.zeros(5,dtype=int)
print(a)

print(np.invert(a))

a = np.array([1,1,0])
b = np.array([0,1,1])

print(np.bitwise_and(a,b))

print(np.bitwise_or(a,b))

print(np.binary_repr(3, width=4))
# 3 =  0011
# -3 = 1011
# 1's complement = 1100
# 2's complement = 1101
print(np.binary_repr(-3, width=4))


print(np.binary_repr(7,width=4))
print(np.binary_repr(-7,width=4))


np.bartlett()