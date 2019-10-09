# 和其他语言的简单数据类型 复杂数据类型不同

# 变量 记录内存地址 叫做引用
# 变量值 保存在对应内存地址的内存中

# id() 可以查看变量保存值的内存地址
a = 1
b = a
print(id(a))
print(id(1))
print(id(b))
# 输出结果相同

a = 2  # id(a) 的结果有改变


#######################
# 函数传参 返回值 传递的是内存地址 即引用

def test_print(num):
    print('%d 的内存地址是 %d' % (num, id(num)))


test_num = 10
print(id(test_num))
test_print(test_num)


# 数字类型 字符串 元组 属于不可变类型  一但被赋值 内存地址中的值就不能被改变  能改变的是变量的引用
# 列表 字典 属于可变类型 内存地址的值可以改变 通过方法操作的是内存地址里面的值

test_list = [1, 2, 3, 4]
print(id(test_list))
test_list.append(5)
print(id(test_list))
test_list = []
print(id(test_list))

# 只能接收一个不可变类型的数据
# 返回一个特征码 相同的内容hash结果相同 不同的内容hash结果不同
# 保存在dict中的key都要进行hash 所以解释了为什么dict的key不能是可变数据类型
hash(1)
