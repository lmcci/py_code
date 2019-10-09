# 多个装饰器 初始化 从下到上依次执行
# 调用的时候 从上到下


def add_fun1(fun):
    print('fun1初始化')

    def caller(*args, **kwargs):
        print('fun1 running')
        return fun()

    return caller


def add_fun2(fun):
    print('fun2初始化')

    def caller(*args, **kwargs):
        print('fun2 running')
        return fun()

    return caller


# @add_fun1
# @add_fun2
def test():
    print('test')


# test()

test = add_fun1(add_fun2(test))     # 执行初始化
test()      # 运行


#############


# 类装饰器  函数上 写 @类名       函数变量名 = 类名（函数引用）    新建一个对象  调用对象的__call__






