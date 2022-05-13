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
# # (7）程序运行后产生的密码保存在“random_password.txt"文件中，每次允许代码不能覆盖原文件
# import random
# temp = 'abcdefghijkImnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*'
# random.seed(0x1010)
# dict_first_name = {}
# def create_pwd():
#     """
#     随机生成密码
#     :return:
#     """
#     ser = ''
#     i = 15
#     while i > 0:
#         ser += random.choice(temp)
#         i -= 1
#     return ser
#
# def be_pwd():
#     '''
#     判断首字母是否重复
#     :return:
#     '''
#     ser = ''
#     ls_ser = []
#     j = 10
#     while j > 0:
#         ser = create_pwd()
#         if ser[0] in dict_first_name:
#             continue
#         else:
#             dict_first_name[ser] = ser[0]
#         ls_ser.append(ser)
#         j -= 1
#     return ls_ser
# ls = be_pwd()
# print(ls)
#
# # print(be_pwd())
#
# f = open('random_password.txt', 'a')
# for i in ls:
#     m = list(i[5:10])
#     n = list(i[10:15])
#     m.sort()
#     n.sort(reverse=True)
#     # print(m, n)
#     res = i[0:5]+''.join(m)+''.join(n)
#     f.write('{}\n'.format(res))
#     print(res)
# f.close()

# 第四题
# 在_____上填写一行代码 从键盘输入一些字符，逐个把它们写到指定的文件，直到输入一个@为止
# 在...上补充一行或者多行代码
# filename = input("请输入文件名：\n")
# fp = open(filename, 'w')
# ch = input("请输入字符串：\n")
# while True:
#     if '@' in ch:
#         fp.write('{} '.format(ch))
#         break
#     else:
#         fp.write('{} '.format(ch))
#         ch = input("")
# fp.close()

# 第五题
# 某学习学生会共计有30名学生，学生信息存放在student_info.csv中，格式为姓名、学号、专业、年级。
# 现在需要从 大二和大三的学生中选举出一个部长和两个副部长，任意年级的人都权利投给任意年级的人一票，
# 如果投给大一或者 大四的则记为无效票得票数第一为部长，得票第二和三（可以并列）为副部长，题目数据保证只有一个最高票和一个 次高票。
# 投票结果存放在student_vote.txt中分别为投票时间、投票者姓名、被投票者姓名，职位名称(main表示部 长，Sub表示副部长)。
# 首先输出无效票数量、其次将副部长和部长的姓名、年级、专业、学号、得票数记录到 final_result.txt中。
# import csv
#
# f = open("student_info.csv", 'r')
# fi = csv.reader(f)
# lu = []
# info = {}
# for i in fi:
#     if i[3] == '大一' or i[3] == '大四':
#         lu.append(i[0])
#     # print(i)
#     info[i[0]] = i[1]+','+i[2]+','+i[3]
# f.close()
# # print(lu)
# # print(info)
#
# f = open('student_vote.txt', 'r')
# fv = f.readlines()
# res_dict = {}
# invalid_ticket = 0
# for i in fv:
#     i = i.strip()
#     temp = i.split(' ')[3]
#     if temp in lu:
#         invalid_ticket += 1
#         continue
#     if temp not in res_dict:
#         res_dict[temp] = 1
#     else:
#         res_dict[temp] = res_dict[temp] + 1
#     # print(temp)
# f.close()
# print('无效票数量为：{}'.format(invalid_ticket))
# print(res_dict)
# num = [v for k, v in res_dict.items()]
# # num2 = []
# res_main = max(num)
# num2 = num.copy()
# num2.remove(res_main)
# res_sub = max(num2)
#
# # 如果有两票相同，首先找出了次高票后，循环判断次高票是不是出现了2次，然后出现了2次，就把相同次高票的人都存入到数组里如下
# # 判断次高票出现了几次
# cnt = num2.count(res_sub)
# print(cnt)
# # 如果次高票没有出现2次，就找次次高票
# # 默认是-1
# res_sub_b = -1
# if cnt != 2:
#     num3 = num2.copy()
#     num3.remove(res_sub)
#     res_sub_b = max(num3)
# # 副部长名单
# res_sub_name_list = []
# res_main_name = ''
# for k, v in res_dict.items():
#     if v == res_main:
#         res_main_name = k
#     if v == res_sub:
#         res_sub_name_list.append(k)
#     if v == res_sub_b:
#         res_sub_name_list.append(k)
# print(res_sub_name_list, res_main_name)
#
# temp1 = info[res_main_name].split(',')
# temp2 = info[res_sub_name_list[0]].split(',')
# temp3 = info[res_sub_name_list[1]].split(',')
#
#
# # for k, v in res_dict.items():
# #     if v == res_main:
# #         res_main_name = k
# #     if v == res_sub:
# #         res_sub_name = k
# # print(res_sub_name, res_main_name)
# # print(res_dict)
# # 另一种方法使用sort排序
# # l_res = list(res_dict.items())
# # l_res.sort(key=lambda x:x[1],reverse=True)
# # fr = open('final_result.txt', 'w')
# # temp1 = info[l_res[0][0]].split(',')
# # temp2 = info[l_res[1][0]].split(',')
# # temp3 = info[l_res[2][0]].split(',')
# # print(l_res)
#
# fr = open('final_result.txt', 'w')
# # temp1 = info[res_main_name].split(',')
# # temp2 = info[res_sub_name].split(',')
# fr.write('副部长姓名1:{}、年级:{}、专业:{}、学号:{}、得票数:{}\n'.format(res_sub_name_list[0],temp2[2],temp2[1],temp2[0],res_sub))
# fr.write('副部长姓名2:{}、年级:{}、专业:{}、学号:{}、得票数:{}\n'.format(res_sub_name_list[1],temp3[2],temp3[1],temp3[0],res_sub_b))
# fr.write('部长姓名:{}、年级:{}、专业:{}、学号:{}、得票数:{}'.format(res_main_name,temp1[2],temp1[1],temp1[0],res_main))
# fr.close()


