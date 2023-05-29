# -*- coding: utf-8 -*-
# 给你一个 升序排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
# 元素的相对顺序应该保持 一致 。然后返回 nums 中唯一元素的个数。
# 考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：
# 更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
# 返回 k
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

if not nums:
    print(0)
i = 0
# 快慢指针的方法，俩个下标，i和j，分别指向nums的第一个元素和后一位元素
for j in range(1, len(nums)):
    # 判断nums[i]和nums[j]是否相等，如果不相等则更新i，并且让num[i]的值等于num[j]的值，再次判断重新赋值nums[i]和nums[j]是否相等
    if nums[i] != nums[j]:
        i += 1
        nums[i] = nums[j]
# 循环结束后，num[i]就是最后一个不想等的元素，这是返回下标i+1就是lenth啦
print(i+1)

# def removeDuplicates(nums):
#     if not nums:
#         return 0
#     i = 0
#     for j in range(1, len(nums)):
#         if nums[i] != nums[j]:
#             i += 1
#             nums[i] = nums[j]
#     return i + 1
#
#
# print(removeDuplicates(nums))


# 这个方法，我感觉没问题啊，不知道为啥，leetcode就是不通过，我麻了，我不理解
# num_dict={}
# for i in nums:
#     if i in num_dict:
#         num_dict[i] += 1
#     else:
#         num_dict[i] = 1
# new_num = []
# for i, v in num_dict.items():
#     new_num.append(i)
# print(len(new_num),new_num)