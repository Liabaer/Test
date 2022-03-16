# -*- coding: utf-8 -*-
# 请编写代码替换橫銭,不修改其他代码,实现下面功能,让用户输入一个自
# 然数n。
# 如果n为奇数输出表达式1+1/3+1/5+.…+1/n的值。
# 如果n为偶数,输出表达式1/2+1/4+1/6+.+1/n的值。
# 输出结果保留两位小数。
# 在___补充一行代码
n = 4
def func(n):
    s = 0
    if n%2 != 0:
        for i in range(1, n + 1, 2):
            # 注意审题啊：s = 0 + 1 / 1 + 1/ 3 + 1/5
            s = s + 1/i
    else:
        for i in range(2, n + 1, 2):
            s = s + 1/i
    return s

number = int(input())


print(func(number))