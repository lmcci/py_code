def decorator(fun):

    def fun_caller(num):
        print('pre code')
        fun(num)

    return fun_caller


# @decorator
def test1(num):
    print('test1====>%d' % num)


test1 = decorator(test1)
test1(123)
