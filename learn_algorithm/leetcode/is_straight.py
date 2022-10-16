# -*- coding: utf-8 -*-
# 从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
# 2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

A = 1
J = 11
Q = 12
K = 13
i = 0
j = 0
k = 0
nums = [11, 0, 9, 0, 0]
for a in range(0, len(nums)):
    if nums[a] == 'A':
        nums[a] = A
    elif nums[a] == 'J':
        nums[a] = j
    elif nums[a] == 'Q':
        nums[a] = Q
    elif nums[a] == 'K':
        nums[a] = K
nums.sort()
is_straight = False

while i < len(nums) - 1:
    if nums[i] == 0:
        j = j + 1
        i = i + 1
        continue
    elif nums[i + 1] - nums[i] == 1:
        i = i + 1
        continue
    elif nums[i + 1] - nums[i] > 1:
        k = k + nums[i + 1] - nums[i] - 1
        i = i + 1
        continue
    elif nums[i + 1] == nums[i]:
        break
print(k, j)
if k <= j:
    is_straight = True
    print(is_straight)
else:
    print(is_straight)
