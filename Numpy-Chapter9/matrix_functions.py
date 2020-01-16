import numpy as np

x = np.array([[1,2],[3,4]],dtype=int)

print(np.linalg.det(x))
print(x)
inv = np.linalg.inv(x)
print(inv)

print(np.linalg.matrix_power(x,2))

