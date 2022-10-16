# -*- coding: utf-8 -*-
#
# import turtle
# import random
# from turtle import *
# from time import sleep
#
#
# def tree(branchLen, t):
#     if branchLen > 3:
#         if 8 <= branchLen <= 12:
#             if random.randint(0, 2) == 0:
#                 t.color('snow')
#             else:
#                 t.color('lightcoral')
#             t.pensize(branchLen / 3)
#         elif branchLen < 8:
#             if random.randint(0, 1) == 0:
#                 t.color('snow')
#             else:
#                 # 淡珊瑚色
#                 t.color('lightcoral')
#             t.pensize(branchLen / 2)
#         else:
#             # 赭(zhě)色
#             t.color('sienna')
#             t.pensize(branchLen / 10)
#
#         t.forward(branchLen)
#         a = 1.5 * random.random()
#         t.right(20 * a)
#         b = 1.5 * random.random()
#         tree(branchLen - 10 * b, t)
#         t.left(40 * a)
#         tree(branchLen-10 * b, t)
#         t.right(20 * a)
#         t.up()
#         t.backward(branchLen)
#         t.down()
#
#
# def petal(m, t):  # 树下花瓣
#     for i in range(m):
#         a = 200 - 400 * random.random()
#         b = 30 - 40 * random.random()
#         t.up()
#         t.forward(b)
#         t.left(90)
#         t.forward(a)
#         t.down()
#         # 淡珊瑚色
#         t.color("lightcoral")
#         t.circle(1)
#         t.up()
#         t.backward(a)
#         t.right(90)
#         t.backward(b)
#
#
# def main():
#     t = turtle.Turtle()
#     w = turtle.Screen()
#     t.hideturtle() # 隐藏画笔
#     t.getscreen().tracer(5, 0)
#     w.screensize(bg='wheat') # wheat小麦
#     t.left(90)
#     t.up()
#     t.backward(150)
#     t.down()
#     t.color('sienna')
#     # 画樱花的躯干
#     tree(62, t)
#     # 掉落的花瓣
#     petal(255, t)
#     w.exitonclick()
#
# main()


from turtle import *
from random import *
from math import *


def tree(n, l):
    pd()  # 下笔
    # 阴影效果
    t = cos(radians(heading() + 45)) / 8 + 0.25
    pencolor(t, t, t)
    pensize(n / 3)
    forward(l)  # 画树枝

    if n > 0:
        b = random() * 15 + 10  # 右分支偏转角度
        c = random() * 15 + 10  # 左分支偏转角度
        d = l * (random() * 0.25 + 0.7)  # 下一个分支的长度
        # 右转一定角度，画右分支
        right(b)
        tree(n - 1, d)
        # 左转一定角度，画左分支
        left(b + c)
        tree(n - 1, d)

        # 转回来
        right(c)
    else:
        # 画叶子
        right(90)
        n = cos(radians(heading() - 45)) / 4 + 0.5
        pencolor(n, n * 0.8, n * 0.8)
        circle(3)
        left(90)

        # 添加0.3倍的飘落叶子
        if (random() > 0.7):
            pu()
            # 飘落
            t = heading()
            an = -40 + random() * 40
            setheading(an)
            dis = int(800 * random() * 0.5 + 400 * random() * 0.3 + 200 * random() * 0.2)
            forward(dis)
            setheading(t)

            # 画叶子
            pd()
            right(90)
            n = cos(radians(heading() - 45)) / 4 + 0.5
            pencolor(n * 0.5 + 0.5, 0.4 + n * 0.4, 0.4 + n * 0.4)
            circle(2)
            left(90)
            pu()

            # 返回
            t = heading()
            setheading(an)
            backward(dis)
            setheading(t)

    pu()
    backward(l)  # 退回


bgcolor(0.5, 0.5, 0.5)  # 背景色
ht()  # 隐藏turtle
speed(0)  # 速度，1-10渐进，0最快
tracer(0, 0)
pu()  # 抬笔
backward(100)
left(90)  # 左转90度
pu()  # 抬笔
backward(300)  # 后退300
tree(12, 100)  # 递归7层
done()
