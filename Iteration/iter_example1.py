

import itertools

l = list(itertools.combinations(['Vannila','Chocolate','Strawberry'],2))
print(l)
print(len(l))

l = list(itertools.combinations_with_replacement(['Vannila','Chocolate','Strawberry'],10))
print(l)
print(len(l))

l = list(itertools.permutations(['Vannila','Chocolate','Strawberry'],2))
print(l)
print(len(l))

for c in itertools.cycle(['A','B']):
    print c








