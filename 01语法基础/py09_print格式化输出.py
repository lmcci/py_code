# %s 字符串
# %d 整数      %06d 表示一共显示6位 不足高位补0 大于6位的就完整显示数字
# %f 浮点数    %.2f 表示小数点后有两位 不足补0 多余的四舍五入  默认的小数点后保留6位
# %%  输出%

name = 'lmcci'
age = 10999999
height = 1.75

print('我叫%s, 今年%06d岁，身高%.01f  %%=======%%' % (name, age, height))


# eg 下面会重复输出9次 而不是 90 乘的优先级低
num = 10
print('hello %d' % num * 9)


#
# 默认print函数会在末尾增加一个换行
# 如果不需要换行 增加一个end参数
print('aa', end='')
print('aa', end='')

# end 就是在print末尾要输出的内容  默认是'\n'
