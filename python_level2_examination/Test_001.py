# -*- coding: utf-8 -*-
# 1
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
s = input("")
d = {}
for c in [0x4e00, 0x9fa5]:
    for i in range(20902):
        d[chr(i + c)] = chr((i + 10451) % 20902 + c)
print("".join([d.get(c, c) for c in s]))