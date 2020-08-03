# -*- coding: utf-8 -*-
# @Time    : 2020/1/19
# @Author  : Yifei Duan
# @Summary :


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print("{} studing {}".format(self.name, course_name))

    def movie(self):
        if self.age > 18:
            print('ok')
        else:
            print('no')


if __name__ == '__main__':
    stu1 = Student('zhangsan', 12)
    stu1.study('english')

    stu2 = Student('lisi', 11)
    stu2.movie()

