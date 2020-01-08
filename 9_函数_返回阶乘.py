# -*- encoding:utf-8 -*-

# 9、写函数，传入一个参数n，返回n的阶乘
# 例如:cal(7)
# 计算7654321

def cal(num):
    product = 1
    g = (num-x for x in range(num))
    for i in g:
         product *=i
    return product

print(cal(5))