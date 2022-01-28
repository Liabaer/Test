# -*- coding: utf-8 -*-
# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
# num = 5
# nums = []
#
# j = 0
# k = 0
# while num >=0:
#     nums.append(num)
#     num = num - 1
#     if num == -1:
#         break
# print(nums)
#
# i = len(nums) -1
# while i >= 0:
#     while nums[i] <= num:
#         j = nums[i] % 2
#         nums[i] = nums[i] / 2
#         if j == 1:
#             k = k + 1
#
#  i = i - 1
from datetime import datetime

# date = datetime.strptime('2021.08.18 16:16:37', '%Y.%m.%d')
a = '2021.08.19 13:14:51'
print(a[0:10])
# print( date)