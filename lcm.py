def hcf(x, y):
    if x < y:
        s = x
    else:
        s = y
    for i in range(1, s + 1):
        if (x % i == 0) and (y % i == 0):
            gcd = i
    return gcd


def lcm(x, y):
    lc = (x*y)/hcf(x, y)
    return lc


n = int(input())
m = int(input())
print("LCM is", lcm(n, m))
