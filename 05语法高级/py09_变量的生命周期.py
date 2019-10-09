# 局部变量 函数被调用时执行到初始化代码的时候被创建 函数执行完毕后被销毁 （有返回值的情况 特殊）
# 在不同函数中定义相同名字的局部变量无影响

# 在函数内部使用全局变量 一定要保证 函数被调用之前 全局变量已经被声明
# 全局变量命名 g_num 或者 gl_num

# 不能在函数内部直接修改全局变量的值

# 这样相当于又定义了一个局部变量 test_num 并没有修改到全局变量
test_num = 1


def demo():
    test_num = 2
    print(test_num)


demo()
print(test_num)


# 非要在函数内修改全局变量的话 用 global关键字
# 声明后面使用的都是全局变量

# 直接赋值或者 += -= 这样的要用global
# 对list.append() 不需要用global
def demo1():
    global test_num
    test_num = 2
    print(test_num)


demo1()
print(test_num)
