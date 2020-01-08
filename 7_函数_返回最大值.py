# -*- encoding:utf-8 -*-

# 7、写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
# 例如:minmax(2,5,7,8,4)
# 返回:{‘max’:8,’min’:2}


def minmax(*args):
    number = args
    max_int = number[0]
    min_int = number[0]
    for i in number:
        if i > max_int:
            max_int = i
        if i < min_int:
            min_int = i
    return {'max': max_int, 'min': min_int}


print(minmax(5,100,3,1,2,3,10,0))