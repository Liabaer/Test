# -*- coding: utf-8 -*-
x = 121

y = str(x)
i = 0
a = True
for z in reversed(y):
    if z != y[i]:
        a = False  # 只要出现一次就不是回文数
        break
    i = i+1
print a




