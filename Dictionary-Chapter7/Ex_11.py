l = ['a','b','a','c','a','b','d']

d = {}
for i in l:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1


print(d)
