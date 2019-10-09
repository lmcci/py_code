# 元组和列表类似 用,分割 索引从0开始

# 定义用()
# 元组的元素不能修改
# 元组通常保存不同类型的数据 列表通常保存相同类型的数据

info_tuple = ('zhangsan', 18, 1.80)

# 取值
# print(info_tuple[0])

# 如果只有一个元素 需要在最后添加一个逗号  (1) 这种声明方式可能被认为 是优先级的小括号 只被认为是int
# print(type((1,)))
# print(type((1)))

# 元素在元组中出现的次数
# print(info_tuple.count(18))

# 通过索引获取元组的元素
# print(info_tuple[0])

# 获取元素在元组中的索引
# print(info_tuple.index(18))

# 获取元组中元素的个数
# print(len(info_tuple))
