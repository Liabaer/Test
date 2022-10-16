# -*- coding: utf-8 -*-
# 001- 1
# 给定一个数字123456，请采用宽度为25、右对齐方式打印输出，使用加号”+"填 充。
# n = 123456
# print('{:+>25}'.format(n))

# 2
# 从键盘输入一个0到1之间的小数，使用计算公式x=3.9*x*(1-)来产生随机数，在屏幕上输出产生的前10个数据。
# x = eval(input())
# for i in range(10) :
#     x = 3.9 * x * (1 - x)
#     print(x)

# 3
# # 请补充如下代码，求其各整数元素的和：
# ls = [123, "456", 789, "123", 456, "789"]
# s = 0
# for item in ls:
#     if type(item) == int:
#         s += item
# print(s)

# 4
# # 使用turtle库绘制红色五角星图形
# from turtle import *
# setup(400,400)
# penup()
# goto(-100,50)
# pendown()
# color('red')
# begin_fill()
# for i in range(5):
#     forward(200)
#     right(144)
# end_fill()
# hideturtle()
# done()

# 5
# 恺撒密码是古罗马恺撒大帝用来对军事情报进行加密的算法，它采用了替换方法对
# 信息中的每一个英文字符循环替换为字母表序列该字符后面第三个字符，即循环左 移3位，对应关系如下：
# 原文：ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 密文：DEFGHIJKLMNOPQRSTUVWXYZABC
# 基础中文字符的Unicode编码范围是[0x4e00,0x9fa5],共20902个字符。请以 10451位循环移位数量，编写中文文本的类恺撒密码加解密方法。
# 原文字符P,其密文字符C满足如下条件：
# C=(P+10451)mod20902
# 解密与加密方法一致，满足：
# P=（C+10451)mod20902
# 标点符号、英文字母不加密。  全国计算机等级考试二级Python语言程序设计
# s = input("")
# d = {}
# for c in [0x4e00, 0x9fa5]:
#     for i in range(20902):
#         d[chr(i + c)] = chr((i + 10451) % 20902 + c)
# print("".join([d.get(c, c) for c in s]))


# 002-1
# 使用turtle库绘制树图形，效果如下图所示
# import turtle as t
# def tree(length,level):#树的层次
#     if level <= 0:
#         return
#     t.forward(length)  #前进方向画 length距离
#     t.left(45)
#     tree(0.6*length,level-1)
#     t.right(90)
#     tree(0.6*length,level-1)
#     t.left(45)
#     t.backward(length)
#     return
# t.pensize(3)
# t.color('green')
# t.left(90)
# tree(100,6)

# 2
# 获得用户输入的一组数字，采用逗号分隔，输出其中的最大值。
# data = input()
# print(max(data.split(',')))

# 3
# # 以123为随机数种子，随机生成10个在1到999（含）之间的随机数，以逗号分 隔，打印输出，请补充横线处代码。提示代码如下
# #
# import random
# random.seed(123)
# for i in range(10):
#     print(random.randint(1, 999), end=",")

# 4
import jieba

# 从键盘输入一个中文字符串变量s，内部包含中文逗号和句号。参考程 序框架文件，补充代码完成程序。
# 问题：计算字符串s中的中文字符个数，不包括中文逗号和句号字符。 示例如下：
# 输入：没有人不爱惜他的生命，但很少人珍视他的时间。
# 输出：中文字符数为20。
# s = input("请输入一个中文字符串，包含逗号和句号：")
# temp = ['，', '。']
# n = 0
# for i in s:
#     if i in temp:
#         continue
#     else:
#         n+=1
# print("\n中文字符数为{}。".format(n))
# 问题2：用jieba分词后，显示分词的结果，用"分隔，并显示输出分词 后的中文词语的个数及中文字符数，不包含逗号和句号。示例如下：
# 输入：没有人不爱惜他的生命，但很少人珍视他的时间。
# 输出：没有/人/不/爱惜/他/的/生命/但/很少人/珍视/他/的/时间
# # 中文词语数为14。
# # # 中文字符数为20。
# import jieba
#
# s = input("请输入一个中文字符串，包含逗号和句号：")
# temp = ['，', '。']
# k = jieba.lcut(s)
# m = 0
# n = 0
# for i in s:
#     if i in temp:
#         continue
#     else:
#         n += 1
# for i in k:
#     # if else一行的写法！ 加括号 防止运算符优先级
#     m = m + (1 if i not in temp else 0)
#     print("{}/".format(i), end='') if i not in temp else print('', end='')
#     # m, x, flag = m + 1 if i not in temp else 0, print("{}".format(i), end='') if str('flag') in dir() else print(
#     #     "{}".format(i), end='/'), True
# print("\n中文词语数为{}。".format(m))
# print("中文字符数为{}。".format(n))


