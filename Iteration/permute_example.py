import itertools

l = list(itertools.permutations(['2','3','3','6','6','7','9']))
c = 0
d = {}
for e in l:
    s = ""

    for i in range(0,7):
        s = s + e[i]
    if d.get(s) == None:
        if int(s) > 6000000:
            c = c + 1
            d[s] = "p"

print(c)