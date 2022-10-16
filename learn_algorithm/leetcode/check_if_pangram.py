# -*- coding: utf-8 -*-
# 全字母句 指包含英语字母表中每个字母至少一次的句子。
#
# 给你一个仅由小写英文字母组成的字符串 sentence ，请你判断  sentence 是否为 全字母句 。
#
# 如果是，返回 true ；否则，返回 false 。
sentence = "leetcode"
temp = "qwertyuiopasdfghjklzxcvbnm"
flag = True
i = 0
if len(sentence) < 25:
    flag = False
    # print(flag)
else:
    while i < len(temp):
        if temp[i] not in sentence:
            flag = False
        i = i + 1
print(flag)
