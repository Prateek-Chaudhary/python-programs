n = int(input("Enter the range\n"))
for i in range(1, n):
    s = 0
    temp = i
    while temp > 0:
        d = temp % 10
        s += d**3
        temp //= 10
    if s == i:
        print(s)
