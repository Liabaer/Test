# -*- coding: utf-8 -*-
# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
nums = [-4,-1,0,3,10]
new_nums = []
for i in range(0, len(nums)):
    new_nums.append(nums[i] * nums[i])
new_nums.sort()
print new_nums