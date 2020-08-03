# -*- coding: utf-8 -*-
# @Time    : 2019/12/12
# @Author  : Yifei Duan
# @Summary :


scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}


for i in scores.values():
    print(i)



for i, j in scores.items():
    print("{} -- {}".format(i, j))