# 5
# 文本文件"红楼梦.txt"中包含了《红楼梦》小说前20章内容，“停用词.txt"包含了 需要排除的词语。请修改模板，实现以下功能。
# 1.对“红楼梦.xt”中文本进行分词，并对人物名称进行归-化处理，仅归一化以下内 容：凤姐、凤姐儿、凤丫头归-为凤姐
# 2.不统计"停用词.txt"文件中包含词语的词频（名字必须大于一个字）。宝玉，597 凤姐，296
# 3.提取出场次数不少于40次的人物名称，将人物名称及其出场次教按照递减排序 保存到result.csv文件中，
# 出场次数相同的.则按照人物名称的字符顺序排序。

# import jieba
#
# f = "红楼梦.txt"
# sf = "停用词.txt"
# # 读取停用词
# l = open(sf, 'r').readlines()
# lr = []
# for i in l:
#     i = i.strip()
#     lr.append(i)
# # print(lr)
# ff = open(f, 'r')
# fr = ff.read()
# fs = []
# lfr = jieba.lcut(fr)
# # 剔除停用词
# for i in lfr:
#     if i not in lr:
#         fs.append(i)
# # 初始化字典
# fj = {'凤姐', '凤姐儿', '凤丫头'}
# by = {'宝玉', '二爷', '宝二爷'}
# dy = {'黛玉', '颦儿', '林妹妹','黛玉道'}
# bc = {'宝钗', '宝丫头'}
# jm = {'贾母', '老祖宗'}
# xr = {'袭人', '袭人道'}
# jz = {'贾政', '贾政道'}
# jl = {'贾琏', '贾琏道'}
# name_count= {}
# for i in fs:
#     # i = i.strip()
#     if i.strip() == '': continue
#     if i in fj:
#         name_count['凤姐'] = name_count.get('凤姐', 0) + 1
#     elif i in by:
#         name_count['宝玉'] = name_count.get('宝玉', 0) + 1
#     elif i in dy:
#         name_count['黛玉'] = name_count.get('黛玉', 0) + 1
#     elif i in bc:
#         name_count['宝钗'] = name_count.get('宝钗', 0) + 1
#     elif i in jm:
#         name_count['贾母'] = name_count.get('贾母', 0) + 1
#     elif i in xr:
#         name_count['袭人'] = name_count.get('袭人', 0) + 1
#     elif i in xr:
#         name_count['袭人'] = name_count.get('袭人', 0) + 1
#     elif i in jz:
#         name_count['贾政'] = name_count.get('贾政', 0) + 1
#     elif i in jl:
#         name_count['贾琏'] = name_count.get('贾琏', 0) + 1
# #     注意处理其他的
#     else:
#         name_count[i] = name_count.get(i, 0)+1
# ff.close()
# print(name_count)
# items = list(name_count.items())
# items.sort(key=lambda x:x[1], reverse=True)
# # 此行语句可以对items列表进行递减排序
# with open('result-name.csv','w') as f:
#     for i in items:
#         if i[1] > 40 and len(i[0]) >= 2:
#             f.write('{}:{}\n'.format(i[0], i[1]))
# f.close()


#
# 键盘输入一个9800到9811之间的正整数n,作为Unicode编码，把n-1、n和n+1三个
# Unicode编码对应字符按照如下格式要求输出到屏幕：宽度为11个字符，加号字符 +填充，居中。
# n = eval(input("请输入一个数字:"))
# print("{:=^11}".format(chr(n)+chr(n-1)+chr(n+1)))

# 003-1
# 编写程序，从键盘上获得用户连续输入且用逗号分隔的若干个数字（不必以逗号结 尾)，计算所有输入数字的和并输出，给出代码提示如下。
# n = input()
# nums = n.split(',')
# s = 0
# for i in nums:
#     s += int(i)
# print(s)

