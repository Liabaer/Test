# -*- coding: utf-8 -*-
# 给定两个数组，编写一个函数来计算它们的交集。

nums1 = [1,2,2,1]
nums2 = [1,2]

new_num = []

i = 0
while i < len(nums1):
    if nums1[i] in nums2:
        if nums1[i] not in new_num:
            new_num.append(nums1[i])
    i = i + 1
print(new_num)

# j = 0
# nums = []
#
# while j < len(new_num):
#     k = 0
#     flag = True
#     while k < len(new_num):
#         if new_num[j] == new_num[k] and j != k:
#             flag = False
#             break
#         k = k + 1
#     if flag == True:
#         nums.append(new_num[j])
#     j = j + 1
# print(nums)
# print(new_num)