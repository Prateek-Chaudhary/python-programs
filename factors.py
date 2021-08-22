n = int(input("Enter the number for factor\n"))
for i in range(1, n//2 + 1):
    if n % i == 0:
        print(i)
