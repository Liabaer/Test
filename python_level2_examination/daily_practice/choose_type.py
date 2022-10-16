# -*- coding: utf-8 -*-
# 在___补充一行代码
# 编写代码替换横线，不修改其他代码，实现下面功能：
# 用户按照列表格式输入数据，将用户输入的列表中属于字符串类型的元素 连接成一个整字符串，并打印输出。   [123,"Python",98,"等级考试"]

# eval函数会自动讲字符串格式化成对应的格式
# input输入的都是字符串，比如input，键盘输入了5，其实得到的是5的字符串，eavl会转换成整形的5
# 比如题目里输入的其实是个数组格式，所以ls被eval转成了数组
ls = eval(input())
s = ""
print(type(ls))
for item in ls:
    print(type('香山'))
    if type(item) == type('香山'):
        s += item
print(s)
