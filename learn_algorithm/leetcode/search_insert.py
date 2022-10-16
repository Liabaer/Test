# -*- coding: utf-8 -*-
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 请必须使用时间复杂度为 O(log n) 的算法。
# nums = [1, 3, 5, 6]
# target = 5
#
# n = 0
# while n < len(nums):
#     if nums[n] == target:
#         print(n)
#         break
#     n = n + 1


nums = [1, 3, 5, 6]
left = 0
right = len(nums) - 1
# ans默认插入到最后一位
ans = 0
target = 5
# 左边和右边相遇了结束循环
while left <= right:
    # 找到中间下标
    mid = (right + left) // 2
    # 说明中间数字比目标大，由于num是有序的，所以答案在中间数字的左边，于是让right = mid - 1
    if nums[mid] > target:
        right = mid - 1
    elif nums[mid] < target:
        # 说明中间数字比目标小，由于num是有序的，所以答案在中间数字的右边，于是让left = mid + 1
        left = mid + 1
        # 当前mid位置的比目标元素要小，那么要插入的肯定是mid + 1的位置
        ans = mid + 1
    else:
        # 找到target 让ans = mid 结束循环不找了
        ans = mid
        break
print(ans)
