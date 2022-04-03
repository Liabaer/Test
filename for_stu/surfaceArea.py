# -*- coding: utf-8 -*-
# 给你一个 n * n 的网格grid ，上面放置着一些1 x 1 x 1的正方体。
# 每个值v = grid[i][j]表示v个正方体叠放在对应单元格(i, j)  上。
# 放置好正方体后，任何直接相邻的正方体都会互相粘在一起，形成一些不规则的三维形体。
# 请你返回最终这些形体的总表面积。
# 注意：每个形体的底面也需要计入表面积中。
grid =[[1,1,1],[1,0,1],[1,1,1]]
i = 0
sum = 0
while i < len(grid):
    j = 0
    k = 0
    while j < len(grid[i]):
        c = 2 + 4 * grid[i][j]
        # print grid[i][j]
        # [0,0]一个正方体时
        if grid[i][j] > 0:
            if i+1 < len(grid[i]):
                if grid[i][j] < grid[i+1][j]:
                    c = c - grid[i][j]
                else:
                    c = c - grid[i+1][j]
                # [0,1]
            if j+1 < len(grid[i]):
                if grid[i][j] < grid[i][j+1] :
                    c = c - grid[i][j]
                else:
                    c = c - grid[i][j+1]
            if i-1 >= 0:
                if grid[i][j] < grid[i-1][j]:
                    c = c - grid[i][j]
                else:
                    c = c - grid[i-1][j]
            if j-1 >= 0:
                if grid[i][j] < grid[i][j - 1]:
                    c = c - grid[i][j]
                else:
                    c = c - grid[i][j- 1]
        else:
            c = 0
        j = j + 1
        sum = sum + c
    i = i + 1
# print sum
