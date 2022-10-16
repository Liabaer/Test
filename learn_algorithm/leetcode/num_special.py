# -*- coding: utf-8 -*-

# 给你一个大小为 rows x cols 的矩阵 mat，其中 mat[i][j] 是 0 或 1，请返回 矩阵  mat 中特殊位置的数目 。
# 特殊位置 定义：如果 mat[i][j] == 1 并且第 i 行和第 j 列中的所有其他元素均为 0（行和列的下标均 从 0 开始 ），则位置 (i, j) 被称为特殊位置。

mat = [[1, 0, 0],
       [0, 1, 0],
       [0, 0, 1]]
i = 0
num = 0

while i < len(mat):
    j = 0
    while j < len(mat[i]):
        if mat[i][j] == 0:
            j = j + 1
            continue
        else:
            x = 0
            y = 0
            flag = True
            while x < len(mat[i]):
                if x != j:
                    if mat[i][x] == 1:
                        flag = False
                        break
                x = x + 1
            if not flag:
                break
            while y < len(mat):
                if y != i:
                    if mat[y][j] == 1:
                        flag = False
                        break
                y = y + 1
            if not flag:
                break
            if flag:
                num = num + 1
        j = j + 1
    i = i + 1
print(num)
