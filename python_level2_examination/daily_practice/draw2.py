import turtle as t


def cir(x, y, head, R, angle):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.seth(head)
    t.circle(R, angle)


def arc(R, angle, r, n):
    dltr = (r - R) / n
    for i in range(1, n + 1):
        t.circle(-R, angle / n)
        R += dltr


t.penup()
t.goto(0, 100)
t.pendown()
t.seth(45)
t.speed(10)
t.pensize(3)
t.color("black", "#CC0099")
t.begin_fill()
r = 300
arc(300, 90, 50, 10)
arc(50, 90, 300, 10)
arc(300, 90, 50, 10)
arc(50, 90, 300, 10)
t.end_fill()
t.color("black", "#FF99FF")
t.begin_fill()
cir(140, -40, 60, -260, 35)
cir(180, 15, 70, -260, 25)
t.seth(-140)
arc(200, 40, 20, 10)
arc(20, 60, 110, 15)
t.seth(-100)
arc(160, 40, 30, 10)
arc(30, 60, 150, 10)
t.seth(-45)
arc(140, 50, 5, 10)
arc(5, 80, 130, 10)
cir(-39, -60, 17, -260, 22)
cir(50, -55, 20, -260, 20)
t.end_fill()
cir(140, -40, -180, 260, 40)
cir(160, -130, -30, -280, 40)
cir(250, -40, -90, 280, 40)
t.color("black", "green")
t.begin_fill()
t.seth(90)
t.fd(50)
t.seth(-40)
arc(180, 110, 10, 10)
arc(10, 110, 180, 10)
t.seth(-10)
t.fd(50)
t.seth(100)
t.fd(50)
t.seth(-30)
t.fd(50)
t.end_fill()
t.done()
