# -*- coding: utf-8 -*-
# 给你一个整数数组 nums 。数组中唯一元素是那些只出现 恰好一次 的元素。
# 请你返回 nums 中唯一元素的 和 。

nums = [1,2,3,2]
# new_nums = []
# count = 0
# i = 0
# while i < len(nums):
#     if nums[i] not in new_nums:
#         new_nums.append(nums[i])
#         print(new_nums)
#     else:
#         new_nums.remove(nums[i])
#     i = i + 1
# print(new_nums)
#
# j = 0
# while j < len(new_nums):
#     count = count + new_nums[j]
#     j = j + 1
# print(count)

new_nums = {}
count = 0

i = 0

while i < len(nums):
    if nums[i] not in new_nums:
        new_nums[nums[i]] = 1
    else:
        new_nums[nums[i]] = new_nums[nums[i]] + 1
    i = i + 1
print(new_nums)

for m, n in new_nums.items():
    # print(m, n)
    if n == 1:
        count = count + m
print(count)