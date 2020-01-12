import numpy as np

print np.version.version

a = np.arange(1,10)
print a

# Q8. Print True...
print a > 0

# All Odd Values
print a[a %2 == 1]

# All Even Values
print a[a %2 == 0]

# Replace all odd values with 1
a[a%2 == 1] = 1
print a

x = np.arange(0,20)
print np.reshape(x, (10,2))




