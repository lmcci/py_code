# 生成器是一种特殊的迭代器


# 函数内只要有yield 就是生成器
# 调用这个函数 就是创建生成器

# 迭代器里面的返回值 可以在迭代完成后抛出异常 e.value 获得

import time


def get_all_odd_num():
    current_num = 0

    while True:
        if current_num % 2 == 1:
            yield current_num

        current_num += 1


all_odd_num = get_all_odd_num()

print(iter(all_odd_num))
print(next(all_odd_num))

# yield 后面的变量就是 迭代出来的 odd_num
# 当print(odd_num)的时候生成器暂停执行 直到要迭代下一个内容的时候才继续执行
# 以此类推

# for odd_num in all_odd_num:
#     print(odd_num)
#     time.sleep(0.2)
