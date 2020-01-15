import numpy as np


print(np.full((3,3),False,dtype = bool))
print(np.full((3,3),2,dtype = complex))


print(np.full((3,3),'A',dtype = object))

print(np.full((3,3),"ABC",dtype = "S"))

# https://stackoverflow.com/questions/13717554/weird-behaviour-initializing-a-numpy-array-of-string-data

print(np.full((3,3),"ABC",dtype = "S10"))
