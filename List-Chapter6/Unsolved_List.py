import statistics

def q12(input):
    sum = 0
    for val in input:
        sum = sum + val
    return (sum,statistics.mean(input))


def q10(l):
    return statistics.mean(l)

def q11(input):
    min = float("inf")
    for value in input:
        if value < min:
            min = value
    return min


def q15(input):
    t = input[0]
    for i in range(0,len(input)-1):
        input[i] = input[i+1]
    input[len(input)-1] = t
    return input


def q14(input,x):
    freq  = 0
    for ele in input:
        if ele == x:
            freq = freq + 1
    return freq

def q9(input):
    sum  = 0
    for val in input:
        try:
            if val % 2 == 1:
                sum = sum + val
        except TypeError:
            pass
    return sum

def q13(input):
    print(input)
    for i in range(1,len(input)-1,2):
        if type(input[i]) is int:
            input[i] = input[i] * 2
        return input


#print(q16([3,25,23,6,35,8,14,45]))
'''
print(q9([3,4,'a','aaa',1,2]))
print(q10([1,2,3]))
print(q11([3,4,2,13,1]))
answer = q12([50,60,80])
print(answer[1],answer[0])

print(q13([0,1,2,3,4,"k","a",4]))
print(q14([1,2,3,1,2,3],2))
print(q15([10,20,30,40]))


'''