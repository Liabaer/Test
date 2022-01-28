# -*- coding: utf-8 -*-
# 给定一个二进制数组， 计算其中最大连续 1 的个数。
nums = [1, 1, 0, 1, 1, 1, 0]
i = 0
j = 0
k = 0
flag = False
while i <= len(nums)-1:
    if nums[i] != 0:
        j = j + 1
    else:
        if k < j:
            k = j
        j = 0
    i = i + 1
if k < j:
    k = j
print(k)