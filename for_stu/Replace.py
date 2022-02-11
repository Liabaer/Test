# -*- coding: utf-8 -*-
# s = "We are happy."
# a = ''
# for b in range(0, len(s)):
#     if s[b] == ' ':
#         a = a + "%20"
#     else:
#         a = a + s[b]
# print(a)


a = [1, 2, 3, 2, 2, 2, 5, 4, 2]
c = {}
for b in range(0, len(a)):
    if a[b] not in c:
        c[a[b]] = 1
    else:
        c[a[b]] = c[a[b]] + 1
print(c)
for i in c:
    if c[i] > len(a)/2:
        print(i)



# 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
# import collections
#
# s = "leetcode"
# b  = collections.OrderedDict()
# for i in range(0, len(s)):
#     if s[i] not in b:
#         b[s[i]] = 1
#     else:
#         b[s[i]] = b[s[i]] + 1
# print(b)
# a = ' '
# for j in b:
#     if b[j] == 1:
#         a = j
#         break
# print(a)






