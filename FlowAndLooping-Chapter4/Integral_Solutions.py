
n = 0

print("EE")

for i in range(0,33):
    for j in range(0, 33):
        for k in range(0, 33):
            for l in range(0, 33):
                if i + j + k + l == 32:
                    print(i,j,k,l)
                    n = n + 1

print(n)