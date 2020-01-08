# -*- encoding:utf-8 -*-

# 17、有列表 li = ['feko', 'nooee', 'biga', 'pllz', 'feko1'], 请将以字母“f”开头的元素的 首字母改为大写字母；

li = ['feko', 'nooee', 'biga', 'pllz', 'feko1']

tmp = ''
li_tmp = []
for i in li:
    if i[0] == 'f':
        tmp = i[0].upper() + i[1:]
    else:
        tmp = i
    li_tmp.append(tmp)
li = li_tmp
print(li)