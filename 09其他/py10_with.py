# 上下文管理器  实现 __enter__ __exit__ 方法的对象


class MyFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')


my_file = MyFile('name')

# 会调用__enter__ 把返回值赋值给f
with my_file as f:
    # 抛出异常或者执行完毕 都会执行 __exit__
    # print(1 / 0)
    print(f.name)



# 另一种方法
from contextlib import contextmanager


@contextmanager
def my_test():
    f = {}
    yield f
    print('exit')


# 会把yield后面的值 返回给f  然后函数阻塞
with my_test() as f:
    # 当执行完毕 或者 抛出异常之后 在执行 yield之后的代码
    print('aaa')


