# Tuple 不能对一个元组进行增删改
# 一般保存不同类型的数据

# 初始化之后就不能再改变
info_tuple = ('zhangsan', 18, 1.75)

print(type(info_tuple))

print(info_tuple[0])

# 只有一个元素的元组
# single_tuple = (5) # 当作int处理
# print(type(single_tuple))
single_tuple = (5,)
print(type(single_tuple))


# 获取元素出现的次数 不存在返回0不报错
print(info_tuple.count(18))

# 获取元素再元组中的索引 不存在报错
print(info_tuple.index(1.75))

# 元组中元素个数
print(len(info_tuple))

# 遍历 for 可以遍历列表 元组 字典 字符串

for item in info_tuple:
    print(item)


# 应用场景
# 函数的参数返回值  可以传入 传出任意多个值
# 格式字符串  print('aaa%d %d' % (a, b)) 本质上是一个元组
# 让列表不可以被修改 保护数据安全

info_str = '%s 年龄%d岁 身高%.2f' % info_tuple
print(info_str)


# 列表 元组相互转换
info_list = list(info_tuple)
print(type(info_list))

info_tuple = tuple(info_list)
print(type(info_tuple))
