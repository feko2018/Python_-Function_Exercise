# -*- encoding:utf-8 -*-


# 20、有名为username.txt的文件，其内容格式如下，写一个程序，判断该文件中是否存在”feko”, 如果没有，则将字符串”feko”添加到该文件末尾，否则提示用户该用户已存在；
#
# pllz
# feko
# nooee

f = open('username.txt',"r+",encoding='utf-8')
if 'feko' in f.read():
    print("feko 已经存在，exit")
else:
    f.write('\nfeko')
f.close()