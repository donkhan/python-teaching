import numpy as np

print(np.version.version)

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)

print(np.fliplr(a))

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.flipud(a))

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("90 degree Rotation ",np.rot90(a,1))



