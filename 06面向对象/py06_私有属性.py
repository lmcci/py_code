# 一些属性和方法不希望被外界访问  变量名前面增加 __
# 对象的属性和方法不希望外部访问 只在内部使用

# 属性和方法变量名加 __ 就变成私有的了
# py没有真正的私有  只是把私有属性 变成了（_类名__属性名）使得外界无法访问


class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 30

    def __secret(self):
        print('这是一个秘密')

    def get_age(self):
        print(self.__age)
        self.__secret()
        return self.__age


xf = Women('小芳')
# xf.__age    # 报错 不能直接访问私有属性
# xf.__sectet()   # 报错 不能直接访问私有方法
xf.get_age()    # 正常 可以在公共方法里面访问私有属性 调用私有方法


# Py 中没有真正意义的私有
# 解释器把 __开头的属性变成了 （_类名__变量名） 所以在外界不能直接访问
print(xf._Women__age)
