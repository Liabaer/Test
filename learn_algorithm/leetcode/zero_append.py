# -*- coding: utf-8 -*-

# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
nums = [0, 1, 0, 3, 12]
a = 0

for i in range(0, len(nums)):
    if nums[i] != 0:
        nums[a] = nums[i]
        a = a + 1
print(nums)
while a < len(nums):
    nums[a] = 0
    a = a + 1
print(nums)

# 这是个简单方法
# nums = []
# for b in a:
#     if b == 0:
#         nums.append(b)
#         a.remove(b)
# nums = a + nums
# print(num)
