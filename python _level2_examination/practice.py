# -*- coding: utf-8 -*-
# 在...上补充一行或者多行代码
# 在——————上补充一行代码
# 在横线处填写代码，完成如下功能。
# 接收用户输入的一个大于10小于10的8次方十进 制正整数，输出这个正整数各字符的和，以25为 宽度，居中显示，采用等号=填充。
# 第一题
# s = input("请输入一个正整数: ")
# cs = 0
# for c in s:
#     cs += int(c)
# print('{:=^25}'.format(cs))

# 第二题
# 在横线处填写代码，完成如下功能。
# 接收用户输入的数据，该数据仅由字母和中文混 合构成，无其他类型字符，统计并输出中文字符 出现的个数，

# 在...上补充一行或者多行代码
# 在——————上补充一行代码

# s = input("请输入中文和字母的组合: ")
# count = 0
# for c in s:
#     # print(c)
#     if not (65 <= ord(c) <= 90 or 97 <= ord(c) <= 122):
#         count += 1
# print(count)
#

# 第三题
# 在横线处填写代码，完成如下功能。
# 接收用户输入的以英文逗号分隔的一组数据，其中，每个数据都是整数或浮点数，打印输出这组 数据中的最大值。
# 在...上补充一行或者多行代码
# 在——————上补充一行代码

# s = input("请输入一组数据：")
# ls = s.split(',')
# # print(ls)
# lt = []
# for i in ls:
#     # 加上eval函数，将字符串转换成对应格式，整形或者浮点型
#     lt.append(eval(i))
# # max求数组里的最大值 min求数组里的最小值
# print(max(lt))


# 第四题
# 描述
# 请写代码替换横线，不修改其他代码，实现以下功能：
# a和b是两个列表变量，列表a为[3,6,9]已给定，键盘输入列表b,计算a中元素与b中 对应元素乘积的累加和。
# 例如：键盘输入列表b为[1,2,3]，累加和为13+26+3*9=42，因此，屏幕输出计算结果 为42

# a = [3, 6, 9]
# b = eval(input()) #例如：[1,2,3]
# s = 0
# for i in range(3):
#     s += a[i]*b[i]
# print(s)

# 第五题
# 请编写代码替换横线，可修改其他代码，实现下面功能：
# 获得用户输入的一个整数n,输出一个n-1行的数字三角形阵列。
# 该阵列每行包含的 整数序列为从该行序号开始到n-1,例如第1行包含1到n-1的整数，第i行包含从到n- 1的整数；数字之间用英文空格分隔。
# 示例如下（其中数据仅用于示意）：

# 在...上补充一行或者多行代码
# 在——————上补充一行代码

# n = eval(input("请输入一个整数："))
# for i in range(1, n):
#     for j in range(1, n):
#         if j <= n-i:
#             # 先打印出j来看，end去掉空格，就比较好看了
#             print(j, end=' ')
#     print()
#
#
# 第六题
# 请编写代码替换横线，可修改其他代码，实现下面功能：
# 获得用户输入的5个小写英文字母，将小写字母变成大写字母， 并逆序输出，字母之间用逗号分隔。
# 示例如下（其中数据仅用于示意）：
# 输入：
# gbcde
# 输出：
# E,D,C,B,G

# 在...上补充一行或者多行代码
# 在——————上补充一行代码

# s = input("请输入5个小写字母：")
# s = s.upper()
# print(','.join(s[::-1]))


# 第七题
# 请写代码替换横线，可修改其他代码，实现如下功能：
# 获得用户输入的一个整数，记为n,以100为随机数种子，随机生成10个1到之间的 随机数，输出生成的随机数，数字之间以逗号分隔。
# 示例如下（其中数据仅用于示意）：

# 在...上补充一行或者多行代码
# 在——————上补充一行代码

