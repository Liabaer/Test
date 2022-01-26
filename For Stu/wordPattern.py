# -*- coding: utf-8 -*-
# 给定一种规律 pattern和一个字符串str，判断 str 是否遵循相同的规律。
#
# 这里的遵循指完全匹配，例如，pattern里的每个字母和字符串str中的每个非空单词之间存在着双向连接的对应规律。
pattern = "abba"
s = " dog cat cat dog"
j = 1
k = 1
s_a = []
temp = ''
l = 0
# 将s截取成单词用数组存s_a储 注意temp的初始化是''中间没有空格，而判断s[l]的为空格的时候，要注意' '中间有空格
while l < len(s):
    if l == 0 and s[l] == ' ':
        l = l + 1
        continue
    if s[l] != ' ':
        temp = temp + s[l]
    if s[l] == ' ':
        s_a.append(temp)
        temp = ''
        l = l + 1
        continue
    if l == len(s) - 1 and s[l] != ' ':
        s_a.append(temp)
        temp = ''
        l = l + 1
        continue
    l = l + 1
print s_a
# 遍历s_a计算单词第几次出现 存到字典sa中
sa = {}
o = 0
p = 1
while o < len(s_a):
    if s_a[o] not in sa:
        sa[s_a[o]] = p
        p = p + 1
    o = o + 1
print sa
# 遍历s，用字典中出现的次数value替换值，用新字符串a_new存
s_new = ''
n = 0
while n < len(s_a):
    if s_a[n] in sa:
        s_new = s_new + str(sa[s_a[n]])
    n = n + 1
print s_new
# 遍历patten 第几次出现存在字典pa里
i = 0
pa = {}
while i < len(pattern):
    if pattern[i] not in pa:
        pa[pattern[i]] = j
        j = j + 1
    i = i + 1
print pa
pattern_new = ''
m = 0
# 遍历patten 用字典中出现的字符串做对比，将pattern以数字形式记录并用新的字符串pattern_new存
while m < len(pattern):
    if pattern[m] in pa:
        pattern_new = pattern_new + str(pa[pattern[m]])
    m = m + 1
print pattern_new
# 对比俩个字符串最终的
if pattern_new == s_new:
    print True
else:
    print False
