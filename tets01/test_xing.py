# -*- coding: utf-8 -*-
# @Time    : 2019/5/11
# @Author  : Yifei Duan
# @Summary :

"""
*
**
***
****
*****
"""

row = int(input("Please input row number: "))
for i in range(row):
    for j in range(i + 1):
        print('*', end='')
    print('\n', end='')
