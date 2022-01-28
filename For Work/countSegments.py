# -*- coding: utf-8 -*-
# 统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
#
# 请注意，你可以假定字符串里不包括任何不可打印的字符。

s = "Of all the gin joints in all the towns in all the world,   "
count =0
i = 0
flag = True
while i < len(s):
    print(s[i])
    if i == len(s) - 1 and s[i] !=' ':
        count = count + 1
    elif s[i] != ' ':
        flag = False
        i = i + 1
        continue
    else:
        if s[i] == ' ' and flag == False:
            flag = True
            count = count + 1
            print(count)
    i = i + 1
print(count)