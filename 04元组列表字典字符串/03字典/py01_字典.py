# 键唯一

# 键可以是字符串 元组 数字型 不可变数据类型  不能用可变数据类型
# 因为字典都会使用hash(key) 增删改查 都依赖这个hash值
# 同一个数据调用hash() 返回结果都相同
# list dict 都不能调用hash()

# 值可以是任意数据类型

xiaoming = {
    'name': '小明',
    'gender': True,
    'age': 18,
}

print(xiaoming)

# 取值 如果键不存在就报错
print(xiaoming['name'])

# 添加  如果不存在就是添加 存在就是修改
xiaoming['height'] = 1.75
print(xiaoming)

# 修改
xiaoming['name'] = 'xiaoming'
print(xiaoming)

# 删除
# pop 键不存在就报错
xiaoming.pop('height')
print(xiaoming)

del xiaoming['age']
print(xiaoming)

# 统计键值对数量
print(len(xiaoming))

# 合并字段 如果有相同的键 会覆盖原有的
xiaoming.update({'a': 1})
print(xiaoming)

# 清空字典
xiaoming.clear()
print(xiaoming)


# 遍历
for key in {'a': 2, 'b': 3}:
    print(key)
