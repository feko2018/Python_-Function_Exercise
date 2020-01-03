# -*- encoding:utf-8 -*-

import os


# 2、写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作
def md_file_contents(filename,old_str,new_str):
    old_file = filename
    old_file_bak = old_file + '_bak'
    new_file = old_file + '_new'
    f = open(old_file, 'r', encoding='utf-8')
    f_new = open(new_file, 'w',encoding='utf-8')

    for line in f:   # 遍历旧文件的每一行
        if old_str in line:   # 判断每一行中有没有这个字符串
            line = line.replace(old_str,new_str)  # 替换字符串
        f_new.write(line)  # 把替换好和不变的行重新写入新的文件
    f.close()
    f_new.close()
    os.remove(old_file_bak)
    os.rename(old_file, old_file_bak)
    os.rename(new_file, old_file)


md_file_contents('test01.txt','大龙', '小龙')
