# -*- coding: utf-8 -*-
# 给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
# 你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。

nums = [2,2,1]
# 超出时间限制了，没有使用线性时间复杂度的算法解决
# i = 0
# flag = False
# while i < len(nums):
#     j = 0
#     while j < len(nums):
#         if nums[i] == nums[j] and i != j:
#             flag = True
#             j += 1
#             break
#         else:
#             flag = False
#         j += 1
#     if not flag:
#         print(nums[i])
#         break
#     i += 1
#     if i == len(nums) - 1 and flag:
#         print(nums[i])

# 异或方法：如果a、b两个值不相同，则异或结果为1。如果a、b两个值相同，异或结果为0。
for i in range(1, len(nums)):
    nums[0] ^= nums[i]
print(nums[0])

# 二、异或运算的性质
# 交换律：A ^ B = B ^ A;
# 结合律：A ^ (B ^ C) = (A ^ B) ^ C;
# 恒等律：X ^ 0 = X;
# 归零律：X ^ X = 0;
# 自反：A ^ B ^ B = A ^ 0 = A;
# 对于任意的 X： X ^ (-1) = ~X；
# 如果 A ^ B = C 成立，那么 A ^ B = C，B ^ C = A；

