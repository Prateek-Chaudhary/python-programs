print("using the global variable in that program")
x = 10


def global1():
    global x
    x = 45
    print("the value of x :", x)


global1()
print("the value of x in global scope is :", x)
