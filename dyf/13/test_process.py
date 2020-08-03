# -*- coding: utf-8 -*-
# @Time    : 2020/3/4
# @Author  : Yifei Duan
# @Summary :

# multiprocessing.py
import os

print('Process (%s) start...' % os.getpid())

pid = os.fork()

if pid == 0:
    # sub process:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    # father process, pid --> sub process;
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
