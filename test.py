# # 1
# import tkinter
#
# canvas = tkinter.Canvas(width=700, height=400)
# canvas.pack()
#
# subor = open('MAPY.txt', 'r')
# n = int(subor.readline())
# for i in range(1, n+1):
#     riadok = subor.readline()
#     s = riadok.split()
#     x, y = int(s[0]), int(s[1])
#     canvas.create_oval(x-1, y-1, x+1, y+1)
#
# riadok = subor.readline()
# while riadok:
#     s = riadok.split()
#     x, y = int(s[0]), int(s[1])
#     obyvatelia = int(s[2])
#     nazov = s[3]
#     r = 0
#
#     if obyvatelia > 100:
#         r = 10
#     if 50 < obyvatelia <= 100:
#         r = 7
#     if 10 < obyvatelia <= 50:
#         r = 5
#     if obyvatelia <= 10:
#         r = 3
#
#     farba = 'green'
#     if obyvatelia > 500:
#         farba = 'red'
#     if 200 < obyvatelia <= 500:
#         farba = 'blue'
#
#     canvas.create_oval(x-r, y-r, x+r, y+r, fill=farba)
#
#     canvas.create_text(x, y+15, text=nazov)
#
#     riadok = subor.readline()
# subor.close()
# canvas.mainloop()
#
# 2
import tkinter

canvas = tkinter.Canvas(width=700, height=500)
canvas.pack()
subor = open('kresli.txt', 'r')

riadok = subor.readline()
while riadok:
    s = riadok.split()
    n = int(s[0])
    x, y = int(s[1]), int(s[2])

    canvas.create_oval(x-2, y-2, x+2, y+2)
    canvas.create_text(x, y+10, text=n)

    riadok = subor.readline()

zaciatokX = 0
zaciatokY = 0

def click(miesto):
    global zaciatokX, zaciatokY
    zaciatokX, zaciatokY = miesto.x, miesto.y


def tahanieMiskou(miesto):
    global zaciatokX, zaciatokY
    x, y = miesto.x, miesto.y
    canvas.create_line(zaciatokX, zaciatokY, x, y)


canvas.bind_all("<B1-Motion>", tahanieMiskou)
canvas.bind_all("<Button-1>", click)

canvas.mainloop()
