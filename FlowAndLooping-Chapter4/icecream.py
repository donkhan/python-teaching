
# Vanilla, Chocolate, Mango, Strawberry
#(10,0,0)
#(0,10,0)
#(0,0,10)
#(9,1,0)
#(1,9,0)
#(0,1,9)
#(8,2,0)

n = 0
for vanilla in range(0,11):
    for chocolate in range(0,11):
        for mango in range(0,11):
            if vanilla + chocolate + mango == 10:
                print(vanilla,  chocolate ,mango)
                n += 1
print(n)


