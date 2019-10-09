# 多个返回值


def measure():
    width = 10
    height = 20

    # 有多个返回值的时候 可以使用元组返回
    # return (width, height)
    return width, height  # 返回值 返回一个元组的时候可以省略小括号


res = measure()
# 不方便
# g_width = res[0]
# g_height = res[1]

# 变量的个数要和返回值元组中元素个数相等
g_width, g_height = measure()


print(res)


# 交换两个变量里的值
a = 1
b = 2
a, b = (b, a)
print(a)
print(b)


# 缺省参数
def print_str(txt='hello world'):
    print(txt)


print_str()
print_str('abc')

# 缺省参数必须在参数最后  不然使用默认值的时候 实参 形参无法一一对应
# def test_fault(txt='hello world', color):
#     print('')

# 调用多个缺省参数的函数时
# def test_fault(txt='hello world', color='#FFFFFF'):
#     print('')
# test_fault(color='#000000')
