n = int(input("Enter the number for reverse consecutive number\n"))
s = 0
for i in range(1, n):
    s = s + i
    if s == n:
        print(i)
        break
