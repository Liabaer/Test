# -*- coding: utf-8 -*-
# 所有 DNA 都由一系列缩写为 'A'，'C'，'G' 和 'T' 的核苷酸组成，例如："ACGAATTCCG"。
# 在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。
#
# 编写一个函数来找出所有目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
num = []
dic = {}
i = 0
while i < len(s):
    j = i
    a = ''
    while j < len(s):
        a = a + s[j]
        if len(a) == 10:
            num.append(a)
            a = ''
            break
        # print(a)
        j = j + 1
    i = i + 1
print(num)

m = 0
while m < len(num):
    if num[m] not in dic:
        dic[num[m]] = 1
    else:
        dic[num[m]] = dic[num[m]] + 1
    m = m + 1
print(dic)

new_num = []
for k, v in dic.items():
    if v >= 2:
        new_num.append(k)
print(new_num)
