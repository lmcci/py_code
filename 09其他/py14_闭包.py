# 函数嵌套  返回一个引用 返回的这个对象或者函数中使用到了外层函数中的变量


# 函数嵌套 使用外部函数变量 可以使用  nonlocal x  用法和 global x类似


def outer():
    x = 10

    def inner1():
        nonlocal x
        x = 20

    def inner2():
        print(x)

    return inner1, inner2


i1, i2 = outer()

i1()
i2()




