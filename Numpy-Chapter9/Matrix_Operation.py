import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

c = np.array([3,4])

print(a+b)
print(a-b)

print(a+c)
print(a-c)

print(a*b)

print("Matrix Multiplication " , a.dot(b))
