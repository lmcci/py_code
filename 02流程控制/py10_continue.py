# 结束本次循环 执行下一次循环


# 死循环情况

i = 0

while i < 10:

    if i == 3:
        # todo
        continue

    print(i)

    i += 1

print("循环结束")
