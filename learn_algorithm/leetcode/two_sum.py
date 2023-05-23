# -*- coding: utf-8 -*-
# 给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target的那两个整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。

nums = [3, 2, 3]
target = 6
# # 自己的俩循环的原始方法
# i = 0
# res = []
# while i < len(nums):
#     j = i + 1
#     while j < len(nums):
#         if i+1 < len(nums):
#             if nums[i] + nums[j] == target:
#                 print(i, j)
#                 res.append(i)
#                 res.append(j)
#         j += 1
#     i += 1
# print(res)


# 答案的标准示例
l = len(nums)
h = {}
# 使用enumerate函数遍历nums，enumreate返回一个元组，其中第一个元素是当前元素的索引，第二个元素是当前元素的值。这些元组分别被赋值给变量i和v
for i, v in enumerate(nums):
    # 这一行代码从哈希表h中获取一个键为target - v的值。
    # 如果哈希表中没有这个键，则返回None。这个操作相当于在列表中查找是否有一个数与当前数的和等于目标值。
    j = h.get(target - v, None)
    # 找到这样的两个数，打印出它们的索引
    if j is not None:
        print([i, j])
    # 当前数字v和它的索引i存储到哈希表h中
    h[v] = i