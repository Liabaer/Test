# -*- coding: utf-8 -*-
# 第一题
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

# 第二题
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
# n = 0
# m = 0
# f = open("univ.txt", "r")
# f_new = f.readlines()
# dict = {}
# for i in f_new:
#     print("{}".format(i))
#     if '大学' in i:
#         dict['大学'] = dict.get('大学', 0) + 1
#     if '学院' in i:
#         dict['学院'] = dict.get('学院', 0) + 1
#     elif '大学' in i and '学院' in i:
#         dict['大学'] = dict.get('大学', 0) + 1
# f.close()
# # print(dict)
# for k, v in dict.items():
#     if k == '大学':
#         n = v
#     if k == '学院':
#         m = v
# print("包含大学的名称数量是{}".format(n))
# print("包含学院的名称数量是{}".format(m))

# 第五题
# 问题1：数据统计。要求：统计出两个文件中出现次数最多的10个词 语，作为主题词，要求词语不少于2个字符，
# 打印输出在屏幕上，输出 示例如下：（示例仅作为示意）
# 2019:改革：10，企业：9，..（略），深化2
# 2018:改革：11，效益，7.…（略)，深化：1
# 注意：输出格式采用英文冒号和英文逗号，标点符号前后无空格，各词 语间用逗号分隔，最后一个词语后无逗号。
# import jieba
#
# temp = [':', ' ', '（', '）', '.', '/', '\n', '-', '，', '「', '」', '—', '：', '；', '。', '、']
# def find_most(f):
#     f = f.readlines()
#     d = {}
#     for i in f:
#         i.strip()
#         # print(jieba.lcut(i))
#         for j in jieba.lcut(i):
#             if j not in temp:
#                 d[j] = d.get(j, 0) + 1
#     # print(d)
#     ls = list(d.items())
#     ls.sort(key=lambda x: x[-1], reverse=True)
#     # print(len(ls))
#     num = 0
#     for i in ls[0:10]:
#         if num < 9:
#             print("{}:{},".format(i[0], i[1]), end='')
#         if num == 9:
#             print("{}:{}".format(i[0], i[1]))
#         num += 1
#     return
#
# f1 = open("text.txt", 'r')
# find_most(f1)
# f2 = open("text1.txt", 'r')
# find_most(f2)

# 第六题
# 其中，文本文件“八十天环游地球.xt"是法国作家儒勒.凡尔纳《八十天环游地球》 长篇小说的网络版本，请修改源文件实现以下功能。
# 问题1：提取章节题目并输出到文件。
# 要求：在模板中补充代码，提取“八十天环游地球.xt”中所有章节的题目，并且将提 取后的题目输出到“八十天环游地球-章节.txt"文件中，每行一一个标题
# f = open("八十天环游地球.txt", encoding="utf-8")
# f_new = f.readlines()
# f = open('八十天环游地球-章节.txt', 'w')
# for i in f_new:
#     if i[0] == '第' and i[2] == '章':
#         # print(i)
#         f.write('{}'.format(i))
# f.close()

