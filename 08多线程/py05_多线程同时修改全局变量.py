# 多个线程对同一个全局变量 同时赋值 会有问题
# 多个线程同时读 不会有问题
# 一个线程写 多个线程读 不会有问题
# 多个线程写 就有问题

import threading
import time


def main():
    threading.Thread(target=test).start()
    threading.Thread(target=test).start()

    time.sleep(3)

    # 最终输出的并不是20000
    print(g_num)


g_num = 0


def test():
    global g_num
    for i in range(1000000):
        g_num += 1


if __name__ == '__main__':

    main()








