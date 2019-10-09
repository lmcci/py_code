# 如果 多个父类中存在同名的属性和方法 应避免多继承
# 子类调用方法和属性的时候 具体使用哪个父类的属性和方法 使用MRO确定


class A:
    def test(self):
        print('A test')

    def demo(self):
        print('A demo')


class B:
    def test(self):
        print('B test')

    def demo(self):
        print('B demo')


class C(A, B):
    pass


print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# 先搜索C下面有没有要找的属性或者方法 有就使用  没有就找A下面 以此类推  直到object
# object下面再没有就报错


# py3.x 没有指定父类默认就是object  # object是所有类的基类
# py2.x 没有指定父类就没有父类

# 以object为基类的就是新式类
# 不以object为基类的就是旧式类

print(dir(C()))
