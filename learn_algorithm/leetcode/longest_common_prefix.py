# -*- coding: utf-8 -*-
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。
strs = ["ab", "a"]
m = 0
new_strs = {}
while m < len(strs):
    n = 0
    new_str = ''
    while n < len(strs[m]):
        # print(strs[m][n])
        new_str = new_str + strs[m][n]
        print(new_str)
        if new_str not in new_strs:
            new_strs[new_str] = 1
        else:
            new_strs[new_str] = new_strs[new_str] + 1
        n = n + 1
    m = m + 1
print(new_strs)
i = 0
j = ""
lenth = 0
for k, v in new_strs.items():
    if v == len(strs):
        if lenth < len(k):
            lenth = len(k)
            i = v
            j = k
print(j)
