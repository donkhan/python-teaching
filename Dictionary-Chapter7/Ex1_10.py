d1 = dict()
d2 = {}

d1['name'] = 'Python'
d2['name'] = 'Python'

print(d1 , d2)

d1['name'] = 'Java'
d2['name'] = 'Java'
print(d1 , d2)

d1['author'] = 'James Gosling'
d2['author'] = 'James Gosling'


key = ''
for key in d1:
    print(key, '=', d1[key])


d1.pop('name')
for key in d1:
    print(key, '=', d1[key])

print('name' in d2)
print('name' not in d2)

# common functions





