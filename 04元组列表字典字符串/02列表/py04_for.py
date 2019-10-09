# for else
# for循环通过break退出 就不会执行else的代码

for n in [1, 2, 3]:
    print(n)
else:
    # list中所有元素都被遍历了 这里就执行
    #  使用场景就是循环查找 查找到了break 这里做都没有找到的逻辑处理
    print('else')

print('end')
