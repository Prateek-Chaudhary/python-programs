s = 0
f = 1
n = int(input("enter the factorial number\n"))
for i in range(1,n+1):
    f=1
    while (i>=1):
        f = f * i
        i = i - 1
    print(f)
    s = s +f
print("\n")
print("sum of factorials are : ", s)
