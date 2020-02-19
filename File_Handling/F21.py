with open("f1.txt","w") as f:
    f.write("Hey I am writing first line")
f.close()

with open("f1.txt","w") as f:
    f.write("Hey I am writing second line")
f.close()

with open("f1.txt","r") as f:
    print(f.read())
f.close()