

x = 29

for i in range(2,int(x/2)+1):
    if x % i ==  0:
        print("Not Prime")
        break
else:
    print("Prime")