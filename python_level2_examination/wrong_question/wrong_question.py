# -*- coding: utf-8 -*-
# 1.当s是函数内的局部变量时，不能在函数外面使用，如果在外面使用的话，就是全局变量了，需要重新定义。相当于此s非彼s

# 表达值是false、None、0时，flag为flase,其他都是true

# reverse 的排序规则 reverse = true是降序 默认是false，是升序

# ss = [2, 3, 6, 9, 7, 1]
# for x in ss:
#     print(max(ss), end=',')
#     ss.remove(max(ss))
#     print(ss)
#
# # for循环内部等价于while循环，如下
# ss = [2, 3, 6, 9, 7, 1]
# i = 0
# while i < len(ss):
#     i = i + 1
#     print(max(ss), end=',')
#     ss.remove(max(ss))

# cs = {'aa': 4, "bb": 6}
# # 循环的是key,然后通过cs[key]取value
# for key in cs:
#     print(key, cs[key])
# # 直接循环key, value
# for key, value in cs.items():
#     print(key, value)
#
# a = {'a': 11, 'b': 5, 'c': 3}
# a.pop('c')
# print(a)

# 不写return或则只写return 等价于return None
# s = 0
# def fun(s, n):
#     for i in range(n):
#         s += i
#         print(s, i)
# print(fun(s,5))

# python里面等号的作用是赋值这个你肯定知道，但是其实给他的是地址，然后我们打印的时候打印的是地址上面的值
# 相当于在数组（内存）中找一个位置（地址）存放[10]这个变量
# ls = [10]
# print('ls当前内存地址是=', id(ls))
# def run(n):
#     ls.append(n) # ls是全局变量，我们执行a.append(n)，首先会找到这个位置，然后把n也一起放入到这个位置，于是这个位置的里面存放的东西就变成了[10,5]
#     print('ls当前内存地址是=', id(ls))
# run(5)
# print(ls)
#
# ls = 5
# print('ls当前内存地址是=', id(ls))
# def run1(n):
#     ls = n # 用等于号，想当于定义了一个局部变量和全局变量同名，所以全局变量不会修改
#     print('ls当前内存地址是=', id(ls))
# run1(4)
# print(ls)

# 1，random.seed0函数初始化随机数种子，默认值是 当前系统时间；2，random库的随机数是计算机按一定算法产生的， 并非完全随机
# 3，Python内置的random库主要用于产生各种伪随 机数序列； 4 random(a,b)产生一个a（0.0）到（1.0）之间的随机小数

# ss = set("htslbht") -->set()会去重
# print(ss)
# sorted(ss)
# print(ss)
# for i in ss:
#     print(i, end='')

# 文件就是存储在磁盘上的数据，序列的集合，一般是说变量 ，read()就是一口气读出全部的文本


# ls = 1,2 -- 输入元祖哦

# 全局变量以等号形式被引用，不会改变其实际值 ，但是append 或者reverse，clear改变其地址的值，全局变量也会变化
# case 1 -- 不修改a的地址
# a = 10
# b = a
# b = 11
# print(a)
#
# # case 2 -- append修改地址值
# a = [10]
# b = a
# b.append(11)
# print(a)
# #
# # case 3 等号不修改a的地址
# a = [10]
# b = a
# b = [10, 11]
# print(a)

#
# # case 4
# c = 10
# def calc1(a):
#     c = a #
# calc1(11)
# print(c)
#
# # case 5
# c = [10]
# def calc2(a):
#     c.append(a)
# calc2(5)
# print(c)
# #
# # case 6
# c = [10]
# def calc3(a):
#     c = a
# calc3([10, 11])
# print(c)
# #
# # case 7
# c = 10
# def calc4(c):
#     c = 6
# calc4(c)
# print(c)
#
# # case8
# c = [10]
# def calc5(c):
#     c = [11, 12]
# calc5(c)
# print(c)
#
# # # case9
# c = [11]
# def calc6(c):
#     c.append(12)
# calc6(c)
# print(c)
# # #
# # # case10
# c = [11]
# d = [1,1,1]
# def calc7(c=[1,2,3]):
#     # 内部有等号，所以外面不修改全局变量的值
#     # c = []
#     c.append(1)
#     d = c
# # 未传参数，不会修改全局变量
# calc7()
# print(d)
#
# # 传了参数，会修改 （但是内部等号，就不会修改）
# # calc7(c)
# print(c)
#
# # 求1010二进制转十进制
# c=0b1010
# print(c)
#
# # 0101的
# c=0x0101
# print(c)

# import random
# print(type(random.random()))    # <class 'float'>
# # random返回0-1之间的小数
#
# print(random.random())
# # 返回a-b之间的数字，非整数
# print(random.uniform(1, 100))
# # 返回a-b的整数
# print(random.randint(1, 100))


