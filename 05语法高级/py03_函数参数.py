# 函数内部对参数进行“赋值” 不会影响实参
# 可变数据类型直接赋值不会影响 不可变数据类型直接赋值也不会影响

# 可变数据类型的参数 调用方法改变元素 会影响实参

# list使用 += 运算符 实际上是调用extend方法

gl_num_list = [1, 2, 3, 4, 5]

def test(num_list):
    # 调用extend 会改变实参
    # num_list += num_list

    # 和赋值一样 不会改变实参
    num_list = num_list + num_list
    print(num_list)

test(gl_num_list)
print(gl_num_list)
