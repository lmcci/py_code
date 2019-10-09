# 字符串 列表 元组 +拼接 *重复

# print([1, 2] * 2)
# print((1, 2) * 2)
# print([1, 2] + [3, 4])
# print((1, 2) + (4, 5))


# in 判断元素是否存在 所有复杂数据类型 字典的key

# print("name" in {"name": "python"})
# print("1" in "123")

# not in    in的相反、


#  当for in 中没有break退出循环的时候 会执行else中的代码
#  如果break退出了 else中代码不会执行
num_list = [1, 2, 3, 4]
for num in num_list:
    print("num")
else:
    print("没有break")

