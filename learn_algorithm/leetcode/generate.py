# -*- coding: utf-8 -*-
# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
numRows = 5
i = 0
m = []
while i < numRows:
    # print(str(i)+'---')
    j = 0
    n = []
    m.append(n)
    print(m)
    while j <= i:
        k = 0
        print(i, j, len(m[i - 1]))
        if i == 0 and j == 0:
            n.append(1)
        elif i - 1 >= 0 and j - 1 >= 0 and j < len(m[i - 1]):
            k = m[i - 1][j - 1] + m[i - 1][j]
            n.append(k)
        elif i - 1 >= 0 and j - 1 >= 0:
            k = k + m[i - 1][j - 1]
            n.append(k)
        elif i - 1 >= 0:
            k = k + m[i - 1][j]
            n.append(k)
        j = j + 1
    i = i + 1
print(m)
