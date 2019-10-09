import threading
import time

# 当子线程所要运行的逻辑比较复杂的时候
# 定义一个类继承Thread 重写run方法  当实例化这个类再调用start()的时候 run方法内的逻辑会被子线程执行


class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print('abc')
            time.sleep(1)


def main():
    t = MyThread()
    t.start()







if __name__ == '__main__':
    main()


