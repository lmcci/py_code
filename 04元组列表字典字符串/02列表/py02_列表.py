# 列表用[]表示 内容用,分割 索引从0开始 同一个列表可以存不同类型的数据

num_list = [1, 2, 3, 4, 5, 6]

# 按索引取值
# print(num_list[0])
# print(num_list[10]) 索引超出报错

# 按值去索引
# print(num_list.index(5))
# print(num_list.index(100)) 不在列表中就报错

# 修改指定索引的内容
# num_list[0] = 100
# num_list[10] = 100  超出范围 报错

# 末尾添加数据
# num_list.append(7)

# 指定位置添加数据
# num_list.insert(0, 0)

# 添加一组数据
# num_list.extend([1, 2, 3])

# 清除所有
# num_list.clear()

# 删除指定内容（删第一次出现的位置） 如果内容不存在就报错
# num_list.remove(1)

# 删除指定索引的内容 不带参数从末尾删除一项 返回被删除的值
# num_list.pop(0)

# del 关键字 删除指定索引的内容
# del num_list[0]

# 把一个变量从内存中删除  后续代码不能再使用这个变量
# name = 'abc'
# del name

# 获取列表长度  len函数
# print(len(num_list))

# 某个元素出现次数
# print(num_list.count(2))

# 反转
# num_list.reverse()

# 排序
num_list.sort(reverse=True)

print(num_list)

# 遍历
for num in num_list:
    print(num)
