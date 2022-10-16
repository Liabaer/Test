# -*- coding: utf-8 -*-
# 字符串相关函数
import string

# a = "testtest"
# # 第一个参数旧值，第二个参数新值，会将a字符串中的旧值换成新值，注意：一定要重复赋值给a才会生效
# a.replace('t', '我')
# print(a)
# a = a.replace('t', '我')
# print(a)


# a = 'abcdea'
# 1.index () 函数 用于从列表中找出某个值第一个匹配项的索引位置。
# 2.index ()方法语法 list.index(x[, start[, end]])
# 3.参数 x-- 查找的对象。 start-- 可选,查找的起始位置。 end-- 可选,查找的结束位置。
# 4.返回值 该方法返回查找对象的索引位置,如果没有找到对象则抛出异常。
# index可以判断指定字符串出现的下标
# .index('a', 0，10)意思，找a里'a'从0到10位之间出现的下标（原字符串的下标哦）
# print(a.index('a', 0))
# # print(a.index('day', 0)) # 报错不存在day
# “find(str，beg，end)函数就是实现检索字符串,并且输出运算值。 ,其主要的作用分别是指定索引、
# 开始索引以及结束索引,输出的返回值是有字符串的就开始索引,没有的直接返回-1。”，find只能判断单个字母出现的下标
# print(a.find('a', 0))
#
# # 字符串支持乘法
# print("aa" * 2)
#
# a = 'abc'
# # 切片中如果只有冒号，则获取整个列表
# print(a[:])
# # # 倒序
# print(a[::-1])
# a = "123456789"
# # # x[a:b:c] 表示从a-b下表范围内（大于等于a小于b)，每隔c个取字符 下面输出1，3，5，7,9
# a = a[0:9:2]
# print(a)
# a = "123456789"
# # 中间的结束不写默认是最后一位(也就是等于数组的长度），所以等价于a[0:9:2]
# a = a[0::2]
# print(a)
# # 负数的话就是b到a的频率 c 例如
# s = 'HelloWorld'
# print(s[5::-2])
#
#
# strip()默认不带参数去重首位的空白字符包含空格回车，也可以指定去除首尾的字符
# a = '\naaa   \n'
# a = a.strip()
# print(a)
# # 去除首位的逗号
# a = ',aaa   ,'
# a = a.strip(",")
# print(a)
#
# # is space 判断字符串是不是只有空格组成
# a = "    "
# print(a.isspace())
# #
# # # 包含键盘上特殊字符 数字 字母的字符串。
# print(string.printable)
# #
# # 字符串还支持注释
# # 比如 三个双引号或者三个单引号，一般用于函数注释
#
# def sum(a, b):
#     """
#     计算a + b 双引号注释
#     :param a:  a
#     :param b:  b
#     :return:
#     """
#     print(a + b)
#
# def sum(a, b):
#     '''
#     计算a + b单引号注释
#     :param a:
#     :param b:
#     :return:
#     '''
#     print(a + b)
