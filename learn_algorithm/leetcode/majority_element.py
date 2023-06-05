# -*- coding: utf-8 -*-
# 给定一个大小为 n 的数组nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 n/2 的元素。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。

nums = [2,2,1,1,1,2,2]
nums_dict = {}
for i in nums:
    if i in nums_dict:
        nums_dict[i] += 1
    else:
        nums_dict[i] = 1
for i in nums_dict:
    if nums_dict[i] > len(nums)/2:
        print(i)