# 问题2：统计每章节的高频词并打印输出。
# 要求：在模板补充代码，统计"八十天环游地球.xt”中每一章的标题和内容中出现
# 次数最多的词语（词语长度不少于2个字符）及其次数，输出格式为章节名、词语及其 出现的次数，以空格分隔
# import jieba
#
# jieba.setLogLevel(20)
# temp = [':', ' ', '（', '）', '.', '/', '\n', '-', '，', '「', '」', '—', '：', '；', '。', '、']
# f = open("八十天环游地球.txt", encoding="utf-8")
# f_new = f.readlines()
#
# new_str = ''
# for i in f_new:
#     i.strip()
#     d = {}
#     if i[0] == '第' and i[2] == '章':
#         # print(new_str)
#         if new_str != '':
#             for j in jieba.lcut(new_str):
#                 if j not in temp and len(j) >1:
#                     d[j] = d.get(j, 0) + 1
#             ls = list(d.items())
#             ls.sort(key=lambda x: x[-1], reverse=True)
#             print("{} {} {}".format(t[0:3], ls[0][0], ls[0][1]))
#         # print(d)
#         # 初始化
#         new_str = ''
#         # 再将标题加进去
#         t = i
#         new_str = new_str +(i)
#     else:
#         new_str = new_str +(i)
# d = {}
# if new_str != []:
#     for j in jieba.lcut(new_str):
#         if j not in temp and len(j) > 1:
#             d[j] = d.get(j, 0) + 1
# # print(d)
# ls = list(d.items())
# ls.sort(key=lambda x:x[-1],reverse=True)
# print("{} {} {}".format(t[0:3], ls[0][0], ls[0][1]))
# f.close()
#
#
# 第七题
# webpage.txt保存了某网站一个网页的HTML格式源代码。在该文件中，JPG图片以
# 一个完整的URL表示，示例如下：# 其中，<a>与<a>是一对组合，表示包含一个URL链接；<img..(略)…/>表示包含
# 一个JPG图像文件的URL,每个URL用src=开头，以JPG图像文件名结束，如
# 538.JPG表示JPG图像文件。
# 在右侧编程框编程实现如下功能：
# 本题作答第一问
# (1)统计并打印输出该页面中JPG图像文件的URL数量。注意，JPG扩展名都是大写
# 字母，输出示例如下（其中数据仅用于示意）：
# 输出：
# 15
#
# f = open("webpage.txt", "r")
# f = f.readlines()
# #统计url个数
# num= 0  #统计个数的初始值为0
# for i in f:
#     if 'src=' in i and 'JPG' in i:
#         num += 1
#         print(i)
# print(num)  #输出个数

# (2)将webpage.txt页面中的JPG图像文件的URL提取出来，保存在文件images.txt
# 中，每个URL-行。
# 输出格式示例如下：( 其中数据仅用于示意)
# http://image.ngchina.com.cn/2018/0829/20180829012548753.JPG
# http:/image.ngchina.com.cn/2018/0823/thumb._469_352_20180823121155508.
# (略)
#
# f = open("webpage.txt", "r")
# a = f.readlines()
# #统计url个数
# f_new = open("images.txt", 'w')
# for i in a:
#     if 'src=' in i and 'JPG' in i:
#         i = i.split(' ')
#         for j in i:
#             if 'src=' in j and 'JPG' in j:
#                 print(j.split('"')[1])
#                 n = j.split('"')[1]
#                 f_new.write("{}\n".format(n))
# f_new.close()
# f.close()

# 第八题
# 要求：在右侧答题模板中修改代码，删除代码中的横线，填写代码，对 文件data.txt的内容进行清洗，
# 去掉中文标点符号、中英文空格、回车 等符号，只保留中文、英文、数字、英文标点符号，将结果输出到文件 clean.txt中。

# t = ["，", "。", "？", "；", " ", " "]
#
# f = open("data(5).txt", 'r')
# a = f.readlines()
# f_new = open("clean.txt", 'w')
# for i in a:
#     for j in i:
#         if j not in t:
#             f_new.write("{}".format(j))
#             # if j != '\n':
#             #     f_new.write("{}".format(j))
#             # else:
#             #     f_new.write('\n')
# f_new.close()
# f.close()
# 问题2：提取主题词及其出现频次。
# 要求：在右侧答题模板中修改代码，删除代码中的横线，填写代码，提 取clean.txt文件中长度不少于3个字符的词语并统计词频，将词频最高 的10个词语作为主题词，并将主题词及其频次输出到屏幕。
# 示例如下：
# 4.0:10,制造业：9.…（略）
# 注意：输出格式采用英文冒号和英文逗号，标点符号前后无空格，各词 语中间用逗号分隔，最后一个词语无逗号。
# import jieba
# f = open("clean.txt", "r")
# a = f.readlines()
# d = {}
# for i in a:
#     i = jieba.lcut(i)
#     for j in i:
#         if len(j) > 2:
#             d[j] = d.get(j, 0) + 1
# # print(d)
# ld = list(d.items())
# # print(ld)
# ld.sort(key=lambda x:x[-1], reverse=True)
# ld = ld[0:10]
# # print(ld)
# num = 0
# for i in ld:
#     if num < 9:
#         print("{}:{},".format(i[0], i[1]), end='')
#     else:
#         print("{}:{}".format(i[0], i[1]))
#     num += 1
# f.close()
#
#
# 第九题
# 二千多年前希腊的天文学家希巴克斯命名十二星座，
# 它们是水瓶座、双鱼座、白羊 座、金牛座、双子座、巨蟹座、狮子座、处女座、天秤座、天蝎座、射手座、魔蝎 座。
# 给出一个CSV文件(PY301-SunSign.csv),内容示例如下：
# 问题1(5分)：在代码框中修改代码，读入CSV文件中的数据，获得用户输入。根
# 据用户输入的星座名称，输出此星座的出生日期范围。
# 参考输入和输出示例格式如下：
# 请输入星座中文名称（例如，双子座）：双子座
# 双子座的生日位于521-621之间

