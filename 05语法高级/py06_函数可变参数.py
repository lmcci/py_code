# 参数名前加 * 接受一个元组
# 参数名前加 ** 接受一个字典


def demo(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


demo(1)
print('==' * 20)
demo(1, 2)
print('==' * 20)
demo(1, 2, 3, 4, 5, '', 1.2, (1, 20), {'a': 1}, name='xiaoming', age=18)


####################


# 元组 字典 拆包   简化实参的传递

def demo1(*args, **kwargs):
    print(args)
    print(kwargs)


test_tuple = (1, 2, 3, 4)
test_dict = {'name': 'xiaoming', 'age': 18}
print('==' * 20)
demo1(test_tuple, test_dict)
print('==' * 20)
demo1(*test_tuple, **test_dict)



