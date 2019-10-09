# 列表 元组 字典 字符串 公共方法

# 内置函数 不需要import就可以直接使用的函数

# len统计元素个数
print(len([]))

# del() del 函数和关键字 删除一个变量 删除一个复杂数据类型的值
my_list = [1, 2, 3, 4]
del my_list[3]
print(my_list)

del(my_list[2])
print(my_list)


# max min 复杂数据类型中的最大值 和 最小值 字典是比较key
print(max(my_list))
print(min(my_list))

# 字典中 max min 比较的是key

# cmp在3.x中取消
# > < = 可比较 字符串 列表 元组  /   字典不能比较


# # 字符串 元组 列表 都可以切片 字典无序不能切片
print([1, 2, 3, 4, 5][0:1])
print((1, 2, 3, 4, 5)[0:1])


#  + 拼接   * 重复   字符串 列表 元组
print([1, 2] * 2)
print((1, 2) * 2)
print([1, 2] + [3, 4])

# list  extend + 区别  extend没有返回值 对原来列表改变   + 返回一个新的值
# append 只能追加一个元素  如果append(list) 会把传入的list当成一个元素插入
test_list = [1, 2, 3, 4]
test_list.append([0, 0, 3])
print(test_list)  # [1, 2, 3, 4, [0, 0, 3]]11


# in / not in  字符串 列表 元组 字典
# 只能判断字典的key
print(3 in [1, 2, 3])
print(30 not in [1, 2, 3])


