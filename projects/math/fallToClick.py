import tkinter
from math import sqrt

width, height = 700, 700

canvas = tkinter.Canvas(width = width, height = height, background = 'black')
canvas.pack()

g = 10
ts = 0.01

ct = 0

x, y = 10, 10
px, py = x, y
sx, sy = x, y

vx = 0

tx, ty = 0, 0

lines = []

r = 5

class point:
    def __init__(self, x, y, r):
        self.x, self.y = x, y
        self.r = r

point = point(10, 10, 5)

def fallTime(y0, y1):
    t = int(sqrt((abs(y1-y0))/(1/2*abs(g)))*10)
    print(t)
    return t

def sideSpeed(x0, x1, t):
    v = (x1-x0)/t
    return v

def fall(event = None):
    global ct, px, py, lines, ct, sx, sy, vx
    point.y = int(sy+1/2*g*ts*ct**2)
    point.x = vx*ct+sx
    canvas.update()
    ct += 1
    lines.append(canvas.create_line(point.x, point.y, px, py, fill = 'white'))
    px, py = point.x, point.y
    if g == 10:
        if point.y < ty:
            canvas.after(int(ts*1000), fall)
        else:
            print(ct)
            ct = 0
            sx, sy = point.x, point.y
    if g == -10:
        if point.y > ty:
            canvas.after(int(ts*1000), fall)
        else:
            print(ct)
            ct = 0
            sx, sy = point.x, point.y

def click(event):
    global vx, tx, ty, lines, g, ct
    ct = 0
    # for line in lines:
    #     canvas.delete(line)
    canvas.update()
    cx, cy = event.x, event.y
    t = fallTime(point.y, cy)
    vx = sideSpeed(point.x, cx, t)
    tx, ty = cx, cy
    if ty < point.y:
        g = -10
    else:
        g = 10
    fall()

canvas.bind_all("<Button-1>", click)
canvas.bind_all('<Return>', fall)

canvas.mainloop()