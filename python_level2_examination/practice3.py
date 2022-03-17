# -*- coding: utf-8 -*-
# 第一题
# 获得用户输入的一个数字，对该数字以30字符宽度，十六进制，居中输出，字母小 写，多余字符采用双引号(")填充，请完善模板中代码。注（英文引号）
# s = input()
# # 由于外面已经是"号，所以内部使用要转以\"
# print("{:\"^30}".format(hex(int(s))))
# print("{:\"^30b}".format(int(s)))

# 第二题
# 从键盘输入4个数字，各数字采用空格分隔，对应变量x0,y0,x1,y1.计算两点(x0,y0) 和(x1y1)之间的距离，屏幕输出这个距离，保留2位小数。根号( (x1-x0)^2 + (y1- y0)^2)  x^n表示x的n次方
# 例如：
# 键盘输入：0 1 3 5
# 屏幕输出：5.00

# ntxt = input("请输入4个数字(空格分隔):")
# nls = ntxt.split(' ')
# x0 = eval(nls[0])
# y0 = eval(nls[1])
# x1 = eval(nls[2])
# y1 = eval(nls[3])
# # pow(x, y) 表示x的y次方 y=1/2就是根号
# x = pow(x1-x0, 2)
# y = pow(y1 - y0, 2)
# res = pow(x+y, 1/2)
# print("{:.2f}".format(res))
#
# 第三题
# 在右侧答题模板中修改代码，删除代码中的横线，填写代码，完成如下功能。
# 程序接收用户输入的五个数，以逗号分隔。将这些数按照输入顺序输出，每个数占 10个字符宽度，右对齐，所有数字显示在同一行。
# 输入：23,42,543,56,71

# num = input().split(',')
# for i in num:
#     print("{:<10}".format(i), end='')
#
# 第四题
# 在右侧答题模板中修改代码，删除代码中的横线，填写代码，完成如下功能。
# 社会平均工作时间是每天8小时。如果这位科学家的当下成就值是1，假设每工作1 小时成就值增加0.01%，计算并输出两个结果：
# 这位科学家5年后的成就值。以及 达到成就值100所需要的年数。其中，成就值和年数都以整数表示，每年以365天 计算。
# 输入输出示例
# 5年后的成就值是XXX
# XX年后成就值是100
# scale = 0.0001  # 成就值增量
#
#
# def calv(base, day):
#     val = base * pow(1+scale, 8*day)
#     return val
#
#
# print('5年后的成就值是{}'.format(int(calv(1, 5 * 365))))
#
# year = 1
# while calv(1, year*365) < 100:
#     year += 1
#
# print('{}年后成就值是100'.format(year))
#
#
# 第五题
# 接收 用户输入的一个小于20的正整数，在屏幕上逐行递增显示从01到该正整数，
# 数字 显示的宽度为2，不足位置补0，后面追加一个空格，然后显示>号，>号的个数 等于行首数字。
# 示例
# 输入：
# 3
# 输出：
# 01>
# 02>>
# 03>>
# n = input('请输入一个正整数:')                    #请输入一个正整数:
# for i in range(0, int(n)):
#     # {:>02}显示的宽度为2，不足位置补0
#     print('{:>02}{}'.format(i + 1, '>' * (i + 1)))
#


