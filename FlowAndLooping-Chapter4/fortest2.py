#s = input("Enter the string ")
s = "python"
count = 0

for c in s:
    if c in ('a','e','i','o','u'):
        count = count + 1


print(count)