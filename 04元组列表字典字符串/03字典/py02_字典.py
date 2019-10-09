# 字典通常用于描述一个事物
# 列表是有序的 字典是无序的

# 用{}定义
# 键必须是唯一的
# 键必须是 字符串 数字 元组(不可变类型)  值可以是任何数据类型

person = {
    "name": "小明",
    "age": 18,
    "gender": True,
    "height": 175
}

# 取值 如果key不存在就报错
# print(person["name"])
# key = "name"
# print(person[key])
# print(person["name123"])

# 如果存在就修改 如果没有就增加
# person["weight"] = 65
# person["name"] = "xiaoming"

# 删除 如果key不存在就报错
# person.pop("name")

# 获取键值对数量
# print(len(person))

# 合并字典 把当前字典和另一个字典合并  如果另一个字典有相同的键会被覆盖
# person.update({"weight": 65, "name": "xiaoming"})

# 清空字典
# person.clear()

# 字典无序 所以输出的内容前后顺序和定义是可能不一样
print(person)
