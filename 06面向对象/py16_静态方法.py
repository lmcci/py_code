# 不访问 实例属性 也不妨问 类属性

# @staticmethod


class Dog(object):
    @staticmethod
    def run():
        print('run')


Dog.run()

d = Dog()
d.run()
