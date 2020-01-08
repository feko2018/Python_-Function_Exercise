# -*- encoding:utf-8 -*-


# 6、写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
# 例如：[(‘红心’，2),(‘草花’，2), …(‘黑桃A’)]
def printed_playing_card_list():
    card = []
    for i in range(1,10):
        card.append(('红心', i))
        card.append(('草花', i))
        card.append(('方块', i))
        card.append(('黑桃', i))
    for j in ['A', 'J', 'Q', 'K']:
        card.append(('红心' + j))
        card.append(('草花' + j))
        card.append(('方块' + j))
        card.append(('黑桃' + j))
    return card


print(printed_playing_card_list())