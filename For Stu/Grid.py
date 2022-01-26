# -*- coding: utf-8 -*-
# 给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。
#
# 请你统计并返回 grid 中 负数 的数目。
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
nums = 0
# for i in range(0, len(grid)):
#     for j in range(0, len(grid[i])):
#         if grid[i][j] < 0:
#             nums = nums + 1
# print nums
i = 0
while i < len(grid):
    j = 0
    while j < len(grid[i]):
        if grid[i][j] < 0:
            nums = nums + 1
        j = j + 1
    i = i + 1
print nums
