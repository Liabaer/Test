# -*- coding: utf-8 -*-
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。
nums = [2,7,11,15]
target = 9
# 我的笨方法
# class Solution:
#     def twoSum(nums,target):
#         i = 0
#         res = []
#         while i < len(nums):
#             j = i + 1
#             while j < len(nums):
#                 if i+1 < len(nums):
#                     if nums[i] + nums[j] == target:
#                         # print(i, j)
#                         res.append(i)
#                         res.append(j)
#                 j += 1
#             i += 1
#         return res


class Solution:
    def twoSum(self, nums, target):
        hashtable = {}
        # enumerate函数返回一个元祖，第一个是下标，第二个是值，（遍历nums，对于每个元素num和它的下标i）
        for i, num in enumerate(nums):
            # 如果target - num在hashtable中，说明已经找到了符合条件的两个元素，返回它们的下标
            if target - num in hashtable:
                # 返回符合条件的两个元素的下标
                return [hashtable[target - num], i]
            # 将num作为键，i作为值存入hashtable。
            hashtable[nums[i]] = i
        # 如果遍历完nums后仍未找到符合条件的元素，返回空列表[]。
        return []