import numpy as np

# https://docs.scipy.org/doc/numpy/reference/routines.array-creation.html

a = np.arange(2.3,4.5,0.1)
print(a)
ar = np.array(([1,2],[3,4]))
print(ar)

print(np.linspace(0,100,21))

print(np.zeros((5)))
print(np.ones((3,5)))

print(np.full((3,3),False,dtype = bool))

print(np.fromstring("1,2,3,4,5,6,7",dtype=int,sep=","))

print(np.fromstring("1 2 3",dtype=int,sep=" "))

print(np.empty((1,4),dtype=int))


print(np.eye(2,dtype = int))

a = np.array([[3,1], [1,2]])
b = np.array([9,8])
x = np.linalg.solve(a, b)

print(x)







