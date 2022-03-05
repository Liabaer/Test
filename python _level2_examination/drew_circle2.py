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