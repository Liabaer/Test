# # -*- coding: utf-8 -*-
# x = 10
# # 二进制输出
# print(bin(x))
# print('{:#b}'.format(x))
# # 不输出前缀
# print('{:b}'.format(x))
# # 十六进制
# # 因为是16进制，0-9 a b c d e f是一轮 -->  10进制的10对应的就是16进制的a
# print(hex(x))
# print('{:#x}'.format(x))
# print('{:x}'.format(x))
# # 八进制
# print(oct(x))
# print('{:#o}'.format(x))
# print('{:o}'.format(x))



# 二进制
# 0b表示该数字是二进制数字，二进制由0和1组成

# 二进制转化十进制原理
# 首先从右边到左边开始计算(注意是从右边到左边)
# x = 0 * 2^0 + 1 * 2 ^ 1 + 0 * 2 ^ 2 + 1 * 2 ^ 3
# a = 0b1010
# print(0 * pow(2, 0) + 1 * pow(2, 1) + 0 * pow(2, 2) + 1 * pow(2, 3))
# # print会直接打印10进制的值
# print(a)
# # 使用int函数计算二进制，我们之前使用的int函数都是int('56'),其实是int('56',10),表示56这个字符串是10进制的,int函数会将任意进制的字符串转换为10进制
# print(int('0b1010', 2))


# # 十进制转二进制原理
# a = 11
# s_list = []
# # 计算原理：通过辗转相除法一直除以2，然后把余数放入到新的数组里，最后将新的数组倒序就是二进制
# while a != 0:
#     s_list.append(str(a % 2))
#     a = a // 2
# s_list.reverse()
# print('0b' + ''.join(s_list))
#
# # 使用函数计算二进制
# a = 11
# # 会打印0b的前缀
# print(bin(a))
# print('{:#b}'.format(a))
# # 不打印前缀
# print('{:b}'.format(a))
#
#
# # 八进制 由0，1，2，3，4，5，6，7组成的数字，由0o前缀表示第一是零，第二个是小写字母o
# a = 0o17
# # 八进制转十进制原理和二进制一样，只是把2的次方换成8的次方
# # x = 7 * 8^0 + 1 * 8 ^ 1
# print(7 * pow(8, 0) + 1 * pow(8, 1))
# # print会直接打印10进制的值
# print(a)
# print(int('0o17', 8))
#
# # 十进制转八进制原理
# a = 15
# s_list = []
# # 计算原理：通过辗转相除法一直除以8，然后把余数放入到新的数组里，最后将新的数组倒序就是二进制
# while a != 0:
#     s_list.append(str(a % 8))
#     a = a // 8
# s_list.reverse()
# print('0o' + ''.join(s_list))
#
# # 十进制 转 八进制
# a = 15
# # 会打印0o的前缀
# print(oct(a))
# print('{:#o}'.format(a))
# # 不打印0o前缀
# print('{:o}'.format(a))


# 16进制 由0，1，2，3，4，5，6，7, 8, 9, A,B,C,D,E,F组成的数字，由0x前缀表示第
# a = 0xAB
# # 16进制转2进制原理和二进制一样，只是把2的次方换成16的次方,注意A,B,C,D,E依次是10，11，12，13，14,15
# # x = 12 * 16 ^ 0 + 11 * 16 ^ 1
# print(11 * pow(16, 0) + 10 * pow(16, 1))
# # print会直接打印10进制的值
# print(a)
# print(int('0xAB', 16))
#
# # # 十进制转十六进制原理
# a = 171
# s_list = []
# # 计算原理：通过辗转相除法一直除以16，然后把余数放入到新的数组里，最后将新的数组倒序就是二进制
# while a != 0:
#     s_list.append(str(a % 16))
#     a = a // 16
# s_list.reverse()
# print('0x' + ''.join(s_list))
# #
# # 十进制 转 十六进制
# a = 171
# # 会打印0x前缀
# print(hex(a))
# print('{:#x}'.format(a))
# # 不会打印0x前缀
# print('{:x}'.format(a))

#
# # 另外二进制到八进制，二进制到十六进制，都可以通过先到10进制再进行转换

# 将0b1011抓换成 十六进制
# 先到十进制
a = int('0b1011', 2)
# 再到十六进制
print(hex(a))