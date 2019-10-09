# 使用 类名() 创建对象的时候 自动执行以下操作

# 分配内存 创建对象
# 为对象属性设置初始值 __init__方法

# __init__ 初始化方法 对象的内置方法
# 作用 专门定义一个类具有哪些属性的

# 如果希望在创建对象的时候 就设置一些属性的值，
# 可在创建对象的时候把属性值传入 __init__方法中可以接收到这些属性值 并且设置给self  self.属性名 = 形参

# 创建对象的时候
# 1 分配空间
# 2 给属性设置初始值   自动调用 初始化方法 __init__


# 当对象被销毁的时候 会自动调用 __del__ 方法
# 从内存中销毁对象的时候
# 会自动调用 删除的方法 __del__
# 当程序执行完毕的时候 所有全局对象都被销毁


# print输出一个对象 会有对象所属的类名 还有对象的内存地址
# __str__ 方法必须返回一个字符串 print打印对象的时候 会打印出这个返回值
# 直接print输出一个对象 默认是 哪个类创建的类名 内存地址
# __str__ 必须返回一个字符串 用于打印


class Cat:
    def __init__(self, name):
        print('init')
        self.name = name

    def __del__(self):
        print('del')

    def __str__(self):
        return self.name


tom = Cat('汤姆')
print(tom.name)
print(tom)

# del tom
print('end')
