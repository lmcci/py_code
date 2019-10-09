# 除了调用 next(g) 还能用send来获取下一个值
# send可以传参


def get_num():
    num = 0

    while True:
        param = yield num
        print(param)
        num += 1


g = get_num()

# 如果要在第一次的时候用send不能传参 否则会崩溃 因为没有能接收这个参数
print(g.send(None))

print(next(g))
print(next(g))
print(next(g))

print(g.send('hello world'))
