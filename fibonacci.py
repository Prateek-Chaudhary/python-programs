a=0
b=1
print(b, end=" ")
for i in range(20):
    s=a+b
    a=b
    b=s
    print(s, end=" ")