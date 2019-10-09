# 函数如果没有传递这个参数就使用缺省参数
# 如果不指定缺省参数 函数调用的时候 参数个数必须相同 否则报错
# 缺省参数 必须在参数列表的末尾

# def print_name(name="姓名未知"):
#     print(name)
# print_name('a')

# 函数的参数列表如果有多个缺省参数的时候 调用的时候 需要加上参数名

def print_info(name="未知", sex="男"):
    print(name + "\t" +sex)

# print_info("张三", "男")

# 这种情况如果name未知想使用缺省参数只传入sex的时候要加上参数名，否则默认按照参数列表顺序传递name被赋值“男”
# print_info("女")
print_info(sex="女")

