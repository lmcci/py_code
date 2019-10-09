# 进程池 管理进程 不用重新创建和销毁进程

# 通过进程池创建的子进程 主进程不会等待所有子进程执行完毕  所以要调用 po.join()

# 进程池里面的代码执行抛出异常不会被打印

# 进程池里面的进程之间通讯用到的 Queue 使用 multiprocessing.Manager().Queue()

import multiprocessing
import time
import random
import os


def worker(msg):
    start_time = time.time()
    print('%d, 进程id:%d' % (msg, os.getpid()))
    time.sleep(random.random() * 2)
    end_time = time.time()
    print('%d, 执行完毕耗时： %.2f' % (msg, end_time - start_time))


po = multiprocessing.Pool(3)

for i in range(20):
    po.apply_async(worker, (i, ))

print('start====>')

po.close()
po.join()

print('end====>')



