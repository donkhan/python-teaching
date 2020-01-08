import numpy
import math

# https://www.lboro.ac.uk/media/wwwlboroacuk/content/mlsc/downloads/var_stand_deviat_ungroup.pdf

def find_std(raw_values):
    x_bar = 0
    total = 0

    for val in raw_values:
        total += val

    x_bar = total/len(raw_values)
    sigma_total = 0.0

    for val in raw_values:
        diff = val - x_bar
        sigma_total += diff * diff

    print(math.sqrt(sigma_total/len(raw_values)))
    print numpy.std(numpy.array(raw_values))


find_std([6,7,10,11,11,13,16,18,25])
find_std([74, 72, 83, 96, 64, 79, 88, 69])
