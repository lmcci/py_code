# 拆分
test_str = 'hell o worl d'

# 不会对原有字符串更改
print(test_str.split(' ', 1))

# 链接字符串 参数字符串列表
print(''.join(test_str.split()))


#####################################


# 切片  [开始索引:结束索引:步长]
# 索引包左不包右
# 索引位负即使倒着数
# 开始索引不写就是从第一位开始
# 结束索引不写就是到最后一位

num_str = '0123456789'
# 截取2-5的字符串
print(num_str[2:6])

# 截取2-末尾的字符串
print(num_str[2:])

# 从开始位值截取到5
print(num_str[:6])

# 截取完整的字符串
print(num_str[:])

# 从开始位置 每隔一个字符截取一个
print(num_str[::2])

# 从开始到 倒数第一个
print(num_str[-1])

# 字符串逆序
print(num_str[-1:0:-1])

# test
print(num_str[0: 2: 1])
