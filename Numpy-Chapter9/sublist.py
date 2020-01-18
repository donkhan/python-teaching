import numpy as np

# { 1,2,3,4 }
#  2 power n
# { {1},{2},{3},{4},{1,2},{1,3},{1,4},{2,3},{2,4},{3,4},{1,2,3},{1,2,4},{1,3,4},{2,3,4},{1,2,3,4} ,NULL }


def sub_lists(l):
    sub_list = [()]
    for i in range(len(l) + 1):
        for j in range(i+1,len(l) + 1):
            sub = l[i:j]
            sub_list.append(sub)
    return sub_list


x = np.array([1,2,3])
print(sub_lists(x))
