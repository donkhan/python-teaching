import numpy as np

a = np.arange(1,10)

print(np.sum(a))
print(np.max(a))
print(np.min(a))


d_2 = np.array([[1,2],[3,4],[5,6]])

print(np.sum(d_2,axis=0))
print(np.sum(d_2,axis=1))

print(np.max(d_2,axis=0))
print(np.max(d_2,axis=1))

