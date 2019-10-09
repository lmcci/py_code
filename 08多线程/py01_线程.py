import time
import threading

# Thread创建的target函数执行完毕 子线程结束
# 主线程会等待所有子线程执行完毕才结束





def dance():
    for i in range(10):
        print('dance')
        time.sleep(1)


def sing():
    for i in range(10):
        print('sing')
        time.sleep(1)


def main():
    t1 = threading.Thread(target=dance)
    t2 = threading.Thread(target=sing)
    t1.start()  # 创建线程 开始执行
    t2.start()

    # threading.enumerate() 返回当前系统中所有的线程
    while True:
        print('当前有 %d 个线程' % len(threading.enumerate()))
        time.sleep(0.4)


if __name__ == '__main__':
    main()