# xz = input("请输入星座中文名称:")
# f = open("data-xz.csv", "r")
# new = f.readlines()
# ls = []
# for i in new:
#     i = i.split(",")
#     if i[1] == xz:
#         print("{}的生日位于{}-{}之间".format(i[1], i[2], i[3]))
# f.close()
#
# 问题2（10分)：在代码框中修改代码，读入CSV文件中数据，获得用户输入。用户
# 键盘输入一组范围是1-12的证书作为序号，序号间采用空格分隔，以回车结束。
# 屏 幕输出这些序号对应的星座的名称、支付编码以及出生日期范围，每个星座的信息
# 一行。本次屏幕显示完成后，重新回到输入序号的状态。
# 双子座(9802)的生日是5月21日至6月21日之间
# import csv
# f = open("data-xz.csv", "r")
# new = csv.reader(f)
# y_s = ''
# d_s = ''
# y_e = ''
# d_e = ''
# while True:
#     xh = input("请输入序号：")
#     if 1 <= int(xh) <= 12:
#         print("输入正确，开始执行计算逻辑")
#         for i in new:
#             if xh == i[0]:
#                 print(i)
#                 if len(i[2]) == 3:
#                     d_s = i[2][1:3]
#                     y_s = i[2][0]
#                 if len(i[3]) == 3:
#                     d_e = i[3][1:3]
#                     y_e = i[3][0]
#                 if len(i[2]) == 4:
#                     d_s = i[2][2:4]
#                     y_s = i[2][1:2]
#                 if len(i[3]) == 4:
#                     d_e = i[3][2:4]
#                     y_e = i[3][1:2]
#                 print("{}({})的生日是{}月{}日至{}月{}日之间".format(i[1], i[4], y_s, d_s, y_e, d_e))
#         break
#     else:
#         print("输入有误继续输入")
#         continue
# f.close()
#
#
# 第十题
# 描述
# 获得用户的非数字输入，如果输入中存在数字，则要求用户重新输入，直至满足条件 为止，
# 并输出用户输入字符的个数，完善模板中的代码，可以删除全部提示代码，删 除横线完成编程。
# count = 0
# flag = True
# while True:
#     num = input("请输入内容：")
#     for i in num:
#         # if ord('0') >= ord(i) or ord(i) >= ord('9')
#         if 48 >= ord(i) or ord(i) >= 57:
#             flag = True
#             count += 1
#         else:
#             flag = False
#             continue
#     if flag:
#         print(count)
#         break
#
# 第十一题
# 键盘输入一组我国高校所对应的学校类型，以空格为分隔，共一行，示例格式如下：
# 综合 理工 综合 综合 综合 师范 理工
# 统计各类型的数量，从数量多道少的顺序屏幕输出类型及对应数量，以英文冒号分 隔，以英文冒号分隔，每个类型一行，输出参考格式如下：
# 综合：4
# 理工：2
# 师范：1