# # 第六题
# 你是否还记得下过雨之后的路面，水面斑驳的路面远处颜色深，近处颜 色浅。
# 使用turtle库的fd()、seth（)、pencolor0,pensize(0等函数和 random.库的randint()函数，在x坐标范围（-200,200)，y坐标范围 (-200,0)的一个长方形区域里，
# 绘制一个雨后路面的效果图。具体 而言，是在这个区域内画100条参数为随机值的横线，其长度在（20， 40)范围，画笔宽度在（1,4)范围，颜色值是在
# (-1/255,-200/255)范围内的灰度值，但色彩的深度与线条的y坐标值 相关，越靠下的线条颜色越浅，越靠上的线条颜色越深。效果如下图所 示。
# 在_____处填写一行代码
# 在….处填写多行代码
# import turtle as t
# import random
# for i in range(0, 100):
#     z = random.randint(0, 200)
#     g = z / 255
#     r = z / 255
#     b = z / 255
#     # 这里控制深浅
#     t.pencolor((r, g, b))
#     t.pensize(random.randint(1, 4))
#     x = random.randint(-200, 200)
#     y = random.randint(-200, 0)
#     t.penup()
#     # 前往坐标（x，y）往目标移动，如果这个时候笔还行落在画板上的，就会画一条前往x,y的线
#     t.goto(x, y)
#     t.pendown()
#     t.fd(random.randint(20, 40))
#     # t.seth(0)不需要这个，0就是向东，默认是向东的
# t.hideturtle()
# t.done()

# 第七题
# 注释：黄色小球的半径为20，红色小球的半径为45，蓝色小球的半径为 30。
# 因turtle颜色覆盖情况下的逻辑运算可能不同机器上效果不一样， 如果出现无法填充完整黄色小球，也是正确的。
# 在_____上完善一行代码
# import turtle as t
#
# t.penup()
# t.fd(-200)
# t.pendown()
# t.begin_fill()
# t.fillcolor('yellow')
# t.circle(20, 360 + 135)
# t.end_fill()
# t.right(90)
# t.fd(200)
# t.begin_fill()
# t.right(45)
# t.fillcolor('red')
# t.circle(45, 360)
# t.right(45)
# t.fd(200)
# t.left(-90)
# t.end_fill()
# t.begin_fill()
# t.fillcolor('blue')
# t.circle(30, 360)
# t.left(-45)
# t.end_fill()
# t.fd(282)
# t.hideturtle()
# t.done()

# 第八题
# 请用户输入中国一线城市和二线城市的城市名，城市名称之间用空格隔开。
# 将输入 的字符串转换为两个列表a和b,去除两个列表中重复出现的城市名称，北京 上海 广州 深圳 杭州

# 并把第一个 列表剩余的城市名称追加到第二个列表后面，保持原有城市的顺序，显示在屏幕 上。示例如下：
city1 = input("请输入一线城市").split()
city2 = input("请输入二线城市").split()
al = []
for i in city1:
    al.append(i)
bl = []
for i in city2:
    bl.append(i)
print(al)
print(bl)
# dict_b = {}
# for i in bl:
#     if i not in dict_b:
#         dict_b[i] = 1
#     else:
#         dict_b[i] = dict_b[i] + 1
# print(dict_b)
temp = al.copy()

for i in bl:
    if i in al:
        temp.remove(i)
res = bl+temp
print(res)


