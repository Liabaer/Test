# -*- coding: utf-8 -*-
# 例如， 罗马数字 2 写做II，即为两个并列的 1。12 写做XII，即为X+II。 27 写做XXVII, 即为XX+V+II。
#
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做IIII，而是IV。数字 1 在数字 5 的左边，
# 所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为IX。这个特殊的规则只适用于以下六种情况：
#
# I可以放在V(5) 和X(10) 的左边，来表示 4 和 9。
# X可以放在L(50) 和C(100) 的左边，来表示 40 和90。
# C可以放在D(500) 和M(1000) 的左边，来表示400 和900。
# 给你一个整数，将其转为罗马数字。

# 双循环解法
# 注意题目中的特殊情况加到数组和字典中中直接判断
roman_dict = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC',100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
roman_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
num = 1994
res = ''
temp = ''

for i in roman_list:
    # 如果在字典里面，直接让结果等于字典的values，（下面while加上=就不需要这个if了）
    # if num in roman_dict:
    #     res = roman_dict[num]
    # 如果num比字典中的数值大，就让temp先等于比较的，再让num-i
    while num >= i:
        print(num)
        print(temp)
        res = res + roman_dict[i]
        num = num - i
# res = temp
print(res)

# 解法二，一个循环解决
# roman_list = [1000, 900, 500, 400, 100, 90, 50, 40,10, 9, 5, 4, 1]
# roman_dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
# i = 0
# while num > 0:
#     if num >= roman_list[i]:
#         num = num - roman_list[i]
#         temp = temp + roman_dict[roman_list[i]]
#     else:
#         i = i + 1
# print(temp)
