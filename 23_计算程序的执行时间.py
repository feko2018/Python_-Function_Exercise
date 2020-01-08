# -*- encoding:utf-8 -*-

# 23、写一个计算每个程序执行时间的装饰器；
import time


def com_time(func):
    def inner():
        time_start = time.time()
        func()
        time_end = time.time()
        return (time_end-time_start)
    return inner

@com_time
def time_sleep():
    time.sleep(2)

@com_time
def time_sleep1():
    time.sleep(3)


print('execution time is %.02f s' % (time_sleep()))
print('execution time is %.02f s' % (time_sleep1()))