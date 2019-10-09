# 对象的内存空间只存属性
# 对象的方法在内存中是有一份在类的内存空间
# 调用的时候把自己的引用self传进去就可以在方法内访问到当前对象的属性


# 类是一个特殊的对象  叫 类对象  类对象也有属性方法  类属性 类方法  类名.xx
# 类创建的对象 叫 实例对象


class Tool(object):
    count = 0

    def __init__(self, name):
        # 对类属性赋值 直接使用 类名.xx
        Tool.count += 1
        self.name = name


t1 = Tool('斧头')
t2 = Tool('剪刀')

print(Tool.count)

print(t1.count)  # 如果对象中没有属性 就去类中寻找 类中没有找到就报错
t1.count = 10  # 这样是给t1对象下添加一个count属性 而不是改变Tool的类属性
print(Tool.count)

