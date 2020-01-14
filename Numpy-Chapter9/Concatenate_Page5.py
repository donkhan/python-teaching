import numpy as np


a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.array([6,7])

print(np.concatenate([a,b,c],axis=1))


a = np.array([[1,2],
              [3,4],
              [10,12]
              ])
b = np.array([[5,6],
              [7,8],
              [15,16]
            ])
c = np.array([[5,6],
              [7,8],
              [15,16]
            ])

#print(np.concatenate([a,b,c],axis=0))
#print(np.concatenate([a,b],axis=1))

A = np.array([[7,5],[1,6]])
print(np.concatenate([A,A,A,A]))
print(np.concatenate([A,A,A,A],axis=1))

x = np.array([1,2])
#print(np.vstack([x,A]))

y = np.array([[99],[100]])
#print(np.hstack([y,A]))
