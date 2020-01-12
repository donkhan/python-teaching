
import numpy as np

a = np.arange(6)
print(a.ndim)

b = np.arange(12).reshape(4,3)
print(b)

c = np.arange(24).reshape(2,3,4)
print(c)


z = np.linspace(2,3,2)
print(z)

a = np.arange(1,10)
b = np.arange(2,10)

print(a)
print(b)
print(np.concatenate([a,b]))