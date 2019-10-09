# self 哪个对象调用的方法 self就是哪个对象的引用
# 方法内部可以通过 self访问对象的属性  也可以通过self调用对象的方法

class Cat:
    def eat(self):
        print('%s eat' % self.name)
    def drink(self):
        print('drink')

tom = Cat()
tom.name = '汤姆'
tom.eat()


# tom.name = '汤姆'  在外部给对象添加属性有问题  应该把属性封装到类的内部


