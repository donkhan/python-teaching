def m1(a,b):
    for i in range(1, 101):
        if i % a == 0:
            print(str(i) + " fizz")
        if i % b == 0:
            print(str(i) + " buzz")
        else:
            print(str(i) + " fizzbuzz")

def m2(a,b):
    for i in range(1, 101):
        if i % a == 0:
            if i % b != 0:
                print(str(i) + " fizz")
        if i % b == 0:
            if i % a != 0:
                print(str(i) + " buzz")
            else:
                print(str(i) + " fizzbuzz")

#a = int(input("Enter value of a "))
#b = int(input("Enter value of b "))

m2(2,3)

