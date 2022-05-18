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

# # 并把第一个 列表剩余的城市名称追加到第二个列表后面，保持原有城市的顺序，显示在屏幕 上。示例如下：
# city1 = input("请输入一线城市").split()
# city2 = input("请输入二线城市").split()
# al = []
# for i in city1:
#     al.append(i)
# bl = []
# for i in city2:
#     bl.append(i)
# print(al)
# print(bl)
# # dict_b = {}
# # for i in bl:
# #     if i not in dict_b:
# #         dict_b[i] = 1
# #     else:
# #         dict_b[i] = dict_b[i] + 1
# # print(dict_b)
# temp = al.copy()
#
# for i in bl:
#     if i in al:
#         temp.remove(i)
# res = bl+temp
# print(res)

# 第九题
# 获得用户输入的一个整数，参考该整数值，打印输出"Hello World",要求：
# 如果输入值是0，直接输出"Hello World"
# 如果输入值大于0，以两个字符一行方式输出"Hello World"（(空格也是字符)
# 如果输入值小于0，以垂直方式输出"Hello World"
# ans = "Hello World"
# res = eval(input('请输入一个整数：'))
# if res == 0:
#     print(ans)
# elif res < 0:
#     for i in ans:
#         print(i)
# else:
#     i = 0
#     j = 2
#     while i < len(ans):
#         print(ans[i:j])
#         i = j
#         j += 2

# 第十题
# 以整数17为随机数种子，获取用户输入整数N为长度，产生3个长度为N位的密
# 码，密码的每位是一个数字。每个密码单独一行输出。
# 产生密码采用random.randint()函数。
# import random
# l = eval(input('请输入一个整数：'))
# random.seed(17)
# for i in range(0, 3):
#     res = ''
#     for j in range(0, l):
#         res += str(random.randint(0, 9))
#     print(res)

# #请在...和____补充代码
# import random
#
# def genpwd(length):
#     random.seed(17)
#     res = ''
#     for i in range(0, length):
#         res += str(random.randint(0, 9))
#     return res
#
#
# length = eval(input('请输入一个整数：'))
# ans = genpwd(length)
# for i in range(0, 3):
#     print(ans)

# 第十题
# 获得用户输入数字N,计算并输出从N开始的5个质数，单行输出，质数间用逗
# 号，分割。
# 注意：需要考虑用户输入的数字N可能是浮点数，应对输入取整数；最后一个输出后不用逗号。

# 请在...补充一行或多行代码
# 质数（素数）：除了1和他本身，无法被其他数字整除，比如5，5的公约数只有1和5，所以是质数，比如4公约除了1和4还有2，所以4是合数。
#
# def prime(m):
#     flag = True
#     for n in range(2, m):
#         if m % n == 0:
#             flag = False
#             break
#     if flag:
#         return m
#
#
# # print(prime(4))
#
# n = eval(input())
# ans = ''
# for i in range(1, n+1):
#     res = prime(i)
#     if res is not None:
#         ans += str(res) + ','
# l = len(ans)
# print(ans[0:l-1])
#
# 另一种方式判断是否第一次出现
# flag = True
# n = 5
# for i in range(1, n + 1):
#     res = prime(i)
#     if res is not None:
#         print(str(res), end='') if flag else print(',' + str(res), end='')
#         flag = False

# 第十一题
# 获得输入的一个字符串$，以字符减号(-)分割$，将其中首尾两段用加号(+)组合 后输出。Alice-Bob-Charis-David-Eric-FLurry
# s = input('请输入字符串：')
# ls = s.split('-')
# print(ls[0]+'+'+ls[len(ls)-1])
#
# 获得用户输入的一个整数a,计算a的平方根，保留小数点后3位，并打印输出。
# 输出结果采用宽度30个字符、右对齐输出、多余字符采用加号(+)填充。
# 如果结果超过30个字符，则以结果宽度为准。
# a = eval(input('请输入整数：'))
# print('{:+>30.3f}'.format(pow(a, 1/2)))

# 第十二题
# 使用turtle库，绘制一个八角图形。
# 注意：这是一个自动评阅题目，请补充"编程模板"中横线内容，横线不保 留。
# import turtle as t
# t.pensize(2)
# for i in range(0, 8):
#     t.fd(100)
#     t.left(135)

