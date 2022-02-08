# -*- coding: utf-8 -*-
# 字符串S和 T 只包含小写字符。在S中，所有字符只会出现一次。
#
# S 已经根据某种规则进行了排序。我们要根据S中的字符顺序对T进行排序。更具体地说，如果S中x在y之前出现，那么返回的字符串中x也应出现在y之前。
#
# 返回任意一种符合条件的字符串T。
order = "kqep"
s = "pekeq"
new_s = ''
new_b = ''

dict_s = {}

m = 0
while m <len(s):
    if s[m] not in dict_s:
        dict_s[s[m]] = 1
    else:
        dict_s[s[m]] = dict_s[s[m]] + 1
    m = m + 1
print(dict_s)
i = 0
while i < len(order):
    if order[i] in s:
        new_s = new_s + order[i]*dict_s[order[i]]
    i = i + 1

# 双循环，空间复杂度高，O(N*N)
# while i < len(order):
#     z = 0
#     # 循环
#     while z < len(s):
#         if order[i] == s[z]:
#             new_s = new_s + order[i]
#         z = z + 1
#     i = i + 1
j = 0
while j < len(s):
    if s[j] not in order:
        new_b = new_b + s[j]
    j = j + 1

# print(new_s, new_b)
res = new_s + new_b
print(res)

