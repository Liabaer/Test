# -*- coding: utf-8 -*-
import turtle
# 起点为0，0
# 设置颜色
turtle.color('red')
# 前进
turtle.forward(100)

# 右转旋转（度数）
turtle.right(90)
turtle.forward(100)

# # 左转旋转（度数）
turtle.left(90)
turtle.forward(100)

# # 前往坐标x,y
turtle.goto(0, 0)
# turtle.forward(100)

# # 设置x,y坐标
turtle.setx(200)
# turtle.sety(300)

# # 标准模式
# # 0-东  90 北  180 西  270 南
turtle.setheading(0)
turtle.forward(100)

# # 返回原点
turtle.home()

# # 绘制圆形
# # 第一个参数是半径 ,第二个参数是绘制多少圆周(180是半圆、360是整个圆)， 第三个参数, 绘制正多边形(数字是边的数量)，都是选填
turtle.circle(50, 360, 4)

# # 绘制一个点，第一个参数多大，第二个参数颜色
turtle.dot(10, 'purple')

# # 撤销上一次操作
turtle.undo()

# # 设置绘制速度0-10 最快10
# turtle.speed(5)
#
# # 获得当前的坐标
# print(turtle.position())
# # 获取目标坐标的方向
# print(turtle.towards(30, 40))
# # 获得当前坐标
# print(round(turtle.xcor(), 5), round(turtle.ycor(), 5))
# # 获得朝向
# print(turtle.heading())
# # 获得当前坐标距离坐标的距离
# print(turtle.distance(30, 40))
# # 设置角度和弧度
# # turtle.degrees()
# # turtle.radians()
#
# # 画笔控制
# # 画笔落下
turtle.pendown()

# # 画笔提起
turtle.penup()

# # 画笔粗细
turtle.pensize(10)
# 保存当前画图
turtle.done()
# # 画笔是否落下

# # 颜色
# turtle.color('red')
# # 画笔颜色
# turtle.pencolor('red')
# # 填充颜色
# turtle.fillcolor('red')
# # 是否填充
# turtle.filling()
# # 开始填充 结束填充
# turtle.begin_fill()
# turtle.end_fill()
# # 重置
# turtle.reset()
# # 清空
# turtle.clear()
# print(turtle.isdown())
# # 画完
