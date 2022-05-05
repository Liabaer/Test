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

# 求1010二进制转十进制
c=0b1010
print(c)

# 0101的
c=0x0101
print(c)
