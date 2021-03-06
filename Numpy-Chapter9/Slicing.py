import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(a[1,1])

print(a[:,1])


a3 = np.array([[[10, 11, 12], [13, 14, 15], [16, 17, 18]],
               [[20, 21, 22], [23, 24, 25], [26, 27, 28]],
               [[30, 31, 32], [33, 34, 35], [36, 37, 38]]])

print(a3[2, 0, 1])


print(a3[:, 1])


print(a3[1,:,:])


print(a3[:,:,2])
print(a3[-1,:,:])

print("Try copy...")
b3 = np.copy(a3,0)
print(b3)


print(np.full((3,3),True,dtype = bool))

