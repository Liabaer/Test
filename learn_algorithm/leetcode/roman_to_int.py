# -*- coding: utf-8 -*-
# 罗马数字包含以下七种字符：I,V,X,L,C,D和M。
# 例如，罗马数字2写做I工，即为两个并列的1.12写做XI工，即为X+II。27写做XXVII,即为XX+V+II。
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如4不写做IIII,而是IV。数字1在数字5的左边，所
# 表示的数等于大数5减小数1得到的数值4。同样地，数字9表示为1x。这个特殊的规则只适用于以下六种情况
# I  可以放在V(5) 和  X  (10) 的左边，来表示 4 和 9。
# X  可以放在L(50) 和  C  (100) 的左边，来表示 40 和  90。
# C  可以放在D(500) 和  M  (1000) 的左边，来表示  400 和  900
s = "III"
roman_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
roman_dict = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9,
              'V': 5, 'IV': 4, 'I': 1}
i = 0
num = 0
temp = ''
while s != temp:
    if s[i] in roman_dict:
        num = num + roman_dict[s[i]]
        temp = temp + s[i]
    else:
        temp = temp + s[i]
        i = i + 1
print(num)
