# -*- encoding:utf-8 -*-

# 25、题目：写一个摇骰子游戏，要求用户压大小，赔率一赔一。要求：三个骰子，每个骰子的值从1-6，摇大小，每次打印摇出来3个骰子的值。

import random


def play_dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)
    print(dice1)
    print(dice2)
    print(dice3)


play_dice()