# 2
# 某商店出售某品牌运动鞋，每双定价160,1双不打折，2双（含)到4双（含)打9 折，5双（含）到9双（含）打8折，10双（含)以上打7折，
# 键盘输入购买数量，屏 幕输出价格总额（保留整数）。格式如下
# n = eval(input("请输入数量："))
# cost = 0
# if n == 1:
#     cost = 160
# elif 2 <= n <= 4:
#     cost = int(n * 160 * 0.9)
# elif 5 <= n <= 9:
#     cost = int(n * 160 * 0.8)
# else:
#     cost = int(n * 160 * 0.7)
# print("总额为:", cost)

# 3
# 将程序里定义好的sd列表里的姓名和成绩与已经定义好的模板拼成一段话，显示在 屏幕上。
# std = [['张三', 90, 87, 95], ['李四', 83, 80, 87], ['王五', 73, 57, 55]]
# modl = "亲爱的{}, 你的考试成绩是: 英语{}, 数学{}, Python语言{}, 总成绩{}.特此通知."
#
# for st in std:
#     cnt = 0
#     for i in range(1, 4):
#         cnt += st[i]
#     print(modl.format(st[0], st[1], st[2], st[3], cnt))

# 4
# 吏用turtle库绘制如下图的花形图形
# import turtle
# for i in range(4):
#     turtle.right(90)
#     turtle.circle(100, 180)

# 5
# 使用字典和列表型变量完成最有人气的明星的投票数据分析。投票信息由附件里的 文件vote.txt给出，
# 一行只有一个明星姓名的投票才是有效票。有效票中得票最多 的明星当选最有人气的明星。
# 问题一：请统计有效票张数。在编程模板中补充代码完成程序。
# f = open("vote-mx.txt", encoding="utf-8")
# names = f.readlines()
# f.close()
# n = 0
# for name in names:
#     num = name.split(' ')
#     if len(num) == 1:
#         n += 1
# print("有效票{}张".format(n))

# 6
# 问题二：请给出当选最有人气明星的姓名和票数，右侧编程模板中补全代码，可删除 横线，随意修改代码，完成程序。
# f = open("vote-mx.txt", encoding="utf-8")
# names = f.readlines()
# f.close()
# D = {}
# for name in names:
#     if len(name.split(' ')) == 1:
#         D[name[:-1]] = D.get(name[:-1], 0) + 1
# l = list(D.items())
# l.sort(key=lambda s: s[1], reverse=True)
# name = l[0][0]
# score = l[0][1]
# print("最具人气明星为:{},票数为:{}".format(name, score))


# 7
# 某班学生评选一等奖学金，学生的10门主干课程成绩存在附件score.txt中，每行为
# 一个学生的信息，分别纪录了学生学号、姓名以及10门课成绩，格式如下：
# 1820161043郑珉镐68668377567361696678
# 1820161044沈红伟91708191968078918994

# 题1：给出按总成绩从高到底排序的前10名学生名单，并写入文件
# top_score_10.txt,每行纪录一个学生的信息，分别为学生学号、姓名以及10门课成 绩。补充，修改编程模板中的代码完成这些功能。

L = []  # L中的元素是学生原始成绩和总成绩
f = open("../data/score-data.txt", 'r')
fr = f.readlines()
f.close()
ld = {}
for i in fr:
    i = i.strip()
    temp = i.split(' ')
    s = temp[2:]
    sum = 0
    for j in s:
        sum += int(j)
    ld[i] = sum
L = list(ld.items())
L.sort(key=lambda x: x[-1], reverse=True)  # 按学生总成绩从大到小排序
res = L[0:10]
with open("../data/top_score_10.txt", 'w') as f1:
    for i in res:
        f1.write('{}\n'.format(i[0]))
# 问题2：读取文件top_score_10.txt,从中选出候选人，并将学号和姓名写入文件 top10.txt,格式如下：
# 1010112161722张三
# 1010112161728李四
# 补充修改模板，完成这一功能。
f = open("../data/top_score_10.txt", 'r', encoding="utf-8")
lines = f.readlines()
f.close()
D = []
f = open('../data/top10.txt', 'w', encoding="utf-8")
ds = {}
for i in lines:
    i = i.strip().split(' ')
    k = ' '.join(i[:2])
    s = i[2:]
    ds[k] = s
for key in ds:
    flag = True
    for i in ds[key]:
        if int(i) < 60:
            flag = False
            break
    if flag:
        f.write('{}\n'.format(key))
f.close()
