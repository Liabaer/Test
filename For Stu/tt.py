# -*- coding: utf-8 -*-

nums = [3,2,4]
target = 6
for i in range(0, len(nums)):
    for j in range(0, len(nums)):
        if nums[i] + nums[j] == target and i != j:
            print [i, j]