# 第十三题
# 1,转子热套,9,4
# 第1列是序号第2列的工序名称第3列是生产该工序所需要的节拍数，第4列是生产设备的数量。
# 请读取文件，并统计所有生产设备的总数，以及所有工序所需要的平均 节拍数，并统计大于和小于平均节拍数的工序的个数。
# 在_____处填写一行代码
# 在….处填写多行代码

# te, tslic, cnt, prol = 0, 0, 0, []
# with open("data-work.csv", 'r') as f:
#     for l in f.readlines():
#         pros = l.split(',')
#         prol.append((pros[0], pros[1], pros[2], pros[3]))
#
# cnt = len(prol)
# for i in prol:
#     tslic += int(i[2])
#     te += int(i[3])
# meansl = tslic//cnt
# bigp, littlep = 0, 0
# for p in prol:
#     if int(p[2]) < meansl:
#         littlep += 1
#     if int(p[2]) > meansl:
#         bigp += 1
#
# print('所有生产设备的总数是：{}个，平均节拍数是: {}'.format(te, meansl))
# print('大于平均节拍数的工序有{}个，小于平均节拍数的工序有{}个'.format(bigp, littlep))

# #第十四题
# 接收用户输入的一串密钥序列号，显示序列号的内容，并检查序列号是否满足下述 条件： NAaG-UJ8Z-EVAP-JAUW NAAG-UJ8ZE-VAP-JAUW
# 1）如果字符串的总长度不是19位，就显示'序列号长度非法'；
# 2）要求被3个连字符连接，三个分隔符正好将序列号分割为四组，并且每组是四个 大写字符或者数字。如果三个分隔符的位置不对，
# 就显示分隔符位置非法'；如果字 符不是大写字母或者不是数字，就显示字符不是大写或数字；
# 3) 如果符合条件，就显示'序列号正确'。

# 在_____处填写一行代码
# 在….处填写多行代码
#
# ss = input()
# temp = ss.split('-')
#
# if len(ss) != 19:
#     print('序列号长度非法')
#
# flag = True
# for i in temp:
#     print(i)
#     if len(i) != 4:
#         print('分隔符位置非法')
#         break
#     for j in i:
#         if ord('A') > ord(j) < ord('Z') or ord('0') > ord(j) > ord('9'):
#             flag = False
# # 这中for else写法可以解决上面打印后下面判断又重复打印，且flag不够用的情况 还可以使用flag == 1， flag ==2，flag ==3 给flag重新定义的方式
# else:
#     if flag:
#         print('序列号正确')
#     else:
#         print('字符不是大写或数字')

# 第十五题
# 获得用户的任何可能输入，将其中的英文字符进行打印输出，程序不出现 错误。
# alpha = []
# for i in range(26):
#     alpha.append(chr(ord('A')+i))
#     alpha.append(chr(ord('a')+i))
# # print(alpha)
# s = input()
# for c in s:
#     if c in alpha:
#         print(c, end='')
#
# 第十六题
# 获得用户输入的一个字符串，格式如下：
# M OP N
# 其中，M和N是任何数字，OP代表一种操作，表示为如下四种：+，-，*/（加减
# 乘除)
# 根据OP,输出MOPN的运算结果，统一保存小数点后2位。
# 注意：M和OP、OP和N之间可以存在多个空格，不考虑输入错误情况。

# s = eval(input("请输入字符串："))   # 不用想复杂了喂
# # temp = s.split(' ')
# # opt = ['+', '-', '*', '/']
# # m = temp[0]
# # op = temp[1]
# # n = temp[2]
# print('{:.2f}'.format(s))

# 十七题
# 获得用户输入的一个整数N,输出N中所出现不同数字的和。
# 例如：用户输入123123123，其中所出现的不同数字为：1、2、3，这几个 数字和为6。
# n = input()
# ss = set(i for i in n)
# s = 0
# for i in ss:
#     s += int(i)
# print(s)

# 十八题
# 获得用户的输入，当作对齐模式，用户输入：左、右、中，分别表示： 左对齐、右对齐和居中对齐，以*作为填充符号30字符宽度输出
# PYTHON:字符串。无任何输入时，默认为左对齐，请参考编程模板，完
# 善代码。本题目支持OJ在线评测。

