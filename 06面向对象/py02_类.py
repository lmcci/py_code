# 类名大驼峰  HelloWorld

# 类中的方法第一个参数都是self
class Cat:
    def eat(self):
        print('eat')
    def drink(self):
        print('drink')


# 创建一个对象
tom = Cat()
tom.name = '汤姆'
tom.eat()
tom.drink()
# 直接打印对象 输出 是哪个类创建的 还有内存地址
print(tom)
print('%x' % id(tom))  # %x 16进制输出整数


# dir 内置函数 查看对象的所有属性和方法   __xx__ 内置的
print(dir(tom))  # 返回一个字符串列表