# 第六题
# 让用户输入一串数字和字母混合的数据，然后统计其中的数字和字母的个数，显示在 屏幕上。
# 示例
# 输入：
# Fda243fdw3
# 输出：
# 数字个数：4，字母个数：6
# ns = input("请输入一串数据：")
# dnum, dchr = 0, 0
# for i in ns:
#     if 47 <= ord(i) <= 58:
#         dnum += 1
#     if (ord('a') <= ord(i) <= ord('z')) or (ord('A')<= ord(i) <= ord('Z')):
#         dchr += 1
# print('数字个数：{}，字母个数：{}'.format(dnum, dchr))
#
#
# 第七题
# 从键盘输入一个字符串，检查并统计字符串中包含的英文单引号的对数。如果没有找 到单引号，就在屏幕上显示“没有单引号”；
# 每统计到2个单引号，就算一对，如果找 到2对单引号，就显示“有2对单引号”；如果找到3个单引号，就显示“有1对配对单引 号，存在没有配对的单引号”。
# 示例1：
# 输入："dfd'dfa'fd'"
# 输出："有1对配对单引号，存在没有配对的单引号”
# st = input()
# pair = 0
# for s in st:
#     if s == "'":
#         pair += 1
# if pair == 0:
#     pro = "没有单引号"
# elif pair % 2 == 0:
#     pro = "有{}对配对单引号，不存在没有配对的单引号".format(pair/2)
# else:
#    pro = "有{}对配对单引号，存在没有配对的单引号".format(int(pair/2))
# print(pro)
#
# 第八题
# 从键盘输入一个由1和0组成的二进制字符串s，转换为十进制数输出显示在屏幕 上。
# 示例1：
# 输入："1101"
# 输出："转换成十进制数是：13"

# s = input()
# d = 0

# 123 正常计算10进制  1 * 100 + 2 * 20 + 3 * 1 = 123
# 123 数学中定义（（1 * 10） + 2）* 10 + 3 = 123

# 从右到左边的计算
# 1101 正常计算二进制 1 * 2 ^ 0 + 0 * 2 ^ 1 + 1 * 2 ^ 2 + 1 * 2 ^ 3 = 13
#                   1           0           1           1
# 从左到右的计算
# 1101 数学中定义 （（1 * 2 + 1） * 2 + 0） * 2 + 1 = 13
#                  1       1         0         1
# while s:
#     d = d * 2 + int(s[0])
#     # 等价与s = s[1: len(s)] 每次删除首位
#     s = s[1:]
# print("转换成十进制数是：{}".format(d))
#
# 第九题
# 从键盘输入一个列表，将该列表中所有的单词首字母转换成大写，在屏幕上输出该列表。
# 示例1：
# 输入："["python","is","opening"]"
# 输出："['Python','Is','Opening'门"

# ls = eval(input())
# for i in range(len(ls)):
#     # s.capitalize() 将首字母转换成大写
#     ls[i] = ls[i].capitalize()
# print(ls)
#
# 第十题
# 苏格拉底是古希腊著名的思想家、哲学家、教育家、公民陪审员。苏格拉底的部分 名言被翻译为中文，其部分内容由sgd.txt给出。
# 读取文件，请过滤中文逗号、中文句号、中文冒号、中文引号，英文空格、换行符 n之后，
# 对其中的内容进行中文分词，在屏幕上显示输出词语出现次数前5的词，用一个中文 顿号、分割。
# 示例1：
# 输入：无
# 输出："你、我、他、我们、他们、" 注意：这里的输出只是示例
# import jieba
# temp = ['，', ' 。', '：', '"', '\n',  ' ', '；']
# f = open("sgld.txt", "r")
# f_new = f.readlines()
# newfile = ''
# d = {}
# for i in f_new:
#     for j in i:
#         if j not in temp:
#             newfile += j
# newfile = jieba.lcut(newfile)
# for i in newfile:
#     d[i] = d.get(i, 0)+1
# # print(d)
# ld = list(d.items())
# ld.sort(key=lambda x: x[-1], reverse=True)
# for i in ld[0:5]:
#     print('{}、'.format(i[0]), end='')
# f.close()
#
#
#
#
# 第十一题
# 设计打字测试功能代码。
# 默认原始字符串为“我爱你中国”，如果输入的字符串长度与原始字符串长度相同，
# 则调用编程模板中Percentage函数去计算这两个字符串对应位置相同的字符个数 占字符总长度的百分比，按照示例的格式输出；
# 请参考编程模板及输入输出示例，完善程序。
# def Percentage(str1, str2):
#     n = 0
#     # zip将字符串改成元祖 比如str1 = '1234'  str2 = '5679'  zip(str1, str2)之后就变成了（1，5）（2，6）（3，7）（4，9）
#     for s1, s2 in zip(str1, str2):
#         if s1 == s2:
#             n += 1
#     return n / len(str1)
#
#
# s1 = "我爱你中国"
# print(s1)
# s2 = input()
# print(s2)
# # 注意保留两位小数  .2f是不足2位不会补0，  0.2f保留2位小数，如果不足2位小数末尾补0
# print('{:0.2f}%'.format(Percentage(s1, s2)*100))
#
# 第十二题
# 从键盘输入一些字符，逐个把它们写到指定的文件out.txt中，直到输入一个@为 止。
# 示例1：
# 输入："
# Python
# is
# open.@
# 输出："Python is open."(执行代码后，out.txt文件中内容)

