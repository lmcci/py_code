# 当父类方法不能满足子类的需求 子类中可以定义一个同名的方法进行重写
# 子类实例化对象调用该方法的时候 使用的是子类中重写的方法

# 子类中如果还需要调用父类方法 使用 super().xxx  或者 父类名.方法名(self)
class Animal:
    def eat(self):
        print('eat')

class Cat(Animal):
    def eat(self):
        super().eat()
        # Animal.eat(self)
        print('cat eat')

c = Cat()
c.eat()

#


