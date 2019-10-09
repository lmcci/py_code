# 对象为空 就设置为None
# 判断一个对象是否为空 不要用 obj == None
# == 判断的是 变量的值 是否相同  [1, 2, 3] == [1, 2, 3]
# 用 is 判断两个变量内存地址是否相同
# obj1 is obj2      obj1 is not obj2

# print(1 is 1)   # True
# print([1, 2, 3] is [1, 2, 3])   # False
# print([1, 2, 3] == [1, 2, 3])   # True


class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return '我叫%s, 体重%.2fkg' % (self.name, self.weight)

    def run(self):
        self.weight -= 0.5

    def eat(self):
        self.weight += 1


xm = Person('小明', 60)
print(xm)
xm.run()
print(xm)
xm.eat()
print(xm)
