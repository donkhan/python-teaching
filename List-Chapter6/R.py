import random

word = input("Enter a word where letter is not repeated ")
l = []
t = 1

for i in range(1,len(word)+1):
    t = t * i

while len(l) < t:
    j = "".join(random.sample(word,len(word)))
    l.append(j)
for each in l:
    print(each)

print(len(l))