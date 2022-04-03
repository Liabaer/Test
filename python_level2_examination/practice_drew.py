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
# import turtle
#
#
# def drawCircle():
#     turtle.pendown()
#     turtle.circle(20)
#     turtle.penup()
#     turtle.fd(40)
#
#
# def drawRowCircle(n):
#     # 倒序循环
#     for j in range(n, 1, -1):
#         for i in range(j):
#             drawCircle()
#         turtle.fd(-j * 40 - 20)
#         turtle.right(90)
#         turtle.fd(40)
#         turtle.left(90)
#         turtle.fd(40)
#     drawCircle()
#
#
# drawRowCircle(5)
# turtle.hideturtle()
# turtle.done()

# 第三题
# 请绘制六角菱形，如下图所示。参照编程模板，完善代码。
# import turtle
#
#
# def Draw():
#     turtle.begin_fill()
#     turtle.fd(100)
#     turtle.left(60)
#     turtle.fd(100)
#     turtle.left(120)
#     turtle.fd(100)
#     turtle.left(60)
#     turtle.fd(100)
#     turtle.end_fill()
#
# for i in range(3):
#     turtle.fillcolor("pink")
#     Draw()
# turtle.left(60)
# for i in range(3):
#     turtle.fillcolor("red")
#     Draw()
# turtle.hideturtle()
# turtle.done()
#
# # 第四题
# 参照代码模板完善代码，实现下述功能，不得修改其它代码，将代码保 存为py提交系统。使用turtle库的fd()、seth()、pencolor()函数绘制嵌套
# 五角形，五角形边长从1像素开始，第一条边从0度方向开始，边长按照 2个像素递增，每条边使用一种颜色，效果如下图所示
# # 特别注意：为了让平台自动评判，提交的代码应该是如模板代码所示， 把需要填空的内容，用printi语句输出出来
# import turtle as t
# colors = ["purple","red","blue","green","black"]
# d = 0
# k = 1
# edge = 5
#
# for j in range(10):
#     for i in range(len(colors)):
#         t.pencolor(colors[i])
#         t.fd(k)
#         d = d + 360/edge
#         t.seth(d)
#         k += 2
# t.done()
#
# 第五题
# 绘制三个菱形
# #
# import turtle
#
#
# def Draw():
#     turtle.fillcolor("red")
#     turtle.begin_fill()
#     turtle.forward(100)
#     turtle.left(60)
#     turtle.forward(100)
#     turtle.left(120)
#     turtle.forward(100)
#     turtle.left(60)
#     turtle.forward(100)
#     turtle.end_fill()
#
#
# for i in range(3):
#     Draw()
# turtle.hideturtle()
# turtle.done()


# 第六题
# 使用turtle库的fd()、seth()、pencolor()等函数绘制n个边长为40的彩色
# 正方形，第一个正方形左下角顶点在画布原点(0,0)处，后续K-1个正方
# 形沿着右上方45度角射线向外扩展布局，边长不变。n的值由用户输 入。当用户输入4的时候，效果如下图所示。
# 在_____处填写一行代码
# 不允许修改其他代码
# import turtle as t
#
#
# def oneSqure(x0, y0, length, color):
#     t.fillcolor(color)
#     t.begin_fill()
#     t.goto(x0, y0)
#     ang = 0
#     t.pendown()
#     for i in range(4):
#         t.fd(length)
#         ang += 90
#         t.seth(ang)
#     t.end_fill()
#     t.penup()
#     # t.write(name,font=('Arial', 10, 'normal'))
#
#
# length = 40
# x, y = 0, 0
# color = ['red', 'yellow', 'blue', 'green']
# # 题目卷面有问题 题目那个案例输入的是6
# n = eval(input("请输入个数"))
# for i in range(n):
#     # i % 4 表示循环利用color的颜色 这个要理解一下 颜色循环出现
#     oneSqure(x, y, length, color[i % 4])
#     x += length
#     y += length
#     这里是去到x,y的坐标
#     t.goto(x, y)
# t.done()

# 第七题
# 使用turtle库的turtle.circle()函数和turtle.seth()函数绘制图形，最 小的圆圈半径为20像素，不同圆圈之间的半径差是20像素。
# import turtle
#
# r = 20
# head = 90
# for i in range(3):
#     turtle.seth(head)
#     turtle.circle(r)
#     r = r + 20
#
# r = 20
# head = -90
# for i in range(3):
#     turtle.seth(head)
#     turtle.circle(r)
#     r = r + 20
#
# turtle.done()

# # 第八题-蝴蝶结
#
# import turtle as t
#
# t.pensize(6)
# t.fillcolor("red")
# t.goto(-100, -50)
# t.pendown()
# t.begin_fill()
# t.pencolor("black")
# t.goto(-100, 50)
# t.goto(100, -50)
# t.goto(100, 50)
# t.goto(-100, -50)
# t.penup()
# t.goto(-10, 0)
# t.pendown()
# t.right(90)
# t.circle(10)
# t.end_fill()
# t.hideturtle()
# t.done()


# 第九题
# 使用turtle库的turtle.circle()函数和turtle.seth()函数绘制套圈，最小的圆圈半径为10像素，不同圆圈之间的半径差是40像素。效果如下图 所示。
# 请在______处补充一行代码
import turtle

r = 10
head = 90
for i in range(4):
    # 先改变方向  turtle.seth(angle):只改变海龟的行进方向(角度按逆时针)，但不行进，angle为绝对度数
    turtle.seth(head)
    # 再画圆
    turtle.circle(r)
    r = r + 40
turtle.done()