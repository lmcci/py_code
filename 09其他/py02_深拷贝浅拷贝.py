import copy

a = [1, 2, 3]
b = a
c = [1, 2, 3]
d = copy.deepcopy(a)    # 深拷贝 把所有内容都复制一份

print(id(a))
print(id(b))
print(id(c))
print(id(d))


###############


e = [1, 2, 3, 4]
f = [5, 6, 7, 8]

g = [a, b]
h = copy.copy(g)    # 浅拷贝 新建了一个list里面的a b 引用还指向之前的


print(id(g))
print(id(h))
print(id(g[0]))
print(id(h[0]))


# 拷贝不可变数据类型的变量时 不会复制 内存地址都相同 等同于 直接赋值
# 数值型 字符串 元组 是不可变数据类型
print(id(1))
print(id(copy.copy(1)))

# deepcopy如果内容都是不可变数据类型就等同于赋值
# deepcopy如果内容中有一个是可变数据类型 就会复制一份相同的 例如：元组中有列表或者对象
print(id(copy.deepcopy(1)))


# 列表切片 是浅拷贝
# 字典的copy方法 {}.copy() 是value的浅拷贝
