a = input("enter the number 1\n")
b = input("enter the number 2\n")
try:
    s = int(a) + int(b)
    print("sum is : ", s)
except Exception as e:
    print(e)

def function():
    print("this is a function type")
    s = "this is a function"
    print(s)
    return s

v = function()
print(v)
