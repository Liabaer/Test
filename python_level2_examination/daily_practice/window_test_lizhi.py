import jieba
import turtle as t


def drawCircle(x, y, radius, color, name):
    t.pencolor(color)
    t.penup()
    t.goto(x, y)
    # 在画板上写文字
    t.write(name, font=('Arial', 10, 'normal'))
    t.seth(-90)
    t.pendown()
    t.circle(radius)
    return t.pos()  # 返回当前的坐标


dws = {}
with open("lizhi.txt", 'r', encoding='utf-8') as f:
    for l in f.readlines():
        ws = jieba.lcut(l)
        for w in ws:
            if len(w) >= 2:
                dws[w] = dws.get(w, 0) + 1

dls = list(dws.items())
dls.sort(key=lambda x: x[1], reverse=True)
temp = dls[0:10]
name = []
for i in temp:
    name.append(str(i[0]) + '' + str(i[1]))
    print('{} {}'.format(i[0], i[1]))
x, y = -300, 0
for i in range(5):
    x, y = drawCircle(x, y, dls[i][1] * 4, 'red', name[i])
    x += dls[i][1] * 8
t.done()
