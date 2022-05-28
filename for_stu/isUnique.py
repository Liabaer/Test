# -*- coding: utf-8 -*-
# 实现一个算法，确定一个字符串 s 的所有字符是否全都不同。
astr ="abc"

i = 0
j = 0
flag = True
#
# while i < len(astr):
#     j = i + 1
#     while j < len(astr):
#         print astr[i], astr[j]
#         if astr[i] == astr[j]:
#             flag = False
#             break
#         j = j + 1
#     if flag == False:
#         break
#     i = i + 1
#
while i < len(astr):
    while j < len(astr)-1:
        j = j + 1
        print(i, j)
        print(astr[i], astr[j])
        if astr[i] == astr[j]:
            flag = False
            break
    i = i + 1
    j = i
    if flag == False:
        break

# print flag