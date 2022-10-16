# -*- coding: utf-8 -*-
# 给你一个整数数组 nums，请你返回其中位数为 偶数 的数字的个数。
nums = [555, 901, 482, 1771]
i = len(nums) - 1
print(i)
j = 0
while i >= 0:
    a = str(nums[i])
    # print(a)
    if len(a) % 2 == 0:
        j = j + 1
        a = ''
    i = i - 1
print(j)
