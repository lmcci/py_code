# 在锁没有释放的时候 子线程一直阻塞

import time
import threading


def main():
    threading.Thread(target=add).start()
    threading.Thread(target=add).start()

    time.sleep(2)
    print(g_num)


lock = threading.Lock()
g_num = 0


def add():
    global g_num
    for i in range(1000000):
        lock.acquire()
        g_num += 1
        lock.release()

    print(g_num)





if __name__ == '__main__':
    main()










