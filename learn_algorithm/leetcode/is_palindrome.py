# -*- coding: utf-8 -*-
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
s = "A man, a plan, a canal: Panama"
s = " "
s_new = s.lower()
flag = True
i = 0
new = ''
while i < len(s_new):
    if 122 >= ord(s_new[i]) >= 97:
        new = new + s_new[i]
    if 48 <= ord(s_new[i]) <= 57:
        new = new + s_new[i]
        print(new)
    else:
        i = i + 1
        continue
    i = i + 1
print(new)
m = 0
n = len(new) - 1
while m < n:
    if new[m] != new[n]:
        flag = False
        break
    m = m + 1
    n = n - 1
print(flag)

# 这是自己的方法，不灵巧
# while m < len(new):
#     while n >= 0:
#         if new[m] != new[n]:
#             flag = False
#             break
#         if new[m] == new[n]:
#             flag = True
#             n = n - 1
#             m = m + 1
#             break
#         n = n - 1
#     if flag == False:
#         break
# print(flag)
