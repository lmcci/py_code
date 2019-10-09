# __new__ object提供的内置静态方法  被调用的时候还没有实例化 所有没有self 入参是cls
# 1 为对象分配空间
# 2 返回一个对象的引用

# 在__init__之前调用


class MusicPlayer(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        """ 重写object的__new__ """
        print('new')
        # 如果不返回值 就不会调用__init__  实例化返回None
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance
        # return super().__new__(cls)

    def __init__(self):
        print('初始化')


p1 = MusicPlayer()
p2 = MusicPlayer()
p3 = MusicPlayer()

print(p1)
print(p2)
print(p3)






