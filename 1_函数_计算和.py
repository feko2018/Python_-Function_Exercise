# -*- encoding:utf-8 -*-


# 1、写函数，计算传入数字参数的和。（动态传参）
def cal_sum(*args):
    sum = 0
    for i in args:
        sum = int(i) + sum
    return sum
#    return sum(args)


print(cal_sum(1,2,3,4))
