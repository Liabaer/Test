# -*- coding: utf-8 -*-
#第一题
# 模板中给出的代码是本题目的提示框架，其中代码可以任意修改。请在该文件中删 除横线，编写代码，以实现一下功能：
# 键盘输入小明学习的课程名称及考分等信息，信息间采用空格分隔，每个课程一 行，空行回车结束录入，示例格式如下：
# 数学90
# 语文95
# 英语86
# 物理84
# 生物87
# 屏幕输出得分最高的课程以及成绩，得分最低的课程及成绩，以及平均分（保留2位 小数)
# 注意，其中逗号为英文逗号，格式如下；
# 最高分课程是语文95，最低分课程是物理84，平均分是88.40

# data = input()  # 课程名 考分
# score = 0
# count = 0
# max_score = 0
# max_name = ''
# min_score = 0
# min_name = ''
# dict_score = {}
# while data:
#     if data[0:2] not in dict_score:
#         dict_score[data[0:2]] = data[2:4]
#     data = input()
# print(dict_score)
# for k, v in dict_score.items():
#     count += 1
#     score += int(v)
#
#     if int(v) > max_score:
#         max_score = int(v)
#         max_name = k
#     if min_score == 0:
#         min_score = int(v)
#     if int(v) < min_score:
#         min_score = int(v)
#         min_name = k
# avg = score/count
# # print(min_name,min_score, max_name, max_score, avg)
# print("最高分课程是{}{}, 最低分课程是{}{}, 平均分是{:.2f}".format(min_name, max_score, min_score, min_score, avg))

#第二题
# 补全编程模板中的代码，删除横线，补全代码，可以修改其他代码。实现以下功能
#
# 键盘输入某个班级各个同学就业的行业名称，行业名称之间用空格间隔(回车结束输入)。完善python代码，统计各行各业就业的学生数量，按数量从高到低方式输出。例如输入:
# 交通 金融 计算机 交通 计算机 计算机
# 输出参考格式如下，其中冒号为英文冒号:
# 计算机:3
# 交通:2
# 金融:1

# names = input("请输入各个同学行业名称，行业名称之间用空格间隔（回车结束输入）：")
# sub = names.split(' ')
# print(sub)
# d = {}
# for i in sub:
#     d[i] = d.get(i, 0) + 1
# print(d)
# ls = list(d.items())
# ls.sort(key=lambda x: x[1], reverse=True)
# print(ls)
# for k in ls:
#     print("{}:{}".format(k[0], k[1]))

# 第三题
# 本题的提示已经在编程模板中给出，其中的代码可以修改，请删除横线，补全代码。实现以下功能:
# 键盘输入一组人员姓名、年龄、性别等信息，信息间采用空格分隔，每人一行，空行回车结束录入，示例格式如下:
#
# 张三 23 男
# 李四 21 女
# 王五 18 男
#
# 计算并输出这组人员的平均年龄(保留2位小数)和其中男性人数，格式如下:
#
# 平均年龄是2067男性人数是2

# data = input()  # 姓名 年龄 性别
# avg = 0
# count = 0
# num_man = 0
# age = 0
# data_new = []
# while data:
#     data_new.append(data.split(' ')[1:3])
#     data = input()
# print(data_new)
# for i in data_new:
#     count += 1
#     for j in i:
#         if j == '男':
#             num_man += 1
#         elif j != '女':
#             age += int(j)
# print(age, num_man, count)
# avg = age/count
# print("平均年龄是{:.2f} 男性人数是{}".format(avg, num_man))

# 第四题问题：请编写程序，从data.txt中提取大学或者机构名称列表，将结果写入文件 univ.txt,每行一个大学或者机构名称，
# 按照大学或机构在data.txt出现的先后顺序 输出，样例如下：
# 北京理工大学
# 北京师范大学
# 。。。
# 提示：所有大学名称在data.txt文件中以alt="北京理工大学"形式存在。

# f = open('school.txt', 'r')  # 此处可多行
# f = f.readlines()
# school = []
# for i in f:
#     for j in i.split(' '):
#         if j[0:3] == 'alt' and ('大学' in j or '学院' in j):
#             school.append(j.split('"')[1])
# print(school)
# f = open("univ.txt", "w")
# for i in school:
#     f.write('{}\n'.format(i))
# f.close()

# 问题2:请编写程序，从univtxt文件中提取大学名称，大学名称以出现“大学"或“学院"字样为参考，
# 但不包括“大学生"等字样，将所有大学名称在屏幕上输出，大学各行之间没有空行，最后给出名称中包含"
# 大学"和“学院”的名称数量，同时有大学和学院做大学处理。样例如下(样例中数量不是真实结果):
#
# 北京理工大学
#
# 长沙师范学院
#
# 包含大学的名称数量是10
# 包含学院的名称数量是10
# 在右侧的编码框中给出了程序框架文件，请补充修改代码完成程序(10分)
n = 0
m = 0
f = open("univ.txt", "r")
f_new = f.readlines()
dict = {}
for i in f_new:
    print("{}".format(i))
    if '大学' in i:
        dict['大学'] = dict.get('大学', 0) + 1
    if '学院' in i:
        dict['学院'] = dict.get('学院', 0) + 1
    if '大学' in i and '学院' in i:
        dict['大学'] = dict.get('大学', 0) + 1
f.close()
# print(dict)
for k, v in dict.items():
    if k == '大学':
        n = v
    if k == '学院':
        m = v
print("包含大学的名称数量是{}".format(n))
print("包含学院的名称数量是{}".format(m))


