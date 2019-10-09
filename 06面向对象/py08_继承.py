# 继承 代码的重用
# 子类拥有父类所有的非私有属性和方法

# 子类拥有父类所有的属性和方法
# 子类可以直接使用父类的属性和方法
# 子类中主要实现特殊的属性和方法即可

# 继承的传递性： A --> B --> C   C类中可以直接使用A类中的属性和方法


class Animal:
    def eat(self):
        print('吃')

    def drink(self):
        print('喝')

    def run(self):
        print('跑')

    def sleep(self):
        print('睡')


class Dog(Animal):
    def bark(self):
        print('叫')


class XiaoTian(Dog):
    def fly(self):
        print('飞')

    def bark(self):
        """父类方法无法满足子类的需求 所以要重写"""
        print('xt叫')

    def run(self):
        """
        super().xxx 调用父类原有的属性和方法  对原有方法的扩展
        Py2.x中 调用父类方法 父类名.方法(self)  py3.x中也支持
        """
        super().run()
        print('run fast')


xtq = XiaoTian()
xtq.eat()
xtq.bark()
xtq.fly()
xtq.run()
