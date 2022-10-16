# -*- coding: utf-8 -*-
from learn_project.my_project.test_case.student_test_case import Info
from learn_project.my_project.test_api.student import Student

test_case = Info.student_test_case()
test_case2 = Info.student_test_case2()
student = Student(no=test_case['no'], age=test_case['age'], grade=test_case['grade'], cls=test_case['cls'])
student2 = Student(no=test_case2['no'], age=test_case2['age'], grade=test_case2['grade'], cls=test_case2['cls'])

# 1. 返回该学生学号 （入参无）（返参 该类生成对象的学号）
print(student.get_no())
# 2. 返回该学生年龄 （入参无）（返参 该类生成对象的姓名）
print(student.get_age())
# 3. 打印该学生所有的信息详情（学号，年龄，年级，班级，学校名）（入参无）（返参无）
student.st_info()
# 4. 判断输入的姓名是否和当前对象的用户名称一致 （入参输入的姓名）（返参true/false）
print(student.is_no(1))
# 1. 返回学校名 （入参无）（返参学校名）
print(Student.get_school())
# 2. 比较两个学生是否是同一个年级的（入参有2个，学生a对象，学生b对象）（返参 true/false)
print(Student.is_grade(student, student2))
