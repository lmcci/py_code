from collections.abc import Iterable
from collections.abc import Iterator
import time

print(isinstance([], Iterable))
print(isinstance(range(10), Iterable))
print(isinstance(100, Iterable))

# 判断对象是不是这个类的实例
# 如果不是Iterable的实例 就不能迭代 不能用for遍历
# 如果不是Iterator的实例 就不死迭代器

# 可迭代的对象可以和迭代器是同一个
# 如果定义一个类 希望能被for遍历 重写__iter__ 返回一个具有__iter__ __next__方法的对象（迭代器）

# iter(obj) 查看对象的迭代器  相当于调用了对象的 __iter__方法， 返回了迭代器对象
print(iter([]))
# next(迭代器) 会调用迭代器的__next__ 获取下一个值  __next__直到返回 抛出StopIteration异常
print(next(iter([10, 12, 13])))


class MyList(object):
    def __init__(self):
        self.name_list = list()

    def add(self, name):
        self.name_list.append(name)

    def __iter__(self):
        return MyListIterator(self.name_list)


class MyListIterator(object):
    def __init__(self, item_list):
        self.item_list = item_list
        self.current_index = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.current_index < len(self.item_list):
            item = self.item_list[self.current_index]
            self.current_index += 1
            return item
        else:
            raise StopIteration


name_list = MyList()
name_list.add('张三')
name_list.add('李四')
name_list.add('王五')
name_list.add('赵六')


for name in name_list:
    print(name)
    time.sleep(1)

