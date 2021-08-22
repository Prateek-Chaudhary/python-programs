ls = []
e = 0
o = 0
n = int(input("range of loop\n"))
print("elements :")
for i in range(0, n):
    l = int(input())
    ls.append(l)
    if l % 2 == 0:
        e = e + 1
    else:
        o = o + 1
print("numbers are : ", ls)
print("even numbers are : ", e)
print("odd numbers are :", o)