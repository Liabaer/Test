# -*- coding: utf-8 -*-
# 使用 turtle库绘制三个彩色的园,园的颜色按顺序从颜色列表 color中获 取,圆的园心位于(0.0)坐标处,半径从里至外分别是10像素,30像素, 60像素。

# import turtle 是导入所有turtle  from turtle import * 也是导入所有的模块，但是不需要turtle.来调用方法
from turtle import *

color = ['red', 'green', 'blue']
rs = [10, 30, 60]
for i in range(0, len(rs)):
    penup()
    # 圆心的位置要注意
    goto(0, -rs[i])
    pendown()
    pencolor(color[i])
    circle(rs[i], 360)
done()