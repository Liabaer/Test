# -*- coding: utf-8 -*-

# 给一非空的单词列表，返回前 k 个出现次数最多的单词。
#
# 返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。

words = ["i", "love", "leetcode", "i", "love", "coding"]

k = 3

words_dict = {}

i = 0
while i < len(words):
    if words[i] not in words_dict:
        words_dict[words[i]] = 1
    else:
        words_dict[words[i]] = words_dict[words[i]] + 1
    i = i + 1
print(words_dict)

# 使用函数比较
# temp = sorted(words_dict.items(), key=lambda item: (-item[1], item[0]))[0:k]

#  plus版本  -->res = [x for x in 数组]
res = [value[0] for value in sorted(words_dict.items(), key=lambda item: (-item[1], item[0]))[:k]]

print(res)
