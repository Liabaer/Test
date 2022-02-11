# -*- coding: utf-8 -*-
# 给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。
# 如果不能形成任何面积不为零的三角形，返回 0。


nums = [3,2,3,4]

nums.sort()
new_nums = []
j = len(nums)-1
while j >= 0:
    new_nums.append(nums[j])
    j = j - 1

i = 0
C = 0
while i < len(new_nums)-2:
    if new_nums[i] < new_nums[i+1] + new_nums[i+2]:
        C = new_nums[i] + new_nums[i+1] + new_nums[i+2]
        break
    i = i + 1
print(C)