# Example for Nested Loop

n = int(input("Enter the No..."))

s = 0
for i in range(1,n+1):
    ls = 0
    for j in range(1,i+1):
        ls = ls + j
    s = s + ls

print(s)