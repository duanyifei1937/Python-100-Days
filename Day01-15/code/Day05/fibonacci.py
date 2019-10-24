"""
输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

a = 0
b = 1
for _ in range(20):
<<<<<<< HEAD:Day01-15/Day05/code/fibonacci.py
    (a, b) = (b, a + b)
=======
    a, b = b, a + b
>>>>>>> upstream/master:Day01-15/code/Day05/fibonacci.py
    print(a, end=' ')
