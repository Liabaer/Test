# -*- coding: utf-8 -*-
# 给你一个混合字符串 s ，请你返回 s 中 第二大 的数字，如果不存在第二大的数字，请你返回 -1 。
# 混合字符串 由小写英文字母和数字组成。

def calc_max(ans):
    i = 0
    max = 0
    while i < len(ans):
        if max < ans[i]:
            max = ans[i]
        i = i + 1
    return max


s = "dfa12321afd"
i = 0
temp = []
res = 0
while i < len(s):
    if 48 <= ord(s[i]) <= 57:
        temp.append(int(s[i]))
    i = i + 1
# print(temp)
num_max = calc_max(temp)

# 注意循环里面不能使用remove，所以使用新数组来存储
temp_new = []
for i in temp:
    if i == num_max:
        continue
    else:
        temp_new.append(i)
print('移除后的', temp_new)

# 判断temp_new长度为0，则是没有第二大值的情况
if len(temp_new) == 0:
    res = -1
else:
    res = calc_max(temp_new)
print(num_max)
print(res)
