# -*- encoding:utf-8 -*-

import datetime

#
# 13、通过生成器写一个日志调用方法， 支持以下功能
#
# - 根据指令向屏幕输出日志
#
# - 根据指令向文件输出日志
#
# - 根据指令同时向文件&屏幕输出日志
#
# - 以上日志格式如下
#
# 2017-10-19 22:07:38 [1] test log db backup 3
#
# 2017-10-19 22:07:40 [2]    user alex login success
#
# 注意：其中[1],[2]是指自日志方法第几次调用，每调用一次输出一条日志


def logger(filename, channel='file'):
    count = 0
    i = 1
    if channel == 'terminal':
        while True:
            n = yield
            count +=i
            log_print = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') +' ' +"[%s] %s" % (count, n)
            print(log_print)
    if channel == 'file':
        while True:
            n = yield
            count +=i
            log_print = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') +' ' +"[%s] %s\n" % (count, n)
            f = open(filename,'a',encoding='utf-8')
            f.write(log_print)
            f.close()
    if channel == 'both':
        while True:
            n = yield
            count +=i
            log_print = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') +' ' +"[%s] %s\n" % (count, n)
            f = open(filename,'a',encoding='utf-8')
            f.write(log_print)
            f.close()
            print(log_print)


# 调用
log_obj = logger(filename="web.log", channel='both')
log_obj.__next__()
log_obj.send('user')

log_obj.send('user feko')
log_obj.send('user feko login ')
log_obj.send('user feko login success')