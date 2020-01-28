list = ['a','b','a','c','a','b','d']
dictionary = {}

for element in list:
    if element in dictionary:
        dictionary[element] = dictionary[element] + 1
    else:
        dictionary[element] = 1
print(dictionary)
