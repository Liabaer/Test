# -*- coding: utf-8 -*-
# 使用turtle库的turtle.fd()函数和turtle.seth()函数 绘制一个边长为40像素的正12边型，在模板中横线 处替换代码，不得修改其他代码，效果如下图所 示。
# 在————————上补充代码

import turtle

turtle.pensize(2)
d = 0
for i in range(1, 13):
    turtle.fd(40)
    d += 30
    turtle.seth(d)
# turtle.pendown()