# -*- coding: utf-8 -*-

# 在右侧答题模板中修改代码,删除代码中的横线,填写代 码,完成如下功能。
# 根据列表保存的数据采用 Turtle库画图直方图,显示输出 在屏幕上,效果如下图所示。
# LS=[69,29233,131,61,254


import turtle as t

ls = [69, 292, 33, 131, 61, 254]
X_len = 400
Y_len = 300
x0 = -200
y0 = -100

t.penup()
t.goto(x0, y0)
t.pendown()

t.fd(X_len)
t.fd(-X_len)
t.seth(90)
t.fd(Y_len)

t.pencolor('red')
t.pensize(5)
for i in range(len(ls)):
    t.penup()
    t.goto(x0 + (i + 1) * 50, y0)
    t.seth(90)
    t.pendown()
    t.fd(ls[i])
t.done()
