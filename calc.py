print("enter the two variables")
v1=int(input())
v2=int(input())
print("enter the operator")
v=input()
if v=="+":
    r=v1+v2
    print(r)
elif v=="-":
    r=v1-v2
    print(r)
elif v=="*":
    r=v1*v2
    print(r)
else:
    r=v1/v2
    print(r)
