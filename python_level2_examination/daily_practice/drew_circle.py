# -*- coding: utf-8 -*-
#
import turtle as t
# 请不要修改其他代码
#

import random as r

color = ['red', 'orange', 'blue', 'green', 'purple']
r.seed(1)
for i in range(5):
    # .randint随机生成一定范围的值
    rad = r.randint(20, 50)
    x0 = r.randint(-100, 100)
    y0 = r.randint(-100, 100)
    # 从数组中随机取一个值 .choice
    t.color(r.choice(color))
    t.penup()
    t.goto(x0, y0)
    t.pendown()
    t.circle(rad)
t.done()
