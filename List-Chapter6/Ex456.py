l_1 = [1,2,3]
l_2 = [4,5,6]

print(l_1 + l_2)

print(l_1 * 4)

print(1 in l_1)
print(5 in l_1)

print(l_1[2])

# private function. Should be avoided
print(l_1.__getitem__(1))

# same as string
print(l_1[1:2])

l_1.extend(l_2)

print(l_1)

del l_1[3]

print(l_1)
