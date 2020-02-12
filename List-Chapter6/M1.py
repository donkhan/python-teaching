n = input()
x = input().split()
l = list(x)
op = ""
for i in range(len(l)):
    op = op + " "+ str(int(l[i]) + int(l[len(l)-i-1]))

print(op[1:])



