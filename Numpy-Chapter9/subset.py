import numpy as np


def sub_lists(l):
    sub_list = [()]
    for i in range(len(l) + 1):
        for j in range(i+1,len(l) + 1):
            sub = l[i:j]
            sub_list.append(sub)
    return sub_list


x = np.array([1,2,3,4])
print(sub_lists(x))
