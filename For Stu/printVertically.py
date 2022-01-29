# -*- coding: utf-8 -*-
# 给你一个字符串s。请你按照单词在 s 中的出现顺序将它们全部竖直返回。
# 单词应该以字符串列表的形式返回，必要时用空格补位，但输出尾部的空格需要删除（不允许尾随空格）。
# 每个单词只能放在一列上，每一列中也只能有一个单词。
s = "TO BE OR NOT TO BE"
i = 0
s_new_array = []
m = 0
s_new = ''
num_l = 0
while m < len(s):
    if s[m] != ' ':
        s_new = s_new + s[m]
    else:
        s_new_array.append(s_new)
        s_new = ''
        m = m + 1
        continue
    if num_l < len(s_new):
        num_l = len(s_new)
    m = m + 1
if s_new != ' ':
    s_new_array.append(s_new)
num_h = len(s_new_array)
print(s_new_array)
print(num_l)
print(num_h)

ans_array = []
while i < num_l:
    # print(s_new_array[i])
    j = 0
    ans = ''
    space = ''
    while j < num_h:
        # ans = ans + s_new_array[j][i]
        # 这里使用space存每一个需要加空格的字符
        if i >= len(s_new_array[j]):
            space = space + ' '
        else:
            # 遇到字母的时候再加到ans，并把space初始化
            ans = ans + space
            space = ''
            print(i, j, s_new_array[j])
            ans = ans + s_new_array[j][i]
        j = j + 1
    ans_array.append(ans)
    i = i + 1
print(ans_array)


# ["TBONTB","OEROOE","   T"]
# h a a
# h a
# h
