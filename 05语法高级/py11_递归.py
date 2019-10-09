# 函数内部调用自身

# 递归都要有一个出口 一个条件不满足的时候不再调用自身

# 数字累加 1 ~ N

def get_sum(num):
    if num == 0:
        return 0
    return num + get_sum(num - 1)

print(get_sum(4))
