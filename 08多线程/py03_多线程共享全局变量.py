import time
import threading

g_num = 0


def add_num():
    global g_num
    g_num = 666
    print('add_num ===> %d' % g_num)


def print_num():
    print('print_num ===> %d' % g_num)


def main():
    # 在一个子线程中修改了全局变量 其他子线程或者主线程中用到这个全局变量也是被修改过的
    threading.Thread(target=add_num).start()
    time.sleep(1)
    threading.Thread(target=print_num).start()
    time.sleep(1)
    print('main ===> %d' % g_num)


if __name__ == '__main__':
    main()









