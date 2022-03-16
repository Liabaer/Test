# -*- coding: utf-8 -*-
# 绘制边长为100的正五边形
import turtle as t
t.pensize(2)
d = 0
# 【0，n）从1开始，所以要到6为止，不是5哦
for i in range(1, 6):
    t.fd(100)
    # 以线右边的度数为准画线
    d += 72
    t.seth(d)
t.done()
