# 3 ways to create the list
l_1 = [1,2,3,'e']
l_2 = list()
l_3 = []

# Accessing element in the list
print(l_1[2])

print(l_1)
# Traversing
for ele in l_1:
    print(ele)

# Aliasing
alias_l1 = l_1
print(alias_l1)

l_2.append(1)
l_2.append(2)
l_2.append(3)
l_2.append('f')

print("L1",l_1)
print("L2",l_2)


print(l_1 < l_2)

