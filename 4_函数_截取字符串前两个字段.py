# -*- encoding:utf-8 -*-


# 4、写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容 （对value的值进行截断），
#   并将新内容返回给调用者，注意传入的数据可以是字符、list、dict


def cut_str(string):
    if len(string) > 2:
        return string[:2]


print(cut_str([1, 2, 3, 4]))
