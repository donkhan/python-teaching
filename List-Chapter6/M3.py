l = [int(i) for i in "21 47 32 43".split()]
o = ""
for ele in l:
    if ele % 5 != 0:
        o = o + " " + str(ele)
print(o[1:],end="")




