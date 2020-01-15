import numpy as np


data = np.array([5,2,7,3,9])

print(data[:])
print(data[1:3])
print(data[:2])
print(data[-2:])

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
b = a[1:2,0:4]
print('b',b)

c = a[:2,0:2]
print('c',c)

d = a[:2,1:3]
print('d',d)

e = a[1:3,2:4]
print('e',e)

data = np.array([[1,2],[3,4]])
print('data before change ',data)
f = data[1:]
print('f',f)
f[0][1] = 12
print('f after change ',f)
print('data after change ',data)

data = np.array([[1,2],[3,4]])
print('data before change ',data)
f = np.copy(data[1:])
print('f before change ',f)
f[0][1] = 12
print('f after change ',f)
print('data after change ',data)

# Reshape

A = np.array([1,2,3,4,5,6])
B = np.reshape(A,(2,3))

print('Before Change A',A)
print('After Change B',B)

B[0][0] = 100
print('After Change A',A)
print('After B',B)











