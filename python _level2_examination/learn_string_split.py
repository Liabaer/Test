# -*- coding: utf-8 -*-
# 对于字符串或者数组，可以通过切片来进行分割
# s[m:n]就表示截取从m到n-1位的字符串 m等于0可以写成s[:n]
# s = "abcde"
# # 从第0位到第2位的字符串
# # print(s[0:3])
# # 但是不会改变s
#
# # # # 除非让他等于他
# # s = s[0:3]
# # print(s)
# # # 如果要倒着截取
# a = "abcde"
# # 倒数第一个元素的索引可以是4也可以是-1
# print(a[-1])
# # 后n个数a[-n:]
# print(a[-1:])
# print(a[-2:])
#
# # 后n到m个数  m是<m 左闭右开
# print(a[-3:-1])

# 反转
# print(a[::-1])

# 上述那些除了字符串，数组也支持
# {:^n}表示格式化字符串,居中对齐长度为n, ^前面没有表示用空格补齐，所以^前面可以自定义字符串
# {:*>30} 右对齐长度为30，不足用*补齐
# {:*<30} 左对齐长度为30，不足用*补齐
# print('{:^30}'.format("ab"))
# print('{:*>30}'.format("ab"))
# print('{:+<30}'.format("ab"))


# 判断字符串是不是数字
# s = "a"
# print(s.isdigit())
# s = "1"
# print(s.isdigit())

# 判断字符串是不是数字或者字母 但是不支持判断中文哦！！！
# s = 'a'
# print(s.isalnum())
# s = '1a'
# print(s.isalnum())
# s = '1a@'
# print(s.isalnum())
# 判断是不是只是字母  但是不支持判断中文哦！！！
# s = '世界'
# print(s.isalpha())
# s = '1a'
# print(s.isalnum())
# 判断是不是小写
# s = 'a'
# print(s.islower())
# s = 'A'
# print(s.islower())
# 判断是不是大写
# s = 'a'
# print(s.isupper())
# s = 'A'
# print(s.isupper())

# # 大写转小写
# s = 'Tt'
# print(s.lower())
# # 小写转大写
# s = 'Tt'
# print(s.upper())

# # %可以链接字符串
# s = '%s + %s' % ("a", "b")
# print(s)
#
# # 乘号支持字符串
# s = "abc" * 3
# print(s)

# 计算字符串a在字符串b中出现多少次
# s = "dayday day day up"
# # s.count('str', x, y)统计，str在s的第x到y位出现过多少次  统计0到最后一位dayday出现多少次
# print(s.count('day', 0, len(s)))
# print(s.count('day', 0, 7))

# 判断字符串a是否出现在字符串b中,存在返回最开始出现的下标不存在返回-1
# s = 'yanxuliabaer'
# print(s.find('lia'))
# print(s.find('day'))

# strip 删除两边的空白字符串 比如\t和\n是空白字符
s = "\tsss\n"
print("----")
print(s)
print("----")
print(s.strip())
print("----")

# split分割字符串
s = "1-a,2-b,3-c:b:ccc:d"
print(s.split(":")[0].split(",")[0].split("-"))