# -*- coding: utf-8 -*-
# 给定一个段落 (paragraph) 和一个禁用单词列表 (banned)。返回出现次数最多，同时不在禁用列表中的单词。
#
# 题目保证至少有一个词不在禁用列表中，而且答案唯一。
#
# 禁用列表中的单词用小写字母表示，不含标点符号。段落中的单词不区分大小写。答案都是小写字母。
paragraph = "Bob. hIt, baLl"
paragraph = paragraph.lower()
banned = ["bob", "hit"]
str = "!?',;."
par = []
temp = ''
i = 0
while i < len(paragraph):
    # 简洁写法
    if paragraph[i] == ' ' or paragraph[i] in str:
        if temp != '':
            par.append(temp)
        temp = ''
    else:
        temp = temp + paragraph[i]
    i = i + 1
if temp != '':
    par.append(temp)
    # 我的啰嗦写法
    # if i == 0 and paragraph[i] == ' ':
    #     i = i + 1
    #     continue
    # if i == len(paragraph) - 1 and paragraph[i] != ' ':
    #     if paragraph[i] not in str:
    #         temp = temp + paragraph[i]
    #     par.append(temp)
    #     temp = ''
    #     i = i + 1
    #     continue
    # if paragraph[i] == ' ' or paragraph[i] in str:
    #     if temp != '':
    #         par.append(temp)
    #     temp = ''
    #     i = i + 1
    #     continue
    # if paragraph[i] in str:
    #     i = i + 1
    #     continue
    # if paragraph[i] != ' ':
    #     temp = temp + paragraph[i]
    # print(temp)
    # i = i + 1
print(par)
pa = {}
j = 0
while j < len(par):
    print(par[j])
    if par[j] not in pa:
        pa[par[j]] = 1
    else:
        pa[par[j]] = pa[par[j]] + 1
    j = j + 1
print(pa)
num = 0
k_max = ''
for k, v in pa.items():
    if k in banned:
        continue
    if v > num:
        num = v
        k_max = k
print(k_max)
