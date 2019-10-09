
def fun1():
    print("world")


def fun2():
    print("hello", end=" ")
    fun1()


fun2()
