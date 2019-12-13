# -*- coding: utf-8 -*-
# @Time    : 2019/12/12
# @Author  : Yifei Duan
# @Summary :
# 斐波那契数列: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。

a = 1
b = 1
print(a)
print(b)

for i in range(10):
    c = a + b
    a = b
    b = c
    print(c)
