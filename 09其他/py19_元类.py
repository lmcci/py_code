# globals()        返回一个字典  是所有全局已经申明的变量和值 包括内建模块 如（print input 。。。。。）


# print(globals()['__builtins__'])


print(globals())


def test():
    AAAAAA = 10
    # 局部变量 不会在 globals()中
    print(globals())

test()

BBBBBB = 100

print(globals())



# 元类 用来创建类

class Test1(object):
    name = ''
    age = 0


# 用type创建类  类名  要继承的父类元组    类属性 类方法 实例方法 静态方法 的字典
Test2 = type('Test2', (object,), {'name': '', 'age': 0})

help(Test1)
help(Test2)




# 使用class定义一个类的时候 默认会使用type创建一个类

# 除非 定义 metaclass=xxxxx     就使用指定的元类来创建类
# 在这个元类的方法里面 可以重新定义一些个性方案




# 装饰器可以对已有函数进行扩展
# 元类可以对已有的类进行扩展