# import random
# n = input("请输入一个整数：")
# random.seed(100)
# for i in range(1,11):
#     if i < 10:
#         #  注意n是字符串
#         print(random.randint(1, int(n)), end=',')
#     else:
#         # 最后一位不打印逗号，所以单独处理
#         print(random.randint(1, int(n)))
#
# 第八题
# 请写代码替换横线，不修改其他代码，实现以下功能：
# a和b是两个长度相同的列表变量，列表a为[3,6,9]已经给定，键盘输入列表b,计算a 中元素与b中元素的和形成新的列表c,在屏幕上输出。

# 在...上补充一行或者多行代码
# 在——————上补充一行代码
# a = [3, 6, 9]
# b = eval(input())  # 例如：[1,2,3]
# c = []
# for i in range(3):
#     c.append(a[i]+b[i])
# print(c)
#
# 第九题
# 请写代码替换横线，不修改其他代码，实现以下功能：
# 键盘输入一段中文文本，不含标点符号和空格，命名为变量s,采用jieba库对其进行 分词，输出该文本中词语的平均长度，保留1位小数。
# 在...上补充一行或者多行代码
# 在——————上补充一行代码

# import jieba
# txt = input("请输入一段中文文本:")
# # jieba精确模式
# ls = jieba.lcut(txt)
# # :.1f是保留一位小数   :.nf是保留n位小数
# print("{:.1f}".format(len(txt)/len(ls)))

# 保留两位小数的方法
# format保留小数位方法
# print('{:.3f} {:.2f}'.format(0.12345, 1))
# # round函数
# print(round(1.234, 2))
# # %.xf
# print('%.2f' % 1.236)
#
# 第十题
# 请写代码替换模板中的横线，键盘输入一段文本，保存在一个字符串变量$中，
# 分别用Python内置函数以及jieba库中的已有函数计算字符串s的中文字符个数以及中 文词语个数。注意：中文字符包括中文标点符号。

# import jieba
# s = input("请输入一个字符串:")
# n = len(s)
# print(jieba.lcut(s, cut_all=True))
# m = len(jieba.lcut(s))
# print("中文字符数为{}，中文词语数为{}。".format(n, m))

#第十一题
# 从键盘输入两个浮点数，计算以这两个浮点数为边长的长方形的面积，显示在屏幕 上，数据长度为10，右对齐，不足部分用-补齐，保留2位小数。"23.34,45.12"

# l, w = eval(input())
# {:->10.2f}表示保留两位小数右对齐，长度为10不足用-补齐
# print("长方形的面积是:{:->10.2f}".format(l*w))
# 这是分开使用":2.f".format(l*w)先算面积并保留两位小数，再右对齐长度为10补齐-
# print("长方形的面积是:{:->10}".format(":2.f".format(l*w)))

#
# 第十一题
# 利用random随机库里的函数，生成一个由四个大小写字母组成的验证码，显示在屏 幕上。
# # 在...上补充一行或者多行代码
# # 在——————上补充一行代码
# import random as r
# zmb = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
# r.seed(1)
# 方法一
# code = ''.join(r.sample(zmb, 4))
# 方法二
# tmp = r.sample(zmb, 4)
# code = tmp[0] + tmp[1] + tmp[2] + tmp[3]
# 方法三
# tmp = r.sample(zmb, 4)
# code = ''
# for x in tmp:
#     code = code + x
# # 方法四
# code = ''
# for i in range(4):
#     code += r.choice(zmb)
# print(code)


# 第十二题
# 示例代码里定义的列表变量score! 里面是5组同学在一次比赛中的成绩，每组成 绩包括三项，分别记为a1,a2,a3,三个字段以逗号分隔，示例如下：
# 计算每组同学比赛成绩的总成绩，计算公式为：total=a1*0.6+a2*0.3+a3*0.1。
# 在...上补充一行或者多行代码
# 在——————上补充一行代码


score = [[87, 79, 90], [99, 83, 93], [90, 75, 89], [89, 87, 94], [95, 85, 84]]
i = 0
for j in score:
    # print(i)
    final = j[0]*0.6 + j[1]*0.3 + j[2]*0.1
    print(final)
    print('the {} final score is {}'.format(i + 1, int(final)))
    i= i+ 1