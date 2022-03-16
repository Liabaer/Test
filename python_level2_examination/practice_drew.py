# -*- coding: utf-8 -*-
# 第一题
# 请编写代码替换横线，不修改其他代码，实现以下功能：
# 使用turtle.库函数绘制4个等距排列的正方形，边长为40像素，间距宽度为40。最左 边的正方形左上角坐标为(0,0)。
# 效果如下图所示。

# 在...上补充一行或者多行代码
# 在——————上补充一行代码


# import turtle
# n = 4
# # j和i只是循环工具，无实际意义
# for j in range(n):
#     # penup和pendown对应
#     turtle.pendown()
#     # 正方形
#     for i in range(4):
#         turtle.forward(40)
#         turtle.right(90)
#     turtle.penup()
#     # 要间距40，所以要加上边长再加边距
#     turtle.fd(80)
# turtle.done()
#
#
# 第二题
# 使用turtle库绘制下面的5行圆圈图案，第一行5个圆圈，向下逐行递减，第5行1 个圆圈。圆圈居中排列，半径为20像素。
import turtle


def drawCircle():
    turtle.pendown()
    turtle.circle(20)
    turtle.penup()
    turtle.fd(40)


def drawRowCircle(n):
    # 倒序循环
    for j in range(n, 1, -1):
        for i in range(j):
            drawCircle()
        turtle.fd(-j * 40 - 20)
        turtle.right(90)
        turtle.fd(40)
        turtle.left(90)
        turtle.fd(40)
    drawCircle()


drawRowCircle(5)
turtle.hideturtle()
turtle.done()