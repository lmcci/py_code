def decorator(fun):
    print('装饰器初始化')

    def fun_caller(*args, **kwargs):
        print('before code')
        res = fun(*args, **kwargs)
        print('after code')
        return res

    return fun_caller


print('======')

# 遇到装饰器声明的时候就开始执行了装饰器初始化


@decorator
def test1(num):
    print('test1====>%d' % num)
    return num + 1


# 当函数真正被调用的时候 闭包内函数才真正执行
test1(100)

# test1 = decorator(test1)
# print(test1(123))
