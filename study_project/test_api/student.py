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
#         4. 判断输入的学号是否和当前对象的学号名称一致 （入参输入的学号）（返参true/false）
#     4. 公有函数
#         1. 返回学校名 （入参无）（返参学校名）
#         2. 比较两个学生是否是同一个年级的（入参有2个，学生a对象，学生b对象）（返参 true/false)
#
# 定义一个test_student.py中需要调用类的所有函数,判断是否有误
from study_project.test_case.student_test_case import Info


class Student(object):
    school = "python_school"

    def __init__(self, no='', age=0, grade='', cls=''):
        self.no = no
        self.age = age
        self.grade = grade
        self.cls = cls

    def get_no(self):
        return self.no

    def get_age(self):
        return self.age

    def st_info(self):
        print('{},{},{},{}'.format(self.no, self.age, self.grade, self.cls))

    def is_no(self, no):
        return self.no == no

    @staticmethod
    def get_school():
        return Student.school

    @staticmethod
    def is_grade(a, b):
        return a.grade == b.grade


test_case = Info.student_test_case()
test_case2 = Info.student_test_case2()
student = Student(no=test_case['no'], age=test_case['age'], grade=test_case['grade'], cls=test_case['cls'])
student2 = Student(no=test_case2['no'], age=test_case2['age'], grade=test_case2['grade'], cls=test_case2['cls'])
student.st_info()

print(student.get_no())
print(student.get_age())
print(student.is_no(1))
print(Student.get_school())
print(Student.is_grade(student, student2))
