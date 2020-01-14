import numpy as np


print(np.__version__)

print np.version.version

a = np.arange(0,10)
print(a)

bool_array = np.full((3,3),True,dtype = bool)
print(bool_array)

odd = np.extract(a%2==1,a)
print(odd)

even = np.extract(a%2==0,a)
print(even)

b = np.copy(a)
b[b%2 == 1] = -1
print(a)
print(b)

a[a%2 == 0] = 1
print(a)

x = np.array([[2,3,4], [5,6,7]])
np.reshape(x, (3, 2))
print(x)


print(np.dot(np.arange(1,3),np.arange(1,3)))

print(np.product(np.arange(1,5)))
print(np.sum(np.arange(1,5)))

a = np.arange(1,21,2)
print(a)

a = np.arange(2,21,2)
print(a)





