def hcf(x, y):
    if x < y:
        s = x
    else:
        s = y
    for i in range(1, s + 1):
        if (x % i == 0) and (y % i == 0):
            gcd = i
    return gcd


n = int(input("Enter the first number\n"))
m = int(input("Enter the second number\n"))
print("HCF is ", hcf(n, m))
