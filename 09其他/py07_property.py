# 如果一个实例方法（没有多余的形参）被 @property 装饰  就是一个property属性

# 这个方法返回只 可以直接通过 实例对象.方法名 使用 不用加括号


class Goods(object):

    @property
    def size(self):
        return 10

    @size.setter
    def size(self, value):
        print(value)

    @size.deleter
    def size(self):
        print('del')


goods = Goods()
print(goods.size)


# 如果使用赋值 需要有 @size.setter       行参的value就是 等号右边的值
goods.size = 20

del goods.size



