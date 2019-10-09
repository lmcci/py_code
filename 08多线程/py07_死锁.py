# 多线程 一个线程持有一个锁 就可能会死锁

import time
import threading

lock_a = threading.Lock()
lock_b = threading.Lock()


def test():
    for i in range(50000):
        lock_a.acquire()
        time.sleep(0.1)
        lock_b.acquire()
        time.sleep(0.1)
        print('test %d' % i)
        lock_b.release()
        lock_a.release()


def main():
    threading.Thread(target=test).start()
    threading.Thread(target=test).start()


if __name__ == '__main__':
    main()

