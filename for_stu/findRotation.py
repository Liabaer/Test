# -*- coding: utf-8 -*-
# 给你两个大小为 n x n 的二进制矩阵 mat 和 target 。
# 现 以 90 度顺时针轮转 矩阵 mat 中的元素 若干次 ，
# 如果能够使 mat 与target 一致，返回 true ；否则，返回 false 。
mat = [[0,0,0],[0,1,0],[1,1,1]]
target = [[1,1,1],[0,1,0],[0,0,0]]

m = 0
while m < 4:
    z = 0
    new_mat = []
    while z < len(mat):
        y = 0
        b = []
        while y < len(mat[0]):
            b.append(0)
            y += 1
        z += 1
        new_mat.append(b)
    i = 0
    while i < len(mat):
        j = 0
        while j < len(mat[i]):
            if len(mat)-i-1 >= 0:
                new_mat[j][len(mat)-i-1] = mat[i][j]
            j = j + 1
        i = i + 1
    flag = True
    mat = new_mat
    # print new_mat
    i = 0
    while i < len(new_mat):
        # print i,j
        j = 0
        while j < len(new_mat[i]):
            if new_mat[i][j] != target[i][j]:
                flag = False
                break
            j = j + 1
        i = i + 1
        if not flag:
            break
    if flag == True:
        break
    else:
        m = m + 1
print(flag)


