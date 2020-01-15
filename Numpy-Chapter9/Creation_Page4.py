import numpy as np


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








