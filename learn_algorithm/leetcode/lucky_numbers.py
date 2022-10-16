# -*- coding: utf-8 -*-
# 给你一个 m * n 的矩阵，矩阵中的数字 各不相同 。请你按 任意 顺序返回矩阵中的所有幸运数。
# 幸运数是指矩阵中满足同时下列两个条件的元素：
# 在同一行的所有元素中最小
# 在同一列的所有元素中最大

# for i in matrix:
#     print i
#     num = 100000
#     for j in range(0, len(i)):
#         # print i[j]
#         if num > i[j]:
#             num = i[j]
#     print num
matrix = [[7, 8], [1, 2]]
m = 0
small = 0
nums = []
while m < len(matrix):
    Flag = True
    n = 0
    num = 100000
    while n < len(matrix[m]):
        if num > matrix[m][n]:
            num = matrix[m][n]
            small = n
        n = n + 1
    # print num, small
    l = 0
    while l < len(matrix):
        # print matrix[l][small]
        if num >= matrix[l][small]:
            l = l + 1
            continue
        else:
            Flag = False
            break
    if Flag == True:
        nums.append(num)
    else:
        print - 1
    m = m + 1
print
nums
