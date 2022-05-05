# -*- coding: utf-8 -*-
# 使用字典和列表完成学生通讯录管理，名单由文件address.txt给出，每行是一个学 生的信息。示例如下：学号，姓名，电话号码，地址
# 问题1：在屏幕上显示功能菜单，功能菜单示例如下：
# 1。显示所有信息
# 2. 追加信息
# 3. 删除信息
# 请输入数字1-3选择功能：
# 请输入数字1-3选择功能（要求：不允许浮点数输入）：
# 接收用户输入数字选择功能，如果输入错误，要求用户重新输入。
# 如果输入正确，在屏幕上显示提示语句： 您选择了功能1/2/3。(5分)
# import random
#
# # 问题2：在问题1的代码基础上，当用户选择1的时候，从通讯录文件读取信息，并显 示所有信息。(5分)示例如下：
# def read():
#     l = []
#     f = open('address.txt', 'r+')
#     fr = f.readlines()
#     for i in fr:
#         i = i.strip()
#         l.append(i)
#     f.close()
#     return l
#
# read()
#
# def show():
#     l_s = read()
#     for i in l_s:
#         print(i)
#
#
# # 问题3：在问题2的代码基础上，当用户选择3的时候， 删除文件最后一行数据，如 果文件无内容，则提示当前文件为空无法删除。
# def delete():
#     l_d = read()
#     # if len(l_d) != 0:
#     #     l_d.pop(len(l_d) - 1)
#     #     print(l_d)
#     # else:
#     #     print('当前文件为空无法删除。')
#     f_d = open('address.txt', 'w')
#     for i in l_d:
#         i = i.strip()
#         if len(i) == 0:
#             print('当前文件为空无法删除。')
#         elif i != l_d[len(l_d)-1]:
#             f_d.write(i+'\n')
#     f_d.close()
#
#
# # 问题4：在问题2的代码基础上，当用户选择2的时候，名字随机a到z之间的字母，
# # 长度为6，学号随机100到200之间的整数，电话长度为11位随机数字，地名随机北京，上海，深圳中的一个，用逗号隔开，追加到新文件未尾，控制台提示追加成功
#
# def add():
#     zmb = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
#            'w', 'x', 'y', 'z']
#     num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     city = ['北京', '上海', '深圳']
#     name = ''
#     new_city = ''
#     phone = ''
#     no = random.randint(100, 200)
#     j = 11
#     while j != 0:
#         phone += random.choice(num)
#         j -= 1
#     i = 6
#     while i != 0:
#         name = name + random.choice(zmb)
#         i -= 1
#     new_city = random.choice(city)
#     f_new = open('address.txt', 'a+', encoding='utf-8')
#     f_new.write('{},{},{},{}\n'.format(name, no, phone, new_city))
#     print('追加成功!')
#     f_new.close()
#
#
# q_dict = {1: '显示所有信息', 2: '追加信息', 3: '删除信息'}
#
#
# def q_ans():
#     while True:
#         q = input('1.显示所有信息\n2. 追加信息\n3. 删除信息\n请输入数字1-3选择功能：')
#         if q == '1':
#             print('您选择了功能:{}'.format(q_dict[1]))
#             show()
#             break
#             # return q
#         elif q == '2':
#             print('您选择了功能:{}'.format(q_dict[2]))
#             add()
#             break
#             # return q
#         elif q == '3':
#             print('您选择了功能:{}'.format(q_dict[3]))
#             delete()
#             break
#             # return q
#         else:
#             print('输入错误，请重新输入：')
#
#
# q_ans()


# # 第二题
# 使用字典和列表型变量完成某课程的考勤记录统计，某班有20名同学，姓名和年龄存储 在student--name.txt,某课程第一次考勤数据存储在class-data.csv中。
# 问题1：求出缺勤考 试的名单存入un_score_.student.txt。
import csv
#
lun = []
fc = open('class-data(1).csv', 'r')
fc.seek(53)
fcn = csv.reader(fc)
# count = 0
for i in fcn:
    # i是每一列csv的数组
    j = i[1]
    # count += 1
    lun.append(j)
    print(j)
fc.close()
print(lun)

fs = open('student-name(1).txt', 'r')
fs.seek(9)
fsn = fs.readlines()
ln = []
la = []
num = 0
cnt = 0
for i in fsn:
    i = i.strip()
    if i != '':
        name = i.split(' ')[0]
        age = i.split(' ')[1]
        num += int(age)
        cnt += 1
        if name not in lun:
            ln.append(name)
        la.append(age)
    # print(i)
fs.close()
print(ln)
print("最大年龄：{}，最小年龄：{}，平均年龄：{:.2f}".format(max(la), min(la), num/cnt))


# 问题2：统计学生的平均年龄、最大年龄和最小年龄。

# 问题3：存储新的文件class-data-age.csv,文件记录D、姓名、年龄、注册时间和班级，按 照班级进行排序，班级相同，按照年龄升序排列
