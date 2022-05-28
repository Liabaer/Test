# -*- coding: utf-8 -*-
# 004
# 1
# 获得用户输入的一个字符串，将字符串逆序输出，同时紧接着输出该字所包含字符的个数。示例如下：

# s = input()
# print(s[::-1], end='')
# print(len(s))

# 2
# 根据斐波那契数列的定义，F(0)=0,F(n)=1,F(n)=F(n-1)+F(n-2) (≥2)，输出不大于100的序列元素。屏幕输出示例：0,1,1,2,3…

# a, b = 0, 1
# while a < 100:
#     print(a, end=',')
#     a, b = b, a+b

# 3
# 使用程序计算整数N到整数N+100之间所有奇数的数值和，不包含N+100,并将结 果输出。整数N由用户给出，代码片段如下，补全代码。不判断输入异常。
# N = input("请输入一个整数: ")
# n = eval(N)
# s = 0
# for i in range(n, n+100):
#     if i % 2 != 0:
#         s += i
# print(s)

# 4
# 使用 turtle库的turtle.circle()函数和turtle.seth()函数绘制同心圆套圈，
# 最小的圆圈半径为10像素，不同圆圈之间的半径差是40像素，效果如下 图所示。

# import turtle
# r = 10
# dr = 40
# for i in range(4):
#     turtle.pendown()
#     turtle.circle(r)
#     r += dr
#     turtle.penup()
# 改变画笔的方向从下方画起
#     turtle.seth(-90)
#     turtle.fd(dr)
# 改变画笔的方向使圆能同心
#     turtle.seth(0)
# turtle.done()

# 5
# 将列表1s=[23,45,78,87,11,67,89,13,243,56,67,311,431,111,141] 中的素 数去除，
# 并输出去除素数后列表1s的元素个数。


# def is_prime(n):
#     flag = True
#     for i in range(2, n):
#         if n % i == 0:
#             flag = False
#     return flag
#
# ls = [23,45,78,87,11,67,89,13,243,56,67,311,431,111,141]
# for i in ls.copy():
#     if is_prime(i):
#         ls.remove(i)
# print(len(ls))

# 6
# 附件文件question.txt中有若干道Python选择题目，
# 第1行的第1个数据为题号，后续 的4行是4个选项，接下来是第二道题。示例内容如下：
# 读取其中的内容，提取题干和四个选项的内容，利用jiba分词并统计出现频率最高 的3个词，其中要删除以下的常用字和符号
# 第一个字符是空格
# 作为该题目的主题标签，显示输出在屏幕上。
import jieba
fi = open("question.txt", 'r')
f = fi.readlines()
# print(f)
fi.close()
temp = list('的，：：可以是和中或一个以下“”了其时产生DBC')
st = {}
new_f = []
s = ''
key = ''
kls = []
for i in f:
    i = i.strip()
    t = i.split('.')[0]
    if t != 'A' and t != 'B' and t != 'C' and t != 'D':
        key = t
        kls.append(t)
        s = i
    else:
        s += i
    # s += i
    # print(s)
    st[key] = s
# print(st)

for i in st:
    txt = ''
    dr = {}
    for j in st[i]:
        if j in temp:
            continue
        else:
            txt += j
    # print(txt)
    txt = txt.strip(' ')
    t = jieba.lcut(txt)
    for k in t:
        dr[k] = dr.get(k,0)+1
    dl = list(dr.items())
    dl.sort(key=lambda x: x[-1], reverse=True)
    print('第{}题的主题是:'.format(i))
    for res in range(3):
        print('{}:{}'.format(dl[res][0],dl[res][1]))