# n = input()
# temp = ''
# for i in n:
#     # print(j)
#     if i == '@':
#         break
#     else:
#         temp += i
# print(temp)


# 循环读入
# 如果读入的数据是
# pyton
# is
# open@
# temp = ''
# cnt = 0
# flag = True
# f = open("out3.txt", "w")
# while flag:
#     n = input()
#     # 直接按回车等于什么也没输入
#     if n == '':
#         cnt += 1
#     else:
#         # 没遇见回车
#         cnt = 0
#         n = n + '\n'
#         for i in n:
#             if i == '@':
#                 flag = False
#                 break
#             else:
#                 temp += i
#     # 连续遇见2次回车 就结束循环
#     if cnt == 1:
#         flag = False
#     # 继续输入
# f.write(temp)
# f.close()
# # print(temp)

# 第十三题
# 有一个列表studs如下：
# studs=[{'sid':'103','Chinese':90}, {'sid':'101','Chinese':80}, {'sid':'102','Chinese':70}]
# 将列表suds的数据内容提取出来，在屏幕上按学号从小到大的顺序显示输出每个 学号对应的课程的分数，格式见输出示例。

# studs=[{'sid':'103','Chinese':90}, {'sid':'101','Chinese':80}, {'sid':'102','Chinese':70}]
# temp = {}
# for i in studs:
#     # 由于studs数据结构复杂，所以要使用新的字典来存储学号和分数
#     sid = i['sid']
#     # 使用新的key存对应的valuse（valuse用循环内i的值来获取）
#     score = i['Chinese']
#     temp[sid] = score
# print(temp)
# temp = list(temp.items())
# temp.sort(key=lambda x: x[0], reverse=False)
# for i in temp:
#     print('{}:{}'.format(i[0], i[1]))



# 第十四题
# 编写函数reverse._dict(),功能是交换字典的key值和value值（不允许重复），并 按照key值降序输出新字典的内容，返回新的字典。
# 参照编程模板，完善程序。
# def reverse_dict(dic):
#     ls = list(dic.items())
#     ls.sort(key=lambda x: x[-1], reverse=True)
#     ls = dict(ls)
#     return ls
#
# #请输入一个字典
# dic = eval(input(""))  #{"alice":1001,"john":1003,"kate":1002}
# new_dic = reverse_dict(dic)
# for k,v in new_dic.items():
#     print('{} {}'.format(v, k))
#
#
# 第十五题
# 实现以下功能：以123为随机数种子，随机生成10个在1（含）到999（含）之间的随 机整数，每个随机数后跟随一个逗号进行分隔，屏幕输出这10个随机数。
# 示例1：
# 输入：无
# 输出："34,56，."

# import random
# random.seed(123)
# for i in range(10):
#     print(random.randint(1,999), end=",")


