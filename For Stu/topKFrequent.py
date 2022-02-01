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

temp = []
for m, n in words_dict.items():
    temp.append([m, n])
print(temp)

# 使用冒泡排序进行比较
j = 0
while j < len(temp):
    # 从第二位开始比较
    p = j + 1
    while p < len(temp):
        temp_words = ''
        # temp[i][0] temp[i][1]就是k和v
        if temp[j][1] < temp[p][1]:
            # 交换位置：a = b,b = c,c = a
            temp_words = temp[p]
            temp[p] = temp[j]
            temp[j] = temp_words
        elif temp[j][1] == temp[p][1] and temp[j][0] > temp[p][0]:
            # 出现频率相同，比较字母先后顺序
            temp_words = temp[p]
            temp[p] = temp[j]
            temp[j] = temp_words
        p = p + 1
    j = j + 1
print(temp)
res = []
o = 0
while o < len(temp):
    print(temp[o])
    if o < k:
        res.append(temp[o][0])
    o = o + 1
print(res)