#请输入对齐模式：
#在_______上完善一行代码
# m = input("")
# s = "PYTHON"
# if  m =="右":
#     m = ">"
# elif m =="中":
#     m = '^'
# else:
#     m = '<'
# # 或者{1:*{0}30}.format(m,s) 使用1，0来指定format里的顺序
# print('{:*{}30}'.format(s, m))

# 十九题
# 完善代码，输出如下图的田字符形状。
#在_______上填写一行代码
# for i in range(11):
#     if i in (0,5,10):
#         print("* - - - * - - - *")
#     else:
#         print("*       *       *")

# 二十题
# 四位玫瑰数是4位数的自幂数。自幂数是指一个位数，它的每个位上的数字的次幂之和等于它本身。
# 例如：当n为3时，有1^3+5^3+3^3=153,153即是n为3时的一个自幂 数，3位数的自幂数被称为水仙花数。
# 请输出所有4位数的四位玫瑰数，按照从小到大顺序，每个数字一行。

# s = ""
# for i in range(1000, 9999):
#     t = str(i)
#     if pow(int(t[0]), 4)+pow(int(t[1]), 4)+pow(int(t[2]), 4)+pow(int(t[3]), 4) == i:
#         print(i)

# 二十一
# 求100以内所有素数之和并输出。
# 素数指从大于1，且仅能被1和自己整除的整数。
# 提示：可以逐一判断100以内每个数是否为素数，然后求和。
#Prime
# def is_prime(n):
#     for i in range(2, n-1):
#         if n%i == 0:
#             return False
#     return True
# sum = 0
# # 不从0开始，0是素数
# for i in range(1, 100):
#     if is_prime(i):
#         sum += i
# print(sum)

# 二十二
# 获得用户输入的一个数字，可能是浮点数或复数，如果是整数仅接收十进 制形式，且只能是数字。对输入数字进行平方运算，输出结果。
# (1)无论用户输入何种内容，程序无错误；
# (2)如果输入有误，请输出"输入有误"。



# def is_num(a):
#     for i in a:
#         if ord('0') > ord(str(i)) > ord('9'):
#             return False
#         else:
#             return True
# if not is_num(s):
#     print("输入有误")
# else:
#     print(pow(s, 2))
# s = input()
# try:
#     print(pow(eval(s), 2))
# except:
#     print("输入有误")
#

# 二十三
# import turtle
# for i in range(0,8):
#     turtle.fd(100)
#     turtle.left(45)

# # 二十五
# 使用turtle库，绘制一个风轮效果，其中，每个风轮内角为45度，风轮边长150像素。
# 注意：这不是自动评阅题目，仅用于练习，没有评阅。
# 提示：turtle.goto(X,y)函数，能够将turtlei画笔移动到坐标(x,y)
# import turtle as t
# t.pensize(2)
# for i in range(4):
#     t.seth(i*90)
#     t.fd(150)
#     t.right(90)
#     t.circle(-150, 45)
#     t.goto(0, 0)

# 二十六
# 使用turtle库，绘制一个叠边形，其中，叠边形内角为100度。
# import turtle as t
# t.pensize(2)
# for i in range(9):
#     t.fd(100)
#     t.left(80)

# 二十七
# data-name-list.txt中包含了含有重复的人名，请直接输出出现最多的人 名。
# f = open('data-name-list.txt', 'r')
# s = f.read()
# # print(s)
#
# ls = s.split()
# # print(ls)
# d = {}
# for i in ls:
#     d[i] = d.get(i, 0) + 1
# max_name, max_cnt = '', 0
# for k in d:
#     # print(k)
#     if d[k] > max_cnt:
#         max_name, max_cnt = k, d[k]
# print(max_name)

