# socket
# 操作文件
# queue

import multiprocessing
import time
import random


def main():
    q = multiprocessing.Queue(3)
    # q.full() 是否已经满了
    # q.empty() 是否已经空了
    # q.put(1) 往队列里面添加一个数据  如果满了就阻塞
    # q.put_nowait(1) 往队列里面添加一个数据 如果满了就抛出异常
    # q.get(1) 从队列里面获取一个数据 如果为空就等待
    # q.get_nowait(1) 从队列里面获取一个数据 如果为空就抛出异常
    multiprocessing.Process(target=get_data, args=(q, )).start()
    multiprocessing.Process(target=process_data, args=(q, )).start()


def get_data(q):
    while True:
        random_num = random.randint(1, 10)
        q.put(random_num)
        print('放入 %d' % random_num)
        time.sleep(1)


def process_data(q):
    while True:
        print('取出 %d' % q.get())






if __name__ == '__main__':
    main()



