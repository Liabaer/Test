# -*- coding: utf-8 -*-
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
s = "leetcode"

i = 0
dict_a = {}
while i < len(s):
    if s[i] not in dict_a:
        dict_a[s[i]] = '1' + ',' + str(i)
    else:
        tmp = dict_a[s[i]].split(',')
        dict_a[s[i]] = str(int(tmp[0]) +1) + ',' + str(i)
    i = i + 1
print(dict_a)
m = -1
for x, y in dict_a.items():
    # print(x,y)
    z = y.split(',')
    if int(z[0]) == 1:
        if m == -1:
            m = int(z[1])
        if m >= int(z[1]):
            m = int(z[1])
print(m)
