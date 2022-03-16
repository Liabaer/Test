# -*- coding: utf-8 -*-
# 使用turtle库的turtle.fd()函数和turtle.seth()函数 绘制一个边长为40像素的正12边型，在模板中横线 处替换代码，不得修改其他代码，效果如下图所 示。
# 在————————上补充代码

# import turtle
#
# turtle.pensize(2)
# d = 0
# for i in range(1, 13):
#     turtle.fd(40)
#     d += 30
#     turtle.seth(d)
# # turtle.pendown()


# 使用tute库的函数绘制10层螺旋状放大的类正方形，类正方形边长从0度方 向、边长为1像素开始，每条边长度比前一条边增加2个像素，画笔逆时针旋转 91度。
# import turtle
# d = 0
# k = 1
# for j in range(10):
#     for i in range(4):
#         turtle.forward(k)
#         d += 91
#         turtle.seth(d)
#         k += 2
# turtle.done()

# 使用turtle库的turtle.fd0函数和turtle.seth(0)函数绘制嵌套10层的螺旋六边形，
# 六边形边长从1像素开始，第一条边从0度方向开始，边长按照3个像素递增，效 果如下图所示。
# import turtle
# edge = 6
# d = 0
# k = 1
# for j in range(10):
#     for i in range(edge):
#         turtle.fd(k)
#         d += 360/6
#         turtle.seth(d)
#         k += 3
# turtle.done()

# 使用turtle库的turtle.right()函数和turtle.circle()函数绘制一个星星图形，圆弧的 半径为90，如下图所示。
# import turtle
# for i in range(4):
#     turtle.circle(-90, 90)  #这个空为一个负数
#     turtle.right(180)
# turtle.done()

# 画太阳花
import turtle
turtle.color("red", "yellow") #画笔颜色与填充设置
turtle.begin_fill()
#绘制太阳花形状
for i in range(50):
    turtle.forward(200)#先前200
    turtle.right(170)  #右转170度
turtle.end_fill()
turtle.done()