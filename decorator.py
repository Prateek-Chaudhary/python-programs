def fun1(n):
    def exe():
        print("This is a internal function")
        n()
        print("This is a internal function 2")
    return exe()


@fun1
def my():
    print("this is a external function for this use")
