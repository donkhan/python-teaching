import numpy as np

a = np.array(([1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]))


a = np.arange(0,10)
print(a)

print(np.extract(a%2 == 0,a))
