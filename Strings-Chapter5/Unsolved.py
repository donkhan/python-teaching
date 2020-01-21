def count_vowels(word):
    a = e = i = o = u = 0
    for i in range(0,len(word)):
        c = word[i]
        if c == 'a':
            a = a + 1
        if c == 'e':
            e = e + 1
        if c == 'i':
            i = i + 1
        if c == 'o':
            o = o + 1
        if c == 'u':
            u = u + 1
    print(word,a,e,i,o,u)

count_vowels("vinny kumar")

def count_is(line):
    c = 0
    words = line.split()
    for word in words:
        if word == 'is':
            c = c + 1
    print("No of is in \"" + line + "\" = " + str(c))

count_is("my name is python. It is a functional language ")

print("INSTITUTE".split('T'))
print("medicine".replace('i',''))

g = "Global Warming"
print(g[-4:])
print(g.replace('a','*'))


print("Z in School ","School".find('Z'))

#9b Change the case
t = "tuTion"
n = ""
for c in t:
    if c.isupper():
        n = n + c.lower()
    if c.islower():
        n = n + c.upper()

print(t,n)

print("sequence".rfind('e',3))

