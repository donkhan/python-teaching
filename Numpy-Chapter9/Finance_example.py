import numpy as np

#What is the future value after 10 years of saving $100 now,
#with an additional monthly savings of $100. Assume the interest rate is 5% (annually) compounded monthly?
print(np.fv(0.03/12, 10*12, -100, -100))


d_2 = np.array([[1,2],[3,4]])
print("Before Transpose ",d_2, "After Transpose",np.transpose(d_2))


data = np.array([1,2,3,4,5])
print(np.mean(data))
print("Standard Deviation ",np.std(data))
