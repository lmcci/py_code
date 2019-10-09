from collections.abc import Iterable
from collections.abc import Iterator
import time


class MyList(object):
    def __init__(self):
        self.name_list = list()
        self.current_index = 0

    def add(self, name):
        self.name_list.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < len(self.name_list):
            item = self.name_list[self.current_index]
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
