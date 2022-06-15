# -*- coding: utf-8 -*-
# 1. 定义一个学生类 放入student.py
#     1. 私有字段 (都为选填参数）
#         1. 学号
#         2. 年龄
#         3. 年级
#         4. 班级
#     2. 公有字段
#         1. 学校名（初始化为python_school)
#     3. 私有函数
#         1. 返回该学生学号 （入参无）（返参 该类生成对象的学号）
#         2. 返回该学生年龄 （入参无）（返参 该类生成对象的姓名）
#         3. 打印该学生所有的信息详情（学号，年龄，年级，班级，学校名）（入参无）（返参无）
#         4. 判断输入的姓名是否和当前对象的用户名称一致 （入参输入的姓名）（返参true/false）
#     4. 公有函数
#         1. 返回学校名 （入参无）（返参学校名）
#         2. 比较两个学生是否是同一个年级的（入参有2个，学生a对象，学生b对象）（返参 true/false)
#
# 定义一个test_student.py中需要调用类的所有函数,判断是否有误
from study_project.test_case.student_test_case import Info

class Student(object):
    school = "python_school"

    def __init__(self):
        self.no = ''
        self.age = ''
        self.grade = ''
        self.cls = ''

    def no(self):
        return self.no

    def age(self):
        return self.age

    def stinfo(self):
        dic = Info.student_test_case()
        for i in dic:
            print('{}:{}'.format(i, dic[i]))

    def isStudent(self, name):
        dic = Info.student_test_case()
        for i in dic:
            if i == 'name':
                na = dic[i]
        return name == na

    @staticmethod
    def school():
        return Student.school

    @staticmethod
    def isgrade(a, b):

        return a==b