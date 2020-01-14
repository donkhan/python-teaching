import numpy as np

sum = 0
for i in range(1,10):
    sum = sum + i
print(sum)

a = np.arange(1,10)
print(np.sum(a))

#print(np.max(a))
#print(np.min(a))


d_2 = np.array([[1,2],
                [3,4],
                [5,6]])

#print(np.concatenate([d_2,d_2]))
#print(np.concatenate([d_2,d_2],axis=1))

print(np.sum(d_2,axis=0))
print(np.sum(d_2,axis=1))

print(np.max(d_2,axis=0))
print(np.max(d_2,axis=1))


