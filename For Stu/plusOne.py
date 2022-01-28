# -*- coding: utf-8 -*-
# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
def add_list(flag, digits, i, temp):
    if digits[i] + 1 < 10:
        temp.append(digits[i] + 1)
        flag = False
    if digits[i] + 1 == 10:
        flag = True
        temp.append(0)
    return flag, temp

digits = [9, 8, 9]

flag = False
temp = []
i = len(digits)-1
while i >= 0:
    print(digits[i])
    if i == len(digits) - 1:
        flag, temp = add_list(flag, digits, i, temp)
    else:
        if flag == True:
            flag, temp = add_list(flag, digits, i, temp)
        else:
            temp.append(digits[i])
    i = i - 1
print(temp)
res = []
j = len(temp)-1
while j >= 0:
    if temp[j] == 0 and j == len(temp)-1:
        res.append(1)
        res.append(temp[j])
    else:
        res.append(temp[j])
    j = j - 1
print(res)