# 二十八
# 使用turtle库的fd)、seth(O、pencolor()、backward()、right()、 screensize0等函数，
# 以及random随机函数库的seed(),randint(), choice()函数，绘制n个彩色的蒲公英小伞。
# 小伞的颜色在给定的颜色列 表color中随机选择；伞J顶半径画笔宽1个像素长edge个像素，
# edge取值 在(20,30)范围里随机选择：伞柄画笔宽5个像素长handle个像素，handle 取值在(30,50)范围里随机选择；
# 小伞的伞柄与伞顶交点的位置在画布上
# 随机分布；画布的X轴坐标取值在(-200,200)范围里随机选择，Y轴坐标
# 取值在（-100,100)范围里随机选择。的值由用户输入，其他值由代码 模板给出。当用户输入6的时候，效果如下图所示。
import csv
import random
# import turtle as t
# from random import *
#
#
# def oneDandelion(x0, y0, color, edge, handle):
#     """
#     绘制一个蒲公英，在(x,y)的位置画一个颜色为color，边长为edge，根长为handle的蒲公英
#     :param x0: 横坐标
#     :param y0: 纵坐标
#     :param color: 颜色
#     :param edge: 边长
#     :param handle: 根长
#     :return:
#     """
#     # 起笔
#     t.penup()
#     # 移动到x,y位置
#     t.goto(x0, y0)
#     # 落笔 准备开始绘制
#     t.pendown()
#     # 设置颜色
#     t.pencolor(color)
#     # 设置根的方向，需要朝上，也就北方
#     t.seth(90)
#     # 设置根的宽度
#     t.pensize(5)
#     # 把根画出来
#     t.fd(handle)
#     # 设置方向开始画边长
#     t.seth(250)
#     # 设置边长的宽度为1
#     t.pensize(1)
#     for i in range(33):
#         # 往返画边长
#         t.fd(edge)
#         t.backward(edge)
#         # 每次移动10度
#         t.right(10)
#
#
# color = ['red', 'pink', 'green', 'violet', 'purple']
# seed(20)
# t.screensize(400, 200, "#E0FFFF")
# n = eval(input())
# for i in range(n):
#     edge = randint(20, 30)  # 蒲公英的边长
#     handle = randint(30, 50)  # 蒲公英的根长
#     oneDandelion(randint(-200, 200), randint(-100, 100), choice(color), edge, handle)
# t.done()


# 二十九
# 补全编程模板中的代码，删除横线，补全代码，可以修改其他代码。 实现以下功能
# 键盘输入一个字符串空格分割，内容为专业名称。
# 统计专业名称 出现的数量，按数量从高到低方式输出，名称不足五位使用等号居左对齐 计算机 计算机 计算机 软件 软件 软件 软件 财务 管理 管理
# names = input("")
# n = names.split(' ')
# d = {}
# for i in n:
#     d[i] = d.get(i, 0)+1
# ls = list(d.items())
# ls.sort(key=lambda x: x[-1], reverse=True)
# print(ls)
# for k in ls:
#     # 这里k是元祖哦记得
#     print('{:=<5}:{}'.format(k[0], k[1]))

# 三十
# 读入一个字典类型的字符串，反转其中键值对输出。
# 即，读入字典key:value模式，输出value:key模式。
# 输入格式
# 用户输入的字典格式的字符串，如果输入不正确，提示：输入错误。{"a":1,"b":2}
# 输出格式
# 给定字典d,按照print(d)方式输出
# s = input()
# try:
#     d = eval(s)
#     e = {}
#     for k in d:
#         e[d[k]] = k
#     print(e)
# except:
#     print("输入错误")

# 三十一
# 获得用户输入，去掉其中全部空格，将其他字符按收入顺序打印输出。 Alice + Bob
# txt = input()
# # print(txt.replace(' ', ''))
# print("".join(txt.split(" ")))
#
# # 三十二
# # 键盘输入正整数n,按要求把n输出到屏幕，格式要求：宽度为20个字符，数字中间 对齐，不足部分用=填充，如果输入的不是数字，则提示输入错误。
#
# n = input()
# try:
#     m = eval(n)
#     print('{:=^20}'.format(m))
# except:
#     print('输入错误')

# 三十三
# 键盘输入一段文本，使用jieba分词文本，并且使用字典统计每个词语出现的次数，
# import jieba
#
# s = input("请输入一个字符串:")
# m = jieba.lcut(s)
# dict_text = {}
# for i in m:
#     dict_text[i] = dict_text.get(i, 0)+1
# for i in dict_text:
#     print(i, dict_text[i])

