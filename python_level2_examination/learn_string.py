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
# # 判断字符串中是否存在目标，第二个参数是从字符串的第i位开始判断,存在会返回第一次出现的元素的下标（比如一个元素中有2个a取前面那个）
# print(a.index('a', 0))
# # print(a.index('day', 0)) # 报错不存在day
# # find同理，都是寻找字符串中是否出现过目标字符串
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