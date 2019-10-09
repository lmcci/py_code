import multiprocessing
import time


# 主进程会等待所有子进程执行完毕后结束


def main():
    multiprocessing.Process(target=test).start()
    multiprocessing.Process(target=test).start()


def test():
    while True:
        print('1')
        time.sleep(1)


if __name__ == '__main__':
    main()
