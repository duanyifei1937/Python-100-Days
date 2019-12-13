# -*- coding: utf-8 -*-
# @Time    : 2019/12/12
# @Author  : Yifei Duan
# @Summary :

# a, b = 5, 10
# print('{} * {} = {}'.format(a, b, a * b))
# print('{0} * {1} = {2}'.format(a, b, a * b))
#
# # python3.6
# print(f"{a} * {b} = {a * b}")

# list1 = [1, 3, 5, 7, 100]
# for index, elem in enumerate(list1):
#     print(index, elem)

# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
#
# def enumerate(sequence, start=0):
#     n = start
#     for elem in sequence:
#         print(n)
#         yield n, elem
#         n += 1

#
# list = [1, 400, 5, 7, 100, 200, 1000, 2000]
# list.pop(2)
# print(list)


f = [x for x in range(1, 10)]
print(f)

# 交叉
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)