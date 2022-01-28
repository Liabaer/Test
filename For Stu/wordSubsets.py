# -*- coding: utf-8 -*-
# 给你两个字符串数组 words1和words2。
#
# 现在，如果b 中的每个字母都出现在 a 中，包括重复出现的字母，那么称字符串 b 是字符串 a 的 子集 。
#
# 例如，"wrr" 是 "warrior" 的子集，但不是 "world" 的子集。
# 如果对 words2 中的每一个单词b，b 都是 a 的子集，那么我们称words1 中的单词 a 是 通用单词 。
#
# 以数组形式返回words1 中所有的通用单词。你可以按 任意顺序 返回答案。
from typing import List, Dict

words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["lo", "eo"]


def calc_dict(i, j, words, temp ) -> Dict[str, int]:
    while j < len(words[i]):
        if words[i][j] in temp:
            temp[words[i][j]] = temp[words[i][j]] + 1
        else:
            temp[words[i][j]] = 1
        j = j + 1
    return temp


# words2 = set(words2)
i = 0
temp3 = {}
while i < len(words2):
    j = 0
    temp2 = {}
    temp2 = calc_dict(i, j, words2, temp2)
    for k, v in temp2.items():
        if k in temp3:
            if v >= temp3[k]:
                temp3[k] = v
        else:
            temp3[k] = v
    i = i + 1
print((temp3))
res = []

m = 0
while m < len(words1):
    temp = {}
    n = 0
    flag = False
    temp = calc_dict(m, n, words1, temp)
    for k, v in temp3.items():
        if k in temp:
            print(k, v)
            if v <= temp[k]:
                flag = True
            else:
                flag = False
                break
        else:
            flag = False
            break
    if flag:
        res.append(words1[m])
    m = m + 1
print(res)

# i = 0
# while i < len(words1):
#     j = 0
#     # print(words1[i])
#     flag = False
#     while j < len(words2):
#         print(words2[j])
#         print(words1[i])
#         if words2[j] in words1[i]:
#             flag = True
#         else:
#             flag = False
#             j = j + 1
#         j = j + 1
#     if flag:
#         temp.append(words1[i])
#     i = i + 1
# print(temp)
