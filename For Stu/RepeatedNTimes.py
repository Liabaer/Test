# -*- coding: utf-8 -*-
nums = [2,1,2,5,3,2]
# nums.sort()
# n = len(nums)/2-1
# i = 0
# j = 0
# while i < len(nums) -1:
#     if nums[i] == nums[i+1]:
#         j = j + 1
#         if j >= n:
#             break
#     i = i + 1
# print(nums[i])
dict_nums = {}
for i in range(0, len(nums)):
    if nums[i] not in dict_nums:
        dict_nums[nums[i]] = 1
    else:
        dict_nums[nums[i]] = dict_nums[nums[i]] + 1
print(dict_nums)
for k, v in dict_nums.items():
    if v >= len(nums)/2:
        break
print(k)


