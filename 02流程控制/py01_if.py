age = 16

if age > 18:
    print("可以进网吧")
else:
    print("不能进网吧")

# if语句下面所有带缩进的语句 是同一个代码块
# else语句下面所有带缩进的语句 是同一个代码块


# 逻辑运算符 != 在python2.x中是 <>    a <> b

num = 10

# 不同数据类型不能直接比较
if num > 20:
    print("num大于20")
    print("带缩进的 还属于if代码块")
print("没有缩进 不属于if代码块")
