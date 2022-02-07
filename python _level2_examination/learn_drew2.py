# -*- coding: utf-8 -*-
# 在____________上补充代码
# 请不要修改其他代码
# 绘制四朵小雪花中心点由points给出，半径由randint给出，雪花颜色是红色
import turtle as t
import random as r

# 对于random.seed(n)，如果使用相同的n值，则随机数生成函数每次生成的随机数序列都相同；如果不设置这个值，则系统根据时间来自己选择这个值，此时每次生成的随机数序列因时间差异而不同
r.seed(1)
# 笔画粗细
t.pensize(2)
# 笔画颜色
t.color('red')
angles = 6
points = [[0,0],[50,40],[70,80],[-40,30]]
# 记住range是范围，如果是数组肯定是取数组的长度range(0, len(points))也可以range(len(points))  0可以省略
for i in range(0, len(points)):
    x0, y0 = points[i]
    # 提笔
    t.penup()
    # 朝向目标坐标画
    t.goto(x0, y0)
    # 落笔
    t.pendown()

    length = r.randint(6, 16)
    for j in range(angles):
        # 向前画
        t.forward(length)
        # 返回 也可以写t.back()或者t.tb()
        t.backward(length)
        # 向旋转360/6 = 60°，六片雪花瓣
        t.right(360 / angles)
# 保存当前图画
t.done()