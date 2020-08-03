# -*- coding: utf-8 -*-
# @Time    : 2020/1/15
# @Author  : Yifei Duan
# @Summary :


# 读取文件内容，存放到list
def readlog():
    with open('log', 'r') as f:
        lines = f.readlines()
    print(lines)


if __name__ == '__main__':
    readlog()
