line = "Python"

# using iteration
for c in line:
    print(c,end=",")

print()
# using indexing
for i in range(len(line)):
    print(line[i],end=",")
print()
# using slice
for c in line[0:len(line):2]:
    print(c,end=",")

print()
for c in line[ : : -1]:
    print(c,end=",")
print()