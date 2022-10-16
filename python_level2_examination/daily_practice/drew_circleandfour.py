# -*- coding: utf-8 -*-
# 使用 turtle.库的 turtle.fd()函数和 turtle.left()函数绘制一个边 长为200像素的正方形及一个紧挨四个顶点的圆形,写入 替换模板中的横线,不得修改其他代码
import turtle

turtle.pensize(2)
for i in range(0, 4):
    turtle.fd(200)
    turtle.left(90)
# 注意箭头开始画的方向
turtle.left(-45)
# pow(2, 0.5)表示根号2  pow(x,y)表示x的y次方
turtle.circle(100 * pow(2, 0.5))
turtle.done()
