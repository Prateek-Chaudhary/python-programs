n = int(input("enter the number\n"))
for i in range(1,n):
    if i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)