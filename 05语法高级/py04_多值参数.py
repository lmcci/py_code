# 函数的参数个数不确定的时候可以使用 多值参数
# *args 接收一个元组
# **kwargs 接收一个字典

def demo(num, *nums, **dic):
    print(num)
    print(nums)
    print(dic)

demo(0)
print('-------------')
demo(0, 1, 2, 3, 4)
print('-------------')
demo(0, 1, 2, 3, 4, name="aa", age=10)


# 任意多个参数求和

def get_sum(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(get_sum(1, 2, 3, 4, 5, 6, 7, 8))


# 拆包 实参传入的时候 如果是一个元组变量使用*拆分传入 字典变量用**传入