# # 二维数组sort排序默认只排一位
# L2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
# # [5，6，7，8] 和[1,2,3,4]排序： 先比较第一个数字，相等往后比较
# L2.sort(reverse=True)
# print(L2)

# 注意index在循环过程中的变化
at = ['1', '2', '3', '0', '0', '0']
# for i in at:
#     if i == '0':
#         at.remove(i)
#
# print(at)

# dic = {'A':'a','B':'b'}
# print(dic.items())
#
# ls = [123]
# def test():
#     ls.append(1)
#     print(ls)
# test()

# # reverse()不需要重新赋值 如下会输出None 类似的有a = a.sort()  a = a.remove(2)
# 数组里面的方法只有copy需要重新赋值一下，其他都不要重新赋值
# print(s.replace('1','2')也会生效哦，他相当于replace函数有一个返回值，字符串，replace要赋值’
# l = [1, 4, 3]
# lr = l.reverse()
# a = l.sort()
# b = l.remove(1)
# print(b)

# 程序的三种结构指的是：顺序结构，从上到下，选择结构 if else，循环结构 for  while
# 分支结构包括如下三种：单分支，双分支，多分支，二分支结构可以嵌套组合形成多分支结构
# a = 1
# # 单分支
# if a > 1:
#     pass
# # 双分支
# if a > 1:
#     pass
# else:
#     pass
# # 多分支
# if a> 1:
#     pass
# elif a > 2:
#     pass
# elif a > 3:
#     pass


# home（）初始到一开始的位置，然后默认向东
# seth（）是改变箭头的方向但是不移动 seth(0）就是朝向东，默认也是朝向东的。
# 导入所有就是imort turtle  from turtle 是部分导入
# from random import randint
#
# # 通过from的方式就不用random.randint的方式了
# a = randint(1, 100)
# # 但是由于没有全部导入，所以调用其他会报错
# # b = choice([1,2])
# print(a)

# a = 1
# def calc1():
#     print(a)
# def calc():
#     print(z)
# z = 1
# # 上面这两个是等价的，因为函数的定义没有顺序
# # 变量只要在函数外面，他就是全局的，他可以作用用于任何函数中，不管顺序。
# # 但是使用函数的地方一定要在定义函数之后不然会报错
# # calc3()
# def calc3():
#     print(1)
# a = 'pythonn'
# try:
#     s = eval(input("请输入整数："))
#     ls = s*2
#     print(ls)
# except:
#     print("请输入整数：")

# # 三个式子等价
# def calc1():
#     print(1)
#     return
# print(calc1())
# def calc2():
#     print(1)
#     return None
# print(calc2())
# def calc3():
#     print(1)
# print(calc3())


# 字典的初始化方式
# d = {}
# name_list = ['a','b','a','d']
# # 第一种初始化
# for name in name_list:
#     if name not in d:
#         d[name] = 1 # 表示第一次出现记成1
#     else:
#         d[name] = d[name] + 1 # 叠加出现的次数
# print(d)
#
# # 第二种初始化
# d = {}
# for name in name_list:
#     d[name] = d.get(name, 0) + 1 # d.get(name,i)写法，如果name不存在d中，那么就取默认值0
# print(d)

# / 商， //整数商  % 取余数

# 36 再次记住进制！！！
# 给定一个整数数字0x1010，请依次输出Python语言中十六进制、十进制、八进制 和二进制表示形式，使用英文逗号分隔。
# n = 0x1010
# print('{},{},{},{}'.format(hex(n),int(n), oct(n),bin(n)))

# print(0.1+0.2 == 0.3)
#
# def fun(a=3,b):    可变参数是一个*
#     return
# 选填参数，必须放在不选填参数前面
# def fun(a=3,b):
#     return a + b
# def fun(a, b=3):
#     return a + b
# # b使用默认的3，没传
# print(fun(1))
#
# # 可变参数,必须放在最后一个*号，将最后的n个参数组成元祖
# def fun(a=3, *b):
#     print(a, b)
# fun(3, 4, 5, 6, 7)


# 整数变为unicode是用chr

# 10%@==
# 20%@====
# 100%@============
# 文本中左侧一段输出N的值，右侧一段根据N的值输出等号，中间用@分隔，等号 个数为N与5的整除商的值，例如，当N等于10时，输出2个等号。
# n = eval(input()) #N取值范围是0一1O0
# print('{2}%@{0:=<{1}}'.format(n, n,n//5))
# print(''.format())


# python将数字变为千分位

# 注意！！ 以下写法只能针对数字
print("{:,d}".format(123444))
# 设置对齐,d需要放到最后面
print("{:>,d}".format(123444))
# 设置宽度还是,d放在最后
print("{:>15,d}".format(123444))
# 调用format函数
print(format(123344, ','))