# txt = input("请输入类型序列：")
# txt = txt.split(" ")
# d = {}
# for i in txt:
#     d[i] = d.get(i, 0)+1
# ls = list(d.items())
# ls.sort(key=lambda x: x[-1], reverse=True)
# for i in ls:
#     print("{}:{}".format(i[0], i[1]))
#
#
# 第十一题
# 计算两个列表1s和1t对应元素乘积的和（即向量和），补充模板中的代码，删除下 划线，可以任意修改代码。完成程序。
# 1s=[111,222,333,444,555,666,777,888,999]
# 1t=[999,777,555,333,111,888,666,444,222]

# ls = [111, 222, 333, 444, 555, 666, 777, 888, 999]
# lt = [999, 777, 555, 333, 111, 888, 666, 444, 222]
#
# i=0
# new=0
# while i < len(ls):
#     new += (ls[i] * lt[i])
#     i += 1
# print(new)
#
#
# 第十二题
# 在右侧答题模板中修改代码，删除代码中的横线，填写代码，完成如下功能。
# 将程序里定义好的sd列表里的姓名和成绩与已经定义好的模板拼成一段话，显示在 屏幕上。
# 示例
# 输出
# 亲爱的张三，你的考试成绩是：英语90，数学87，python语言95，总成绩272.特此通知

# std = [['张三', 90, 87, 95], ['李四', 83, 80, 87], ['王五', 73, 57, 55]]
# modl = "亲爱的{}, 你的考试成绩是: 英语{}, 数学{}, Python语言{}, 总成绩{}.特此通知."
#
# for st in std:
#     cnt = 0
#     for i in range(1, 4):
#         cnt += int(st[i])
#         # print(cnt)
#     print(modl.format(st[0], st[1], st[2], st[3], cnt))
#
#
#
# 第十三题
# 《论语》是儒家学派的经典著作之一，主要记录里孔子及其弟子言行。这里给出了
# 一个网络版的《论语》，文件名为“论语.xt”，其内容采用逐句"原文"与逐句“注释” 相结合的形式组织，
# 通过【原文】标记《论语》原文内容，通过【注释】标记《论 语》注释内容，具体文件格式框架请参考“论语txt"文件。
# 问题一（10分)：在模板中修改代码，提取"论语.txt"文件中的原文内容，输出保 存到考生文件夹下，文件名为“论语-原文.tx"
# 具体要求：仅保留"论语.txt"文件中 所有【原文】标签下面的内容，不保留标签，并去掉每行行首空格及行尾空格，无 空行。
# 原文小括号及内部数字是源文件中注释项的标记，请保留。示例输出文件格 式请参考“论语-原文-输出示例.txt”文件。注意：示例输出文件仅帮助考生了解输出 格式，不作它用。
#
# fi = open("论语.txt", "r")
# fo = open("论语-原文.txt", "w")
# fi_r = fi.readlines()
# flag = True
# for i in fi_r:
#     i = i.strip()
#     temp = ''
#     # print(i)
#     if "【原文】" in i:
#         flag = True
#         # print(temp)
#     elif "【注释】" in i:
#         flag = False
#         continue
#     # print(flag)
#     if flag and i != '【原文】' and i != '':
#         temp = i
#         fo.write("{}\n".format(temp))
# fo.close()
# fi.close()
#
# 问题二（10分)：在模板中修改代码，对“论语-原文.txt"(这是你回答问题一生成的 答案文件)或“论语.txt"文件进一步提纯，
# 去掉每行文字中所有的小括号及内部数 字，保存为“论语-提纯原文"文件。示例输出文件格式请参考“论语-提纯原文-输出 示例txt"文件。
# 注意：示例输出文件仅帮助考试了解输出格式。不做它用。

fi = open("../data/论语-原文.txt", "r")
fo = open("../data/论语-提纯原文.txt", 'w')
f_new = fi.readlines()
for i in f_new:
    flag = True
    temp = ''
    for j in i:
        if (ord('1') > ord(j) or ord(j) > ord('9')) and j != '(' and j != ')':
            temp += j
            # flag = True
        else:
            flag = False
            continue
        # if flag:
        #     temp += j
    if temp != '':
        # print("{}".format(temp))
        fo.write("{}".format(temp))
fo.close()
fi.close()
