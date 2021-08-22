n = int(input("Enter the range for fibonacci series\n"))
a = 0
b = 1
print(a, b, end=" ")
for i in range(n):
    s = a + b
    a = b
    b = s
    print(s, end=" ")
