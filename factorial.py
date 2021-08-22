f = 1
n = int(input("enter the factorial number\n"))
while (n>=1):
    f = f*n
    print(n, end=" ")
    n = n-1
print("\n")
print("sum of factorial is : ", f)