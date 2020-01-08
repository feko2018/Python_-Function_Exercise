#  -*- encoding:utf-8 -*-

import  os
# 21、有名为user_info.txt的文件，其内容格式如下，写一个程序，删除id为100003的行；
#
# pllz,100001
# # feko, 100002
# # nooee, 100003

old_file = 'user_info.txt'
new_file = old_file + '_new'
old_f = open(old_file, 'r', encoding='utf-8')
new_f = open(new_file, 'w', encoding='utf-8')

for line in old_f:
    if '100002' in line:
        line = 'feko li, 100002'
    new_f.write(line)

old_f.close()
new_f.close()
os.replace(new_file, old_file)

