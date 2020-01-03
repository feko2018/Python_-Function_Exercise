# -*- encoding:utf-8 -*-


# 3、写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容。
def chk_str_list_tuple(str_list_tuple):
    for i in str_list_tuple:
        if i == " ":
            print("有空格")
            return 2
            break
    return 1


chk_str_list_tuple("abc d")
