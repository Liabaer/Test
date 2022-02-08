# -*- coding: utf-8 -*-
order = "kqep"
s = "pekeq"
dict_order = {}  # 记录每个字母的真实大小 key表示当前字母 value表示当前字母的大小
i = 0
while i < len(order):
    dict_order[order[i]] = i
    i = i + 1
s_list = []
i = 0  # 上面的i不用了 重新利用i
# 把字符串拆分成字符串数组用于冒泡排序
while i < len(s):
    s_list.append(s[i])
    i = i + 1
i = 0
while i < len(s_list):
    j = i + 1
    while j < len(s_list):
        # 如果2个都在order里出现过就比较他们字典里的大小
        if s_list[i] in dict_order and s_list[j] in dict_order:
            if dict_order[s_list[i]] > dict_order[s_list[j]]:
                temp = s_list[i]
                s_list[i] = s_list[j]
                s_list[j] = temp
        elif s_list[i] in dict_order and s_list[j] not in dict_order:
            # s_list[i]在order里，s_list[j]不在字典里 不交换
            j = j + 1
            continue
        elif s_list[i] not in dict_order and s_list[j] in dict_order:
            # s_list[i] 不在order里， s_list[j] 在字典里 交换
            temp = s_list[i]
            s_list[i] = s_list[j]
            s_list[j] = temp
        else:
            # 都不在字典里 不交换
            j = j + 1
            continue
        j = j + 1
    i = i + 1
res = ''
i = 0
while i < len(s_list):
    res = res + s_list[i]
    i = i + 1
print(res)