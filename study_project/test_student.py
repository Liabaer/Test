# -*- coding: utf-8 -*-
from study_project.test_case.student_test_case import Info
from study_project.test_api.student import Student

# 1. 返回该学生学号 （入参无）（返参 该类生成对象的学号）
no = Student()
print(no.no())
# 2. 返回该学生年龄 （入参无）（返参 该类生成对象的姓名）
age = Student()
print(age.age())
# 3. 打印该学生所有的信息详情（学号，年龄，年级，班级，学校名）（入参无）（返参无）
info = Student()
print(info.stinfo())
# 4. 判断输入的姓名是否和当前对象的用户名称一致 （入参输入的姓名）（返参true/false）
no = input()
isno = Student.isStudent(no)
print(isno)

# 1. 返回学校名 （入参无）（返参学校名）
print(Student.school)
# 2. 比较两个学生是否是同一个年级的（入参有2个，学生a对象，学生b对象）（返参 true/false)