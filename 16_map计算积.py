# -*- encoding:utf-8 -*- 

from functools import reduce
# 16.计算购买每支股票的总价
#    用filter过滤出，单价大于100的股票有哪些

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]


print(list(map(lambda x:x['shares']*x['price'],portfolio)))
print(list(filter(lambda x:x['shares']>100,portfolio)))


