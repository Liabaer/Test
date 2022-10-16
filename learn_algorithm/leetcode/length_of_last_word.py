# -*- coding: utf-8 -*-
# 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中最后一个单词的长度。
# 单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
s = "   fly me   to   the moon  "

i = len(s) - 1
sum = 0
flag = True
while i >= 0:
    if s[i] == ' ' and flag == True:
        i = i - 1
        # flag = False
        continue
    else:
        flag = False
    if s[i] == ' ' and flag == False:
        break
    print(s[i], flag)
    sum = sum + 1
    i = i - 1
print(sum)
