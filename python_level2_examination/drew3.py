# -*- coding: utf-8 -*-
# 绘制一个边长为 200 的正方形, 正方形的边长为紫色，内部填充为黑色

import turtle

d = 90
turtle.color('black')
turtle.pencolor('purple')
turtle.begin_fill()
# 要从90开始，本来已经向前200了，0的话还是同一个方向
for i in range(90, 360, 90):
    turtle.forward(200)
    turtle.setheading(i)
turtle.end_fill()
turtle.done()
