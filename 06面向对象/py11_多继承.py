# 一个子类可以有多个父类
# 子类同时具有所有父类的属性和方法

# 多个父类具有同名的属性和方法的时候 子类调用父类方法用MRO 方法搜索顺序来判断调用哪个
# 类名.__mro__ 来输出顺序 返回一个元组 从左向右依次查找 使用找到的第一个

# py中所有对象的基类 是object 在其中提供一些内置的属性和方法
# py3中所有类 如果没有指定父类 都会默认使用object为基类

class Father:
    def f_fn(self):
        print('F')

class Mother:
    def m_fn(self):
        print('M')

class Son(Father, Mother):
    pass

s = Son()

s.m_fn()
s.f_fn()

print(Son.__mro__)
# (<class '__main__.Son'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class 'object'>)
