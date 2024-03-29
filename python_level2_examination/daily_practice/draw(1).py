import turtle


def cir(x, y, head, R, angle):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.seth(head)
    turtle.circle(R, angle)


def arc(R, angle, r, n):
    dltr = (r - R) / n
    for i in range(1, n + 1):
        turtle.circle(-R, angle / n)
        R += dltr


turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.seth(45)
turtle.speed(10)
turtle.pensize(3)
turtle.color("black", "#CC0099")
turtle.begin_fill()
r = 300
arc(300, 90, 50, 10)
arc(50, 90, 300, 10)
arc(300, 90, 50, 10)
arc(50, 90, 300, 10)
turtle.end_fill()
turtle.color("black", "#FF99FF")
turtle.begin_fill()
cir(140, -40, 60, -260, 35)
cir(180, 15, 70, -260, 25)
turtle.seth(-140)
arc(200, 40, 20, 10)
arc(20, 60, 110, 15)
turtle.seth(-100)
arc(160, 40, 30, 10)
arc(30, 60, 150, 10)
turtle.seth(-45)
arc(140, 50, 5, 10)
arc(5, 80, 130, 10)
cir(-39, -60, 17, -260, 22)
cir(50, -55, 20, -260, 20)
turtle.end_fill()
cir(140, -40, -180, 260, 40)
cir(160, -130, -30, -280, 40)
cir(250, -40, -90, 280, 40)
turtle.color("black", "green")
turtle.begin_fill()
turtle.seth(90)
turtle.fd(50)
turtle.seth(-40)
arc(180, 110, 10, 10)
arc(10, 110, 180, 10)
turtle.seth(-10)
turtle.fd(50)
turtle.seth(100)
turtle.fd(50)
turtle.seth(-30)
turtle.fd(50)
turtle.end_fill()
turtle.done()
