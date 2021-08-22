n = int(input("Enter the number\n"))
c = 0
while n > 0:
    c = c + 1
    n = n//10
print(c)

m = int(input("Enter the number\n"))
mp = 1
s = 0
for i in range(0, m):
    r = m % 10
    m = m // 10
    mp = mp*r
    s = s + r
    print(r, end=" ")
    print()
    if m == 0:
        break
print("Sum of digit is ", s)
print("Multiplication of digit is ", mp)

k = int(input("Enter the number\n"))
sk = str(k)
print(sk[0], sk[-1])
skk = int(sk[0]) + int(sk[-1])
print(skk)