# 三十四
# 请写代码替换模板中的横线，不得修改其他代码，
# 实现以下功能：键盘输入正整数 n,按要求把n输出到屏幕上，
# 格式要求：宽度为20个字符，减号字符-填充，右对 齐，带千位分隔符。
# 如果输入正整数超过20位，则按照实际长度输出。

# # 千分分隔符：比如数字1234，在千分位上加上逗号1,234，比如12345678，123,456,789
# # 实现方法，使用,d的写法。print("{:,d}".format(123456))
# n = eval(input("请输入一个正整数:"))
# print('{:->20,d}'.format(n))

# 三十五
# 键盘输入一组人员姓名、工作、性别、工资等信息，信息间采用空格分隔，每人一 行，空行回车结束录入，示例格式如下：
# 张三 教师 男 5010
# 李四 工人 女 4900
# 王五 商人 男 6700
# 计算并输出这组人员的平均工资（保留2位小数，宽度为20个字符，不足用=号补足)和最高工资， 格式如下：
# data = input()
# s = 0
# n = 0
# i = 0
# max_value = 0
# while data:
#     i = i + 1
#     ls = data.split(' ')[3]
#     print(ls)
#     if int(ls) > max_value:
#         max_value = int(ls)
#     s = s + int(ls)
#     data = input()
# s = s/i
# print("这组人员的平均工资:{:=^20.2f}\n最高工资:{:=^20.2f}".format(s, max_value))

# 三十六
# 附件是一个CSV格式文件，提取数据进行如下格式转换：
# (1)按行进行倒序排列；
# (2)每行数据倒序排列；
# (3)使用分号(：)代替逗号（，)无空格；
# 按照上述要求转换后将数据输出。
# f = open("data-list-reverse.csv")
# ls = f.readlines()   #本身就返回了一个字符串的数组给ls
# ls = ls[::-1]
# lt = []
# for item in ls:
#     item = item.strip('\n')
#     item = item.replace(' ', '')
#     lt = item.split(",")
#     lt = ';'.join(lt)
#     print(lt)
# f.close()

# 三十七
# 接收用户输入任何字符串或数字，显示在屏幕上，如果用户直接回车则显示'game over.'
# count = input()
# print(count if count else "game over")

# 三十八
# 使用turtle)库的fd)、seth()、pencolor(0函数绘制嵌套五角形，五角形边 长从1像素开始，
# 第一条边从0度方向开始，边长按照2个像素递增，每 条边使用一种颜色

#在_____处填写一行代码
#不允许修改其他代码
#
# import turtle as t
# colors = ["purple","red","blue","green","black"]
# d = 0
# k = 1
# edge = 5
# for j in range(10):
#     for i in range(5):
#         t.pencolor(colors[i])
#         t.fd(edge*k)
#         d = d + 360 / edge
#         t.seth(d)
#         k += 1
# t.done()

# 三十九
# 输入一个包含字母和数字的字符串，剔除其中的字母，只保留数字，输出显示在屏幕上。
#请在________处填写一行代码
#不可修改其他代码

# w = input()
# for x in w:
#     if ord('0') <= ord(x) <= ord('9'):
#         continue
#     else:
#         w = w.replace(x, '')
# print(w)

# 四十
# 字符串变量sr保存了气体浓度传感器的4条数据，每条数据的第一字段是传感器编号，第二字段是气体名 称，第三字段是浓度值。示例如下：
# TGS2402:甲醛：1.36
# 在屏幕上按照浓度值递减的顺序，显示输出每种气体名称，浓度，及其浓度在四种气体浓度中所占的百分 比；示例如下：
#氮气的浓度是：5.20，占比：49号
#请在………处填写多行代码
#不可修改其他代码
str = 'TGS2402:甲醛:1.36\nTGS2500:氮气:5.20\nTGS2310:甲烷:1.70\nTGS2820:乙烯:2.43'
ls = str.split('\n')
sum = 0
fieds = []
print(ls)
for gas in ls:
    fi = gas.split(':')[1]
    sum += float(gas.split(':')[2])
    fieds.append((fi, gas.split(':')[2]))
    fieds.sort(key=lambda x: x[-1], reverse=True)
print(fieds)
for gas in fieds:
    print('{}的浓度是:{},占比：{:.0f}%'.format(gas[0], gas[1], (float(gas[1])/sum) * 100))