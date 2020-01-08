# -*- encoding:utf-8 -*-

# 14、用map来处理字符串列表,把列表中所有人都变成sb,比方alex_sb
# name=[‘feko’,’wupeiqi’,’yuanhao’,’nezha’]
name = ['fako', 'wupeiq', 'yuanhao', 'nezha']
name = list(map(lambda x: x+'_sb', name))
print(name)