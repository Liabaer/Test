# -*- coding: utf-8 -*-
# 给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。
# 如果存在一个整数 x 使n == 2x ，则认为 n 是 2 的幂次方。
n = 0
flag = True
if n == 0:
    flag = False
else:
    while n != 1:
        if n % 2 != 0:
            flag = False
            break
        else:
            n = n / 2
print
flag