# 第十六题
# 从键盘输入一个整数，在屏幕上显示输出该整数的十六进制、八进制、二进制表示形 式。
# 示例1：
# 输入："100"
# 输出："0x64,0o144,0b1100100"
# tempStr = hex(100), oct(100), bin(100)
# print("{}".format(tempStr))
# tempStr = str(hex(100)), str(oct(100)), str(bin(100))
# print(tempStr)
# print("{}".format(",".join(list(tempStr))))
# #
# # temp_str = 100
# # print("{0:#x},{0:#o},{0:#b}".format(temp_str))
#
#
# 第十七题
# 在代码模板里定义了一个字典，key是员工的姓名，value是由部门和工资构成的列 表，用逗号隔开。示例如下：
# members={'张三'：['人力部'，5500]，
# 李四'：['后勤部'，4500]，
# # 。.(略)
# # 将姓名和工资显示在屏幕上，示例如下：
# # 张三的工资是：5500，部门是人力部 李四的工资是：4500，部门是后勤部 。略)
# # 工资最高的部门是：开发部，该部门工资是：8500
#
# members = {'张三': ['人力部', 5500],
#            '李四': ['后勤部', 4500],
#            '王三': ['市场部', 6500],
#            '赵六': ['开发部', 8500]
#            }
#
# lm = list(members.items())
# lm.sort(key=lambda x:x[1][1],reverse=True)
# print(lm)
# for key in members:
#     # print(key)
#     print('{}的工资是:{}, 部门是{}'.format(key, members[key][1], members[key][0]))
# res = lm[0]
# print('工资最高的部门是:{},该部门工资是:{}'.format(res[1][0], res[1][1]))
#
#
# 第十八题
# 本题目一共两个问题，分别拆解开成为两道题目。请根据问题修改代码，实现以下功能：
# 下面所示为一套由公司职员随身佩戴的位置传感器采集的数据，文件名称为"sensor.txt"，其内容示例如下：
# 2016/5/31 0:05,vawe1on1,1,1
# 2016/5/31 0:20,earpat001,1,1
# 2016/5/31 2:26,earpa001,1,6
# .(略)
# 第一列是传感器获取数据的时间，第二列是传感器的编号，第三列是传感器所在的楼层，第四列是传感器所在的位置 区域编号。
# 本题解答问题一
# 问题一(10分)：在右侧模板中修改代码，读入sensor..txt文件中的数据，提取出传感器编号为earpa001的所有数 据，
# 将结果输出保存到"earpa001.txt"文件。输出文件格式要求：原数据文件中的每行纪录写入新文件中，行尾无空 格，无空行。参考格式如下：
# 2016/5/317:11,earpa001,2,4
# 2016/5/318:02,earpa001,3,4
# 2016/5/319:22,earpa001,3,4
#
# f = open("sensor.txt",'r')
# f_new= f.readlines()
# fo = open("earpa001.txt", 'w')
# for line in f_new:
#     l = line.split(',')
#     print(l)
#     if l[1] == ' earpa001':
#         fo.write('{},{},{},{}\n'.format(l[0], l[1], l[2], l[3].strip()))
# fo.close()
# f.close()
#
# 问题二（10分)：在右侧模板中修改代码，读入"earpa001.txt" 文件中的数据，统计earpa00对应的职员在各楼层和区域出现的 次数，
# 保存到"earpa001_count.txt"文件，每一条纪录一行，位置信息和出现的次数之间用英文半角逗号隔开，行尾无空格，无 空行。参考格式如下。
# 1-1,5
# 1-4,3
# (略)
# 含义如下：
# 第1行"1-1,5"中1-1表示1楼1号区域，5表示出现5次；
# 第2行"1-4,3"中1-4表示1楼4号区域，3表示出现3次；

# f = open("earpa001.txt", 'r')
# f_new = f.readlines()
# d = {}
# fc = open("earpa001_count.txt", 'w')
# for i in f_new:
#     i = i.strip().split(',')
#     k = i[2]+'-'+i[3]
#     # print(k)
#     if k not in d:
#         d[k] = 1
#     else:
#         d[k] = d[k] + 1
# print(d)
# for k, v in d.items():
#     fc.write('{},{}\n'.format(k, v))
# fc.close()
# f.close()

# 第十九题
# 从键盘输入一个人的身高和体重的数字，以英文逗号隔开，在屏幕上显示输出这个人 的身体质量指数(BMI),BMI的计算公式是：BMI=体重(kg)/身高^2(m^2)
# 示例1：
# 输入："1.6,50"
# 输出："BMI是19.5"
h, w = eval(input()) # 请输入身高(m)和体重(kg)，逗号隔开:
# :.1f保留一位小数
print("BMI是{:.1f}".format(w/pow(h, 2)))