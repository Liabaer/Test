# -*- coding: utf-8 -*-
# 合你一个字符串数组w0ds，找出并返回数组中的第一个回文字符串。如果不存在满足要求的字符串，返回一个空字符串
#  回文字符串的定义为：如果一个字符串正着读和反着读一样，那么该字符串就是一个回文字符串。

words = ["xngla", "e", "itrn", "y", "s", "pfp", "rfd"]
flag = False
for i in words:
    l = 0
    r = len(i) - 1
    # print(i)
    while l <= r:
        if i[l] == i[r]:
            flag = True
        else:
            flag = False
            break
        l += 1
        r -= 1
    if flag:
        print(i)
        break
if not flag:
    print('')
