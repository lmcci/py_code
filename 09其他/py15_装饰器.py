# 在执行函数之前或者执行之后需要 执行一些逻辑 可以使用装饰器

# 装饰器依赖闭包


def decorator(fun):

    def fun_caller():
        print('pre code')
        fun()

    return fun_caller


@decorator
def test1():
    print('test1')


test1()


#######################

def test2():
    print('test2')


# decorator(test2)()
test2 = decorator(test2)
test2()
# 在调用函数不变的情况下 对功能进行扩展











