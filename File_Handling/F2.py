with open("f21.txt","w") as f:
    f.write("0110")
f.close()

with open("f21.txt","r") as f:
    l = list(f.read())
    s = 0
    for each in l:
        s = s + int(each)
    print(s)
f.close()