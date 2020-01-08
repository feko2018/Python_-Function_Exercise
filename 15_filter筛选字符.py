# -*- encoding:utf-8 -*-


# 15、用filter函数处理数字列表，将列表中所有的偶数筛选出来
# - num = [1,3,5,6,7,8]
num = [0,1,3,2,10,33,22,5,6,7,8]
num1 = list(filter(lambda x: x % 2 == 0, num))
print(num1)