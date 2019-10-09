import time


def task_1():
    while True:
        time.sleep(0.1)
        print(1)
        yield


def task_2():
    while True:
        time.sleep(0.2)
        print(2)
        yield


while True:
    t1 = task_1()
    t2 = task_2()
    # 交替执行
    next(t1)
    next(t2)

