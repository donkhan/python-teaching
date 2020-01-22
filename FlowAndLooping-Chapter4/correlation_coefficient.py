import math

#https://www.socscistatistics.com/tests/pearson/default2.aspx

x = [1,2,3,4,5,6,7,8,9,10]
y = [3,4,9,12,15,18,21,24,27,30]

x_bar = 0
y_bar = 0
x_sum = 0
y_sum = 0

for i in range(0,10):
    pass    

for i in range(0,len(x)):
    x_sum += x[i]
    y_sum += y[i]


x_bar = x_sum/len(x)
y_bar = y_sum/len(y)

print(x_bar,y_bar)

sigma_xy = 0
sigma_x_square = 0
sigma_y_square = 0

den = 1

for i in range(0,len(x)):
    sigma_xy += (x[i] - x_bar)*(y[i] - y_bar)
    sigma_x_square += (x[i] - x_bar) ** 2
    sigma_y_square += (y[i] - y_bar) ** 2

r = sigma_xy/(math.sqrt(sigma_x_square) * math.sqrt(sigma_y_square))
print(r)


