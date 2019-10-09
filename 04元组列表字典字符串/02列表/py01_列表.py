# list 就是数组  可以存储不同数据类型的数据 

name_list = ['zhangsan', 'lisi', 'wangwu']
print(name_list[0])

# 长度
print(len(name_list))

# 添加
name_list.append('zhaoliu')
print(name_list)
name_list.insert(0, 'NO.1')
print(name_list)
name_list.extend([1, 2, 3])  # 会在原列表后面添加新list
print(name_list)

# 修改
name_list[3] = 'aaa'
print(name_list)

# 查索引
print(name_list.index('lisi'))
# print(name_list.index('lisi0000'))  如果不存在就报错

# 查找出现次数
print(name_list.count('lisi'))

# 删除
name_list.remove('NO.1')  # 删除指定的元素 如果不存在就报错  如果有多个删除第一个
print(name_list)
name_list.pop()  # 删除并返回指定索引的元素  不传索引删除最后一位
print(name_list)
name_list.clear()
print(name_list)


# del关键字 把一个变量从内存中删除
test_del_list = [1, 2, 3]
del test_del_list[0]
print(test_del_list)
