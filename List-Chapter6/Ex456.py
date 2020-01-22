'''
l_1 = [1,2,3]
l_2 = [4,5,6]

print(l_1 + l_2)

print(l_1 * 4)

print(1 in l_1)
print(5 not in l_1)

print(l_1[2])

# private function. Should be avoided
print(l_1.__getitem__(1))

# same as string
print(l_1[1:2])

l_1.extend(l_2)

print(l_1)

del l_1[3]

print(l_1)
'''

# Built_in Functions

# Append. Append the value at the end of list
l = [1,2,3]
l.append(4)
print(l)

# extend
l2 = [5,6,7]
l.extend(l2)
print(l)

# insert (at a given location)
l.insert(4,8)
print(l)

# reverse
l.reverse()
print(l)

l.reverse()

print(l)

# index
print("Index of 7 ",l.index(7))

# length of the list
print(len(l))

# sort
l = [2,3,1,4,5]
print(l)
l.sort(reverse=True)
print(l)

# Count
l = [1,2,3,2,4,2]
print("Count of 2 ",l.count(2))

# delete an element
del l[2]
print(l)

# update
l[0] = 46
print(l)

# Remove all elements
l.clear()
print(l)



















