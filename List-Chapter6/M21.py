import random

word = "lion"
print("".join(random.sample(word,3)))

with open("file.txt","w") as f:
    print(f.read())
    f.write("hey, I am writing")
f.close()