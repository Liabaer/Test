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
# # 问题1：求出缺勤考 试的名单存入un_score_.student.txt。
# import csv
# #
# lun = []
# fc = open('class-data(1).csv', 'r')
# fc.seek(53)
# fcn = csv.reader(fc)
# # count = 0
# ls_class = []
# for i in fcn:
#     # i是每一列csv的数组
#     j = i[1]
#     # count += 1
#     lun.append(j)
#     temp = [i[3], i[1], i[4], i[2]]
#     ls_class.append(temp)
#     # print(i)
# fc.close()
# # print(lun)
# print(ls_class)
#
# fs = open('student-name(1).txt', 'r')
# fs.seek(9)
# fsn = fs.readlines()
# ln = []
# la = []
# num = 0
# cnt = 0
# dic_student = {}
# for i in fsn:
#     i = i.strip()
#     if i != '':
#         name = i.split(' ')[0]
#         age = i.split(' ')[1]
#         dic_student[name] = age
#         num += int(age)
#         cnt += 1
#         if name not in lun:
#             ln.append(name)
#         la.append(age)
#     # print(i)
# fs.close()
# print(dic_student)
# print(ln)

# 问题2：统计学生的平均年龄、最大年龄和最小年龄。
# print("最大年龄：{}，最小年龄：{}，平均年龄：{:.2f}".format(max(la), min(la), num/cnt))

# 问题3：存储新的文件class-data-age.csv,文件记录iD、姓名、年龄、注册时间和班级，按照班级进行排序，班级相同，按照年龄升序排列

# for i in ls_class:
#     name = i[1]
#     age = dic_student[name]
#     i.insert(2, age)
# print(ls_class)
# ls_class.sort(key=lambda x: (x[4], x[2]) )
# print('---', ls_class)
# f_new = open('class-data-age.csv', 'w')
# f_new_w = csv.writer(f_new)
# f_new_w.writerow(['ID', '姓名', '年龄', '注册时间', '班级'])
# i = 0
# while i < len(ls_class):
#     f_new_w.writerow(ls_class[i])
#     i += 1
# f_new.close()

#
# 第三题
# 请编写程序，生成随机密码。具体要求如下：
# (1)使用random库，采用0x1010作为随机数种子。
# (2)密码abcdefghijkImnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*中的字符组 成。
# (3)每个密码长度固定为15个字符
# (4)程序运行每次产生10个密码，每个密码一行。
# (5)每次产生的10个密码首字符不能一样。
# (6) 密码的中间五位按照scⅱ码从小到大排序，最后五位从大到小排序，排序后如果生成的密码出现过，则继续随机 密码，然后排序直到该密码没有出现过。
# (7）程序运行后产生的密码保存在“random_password.txt"文件中，每次允许代码不能覆盖原文件
import random
temp = 'abcdefghijkImnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*'
random.seed(0x1010)
dict_first_name = {}
def create_pwd():
    """
    随机生成密码
    :return:
    """
    ser = ''
    i = 15
    while i > 0:
        ser += random.choice(temp)
        i -= 1
    return ser

def be_pwd():
    '''
    判断首字母是否重复
    :return:
    '''
    ser = ''
    ls_ser = []
    j = 10
    while j > 0:
        ser = create_pwd()
        if ser[0] in dict_first_name:
            continue
        else:
            dict_first_name[ser] = ser[0]
        ls_ser.append(ser)
        j -= 1
    return ls_ser
ls = be_pwd()
print(ls)

# print(be_pwd())

f = open('random_password.txt', 'a')
for i in ls:
    m = list(i[5:10])
    n = list(i[10:15])
    m.sort()
    n.sort(reverse=True)
    # print(m, n)
    res = i[0:5]+''.join(m)+''.join(n)
    f.write('{}\n'.format(res))
    print(res)
f.close()