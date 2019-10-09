# 当需要函数返回多个返回值时可以使用元组返回
#


def get_temp():
    max_temp = 10
    min_temp = 5
    # 返回值是一个元组的时候可以省略小括号
    # return (min_temp, max_temp)
    return min_temp, max_temp


result = get_temp()
print(result)

# 返回结果是一个元组的时候可以用多个变量接收  个数必须一样
gl_min_temp, gl_max_temp = get_temp()
print(gl_min_temp)
print(gl_max_temp)


# 交换两个变量的值
a = 1
b = 2
a, b = b, a

print(a)
print(b)
