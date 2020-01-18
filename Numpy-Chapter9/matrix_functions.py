import numpy as np

x = np.array([[1,2],[3,4]],dtype=int)

print(np.linalg.det(x))
print(x)
inv = np.linalg.inv(x)
print(inv)

print(np.linalg.matrix_power(x,2))

# 1 2
# 3 4 = (1 * 4 - 2 * 3)

# 1 2  1 2 = 7 10
# 3 4  3 4