def print_line():
    print("---------------------------------------------------")

# Creating
d1 = {}
d2 = dict()
d3 = {'motor': 'convert electrical to mechanical', 'generator' : 'convert mechanical to electrical'}
d4 = dict([('america','washington'),('india','new delhi')])

print(d4)

# Accessing

print(d4.get('america'))
print(d4['america'])

print(d1.get('america'))
#print(d1['america'])

# Traversing

for key in d4:
    print(key,d4.get(key))
print_line()

d4['srilanka'] = 'colombo'

for key in d4:
    print(key,d4.get(key))
print_line()
d4['america'] = 'new york'
for key in d4:
    print(key,d4.get(key))
print_line()
del d4['america']
for key in d4:
    print(key,d4.get(key))
print_line()

print("Keys",d4.keys())
print("Values",d4.values())
print("Values",d4.items())
for key in d4:
    print(key,d4.get(key))
print_line()

d4.clear()
for key in d4:
    print(key,d4.get(key))
print_line()

#membership
print('america' in d4)
print('america' not in d4)


d4['a'] = 'abc'
print(d4.get('a'))
d4.pop('a')
print(d4.get('a'))
