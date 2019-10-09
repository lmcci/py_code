# 子类不能使用父类的私有属性和方法
# 除非父类通过共有的方法对外暴露简介访问到父类的私有属性

class Father:
    def __init__(self):
        self.__private_num = 1
        self.public_num = 2

    def __private_fn(self):
        print('父类私有方法')

    def public_fn(self):
        print('父类共有方法')
        print('私有属性 %d' % self.__private_num)
        self.__private_fn()

class Son(Father):
    def test(self):
        print(self.public_num)
        self.public_fn()


s = Son()
s.test()
