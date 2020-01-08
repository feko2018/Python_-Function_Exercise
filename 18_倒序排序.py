# -*- encoding:utf-8 -*-

# 18、有列表 li = ['feko', 'nooee', 'biga', 'pllz', 'feko1'], 请以列表中每个元素的第二个 字母倒序排序；

li = ['feko', 'nooee', 'biga', 'pllz', 'feko1']

tmp = ''
li_tmp = []
for i in li:
    tmp = i[0] + ''.join(reversed(i[1:]))
    li_tmp.append(tmp)
print(li_tmp)