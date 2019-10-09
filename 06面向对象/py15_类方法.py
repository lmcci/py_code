# cls 不能访问 实例属性 实例方法    只能访问 类属性 类方法

# 1 加 @classmethod
# 2 传参 cls


class Tool(object):
    count = 0

    @classmethod
    def show_count(cls):
        print(cls.count)

    def __init__(self):
        Tool.count += 1


t = Tool()
t1 = Tool()
Tool.show_count()

