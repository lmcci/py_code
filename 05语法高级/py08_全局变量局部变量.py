# 局部变量 定义在函数内部的变量 只能在这个函数内部使用
# 全局变量 定义在函数外部的变量 所有的函数内部都能使用


def demo1():
    num = 10
    print(num)


def demo2():
    print(num)


demo1()
print(num)



