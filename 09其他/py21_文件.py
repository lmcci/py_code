# 文件 分为  文本文件  二进制文件


# open 全局函数 打开文件返回一个文件操作对象

# 文件路径 作为参数传给open 区分大小写
hello_file = open('res/hello')

# read 一次性读取所有内容 并返回
print(hello_file.read())

# 文件指针 标记从哪里开始读
# 调用read后文件指针移动到文件末尾  再次调用read不会读取任何内容
print(hello_file.read())

# 关闭
hello_file.close()


# 打开文件的方式 默认只读
# r只读     w只写如果存在就覆盖不存在就创建    a追加   b以二进制的方式
# r+ w+ a+ 读写方式
hello_file = open('res/hello', 'a')

hello_file.write('new')

hello_file.close()


hello_file = open('res/empty')

# 读取一行 返回一行的结果 文件指针移动到下一行
# readline() 会把当前行的换行符也读出来

while True:
    t = hello_file.readline()
    print(t, end='')
    print(type(t))
    if t == '':
        break

hello_file.close()


file = open('res/hello')
copy = open('res/copy', 'w')

while True:
    t = file.readline()
    if t == '':
        break
    copy.writelines(t)

file.close()
copy.close()

