Vo = int(input('Vo: '))
h = int(input('H: '))

import tkinter as tk

width, height = 750, 300

bt = tk.Canvas(width = width, height = height, bg = 'black')
bt.pack()

t = 0
g = 10
x = 0
y = height-h
r = 3
predX = x
predY = y

textX = bt.create_text(x, height//2, text = x, fill = 'white')
textY = bt.create_text(width//2, y, text = y, fill = 'white')


def play(event = None):
    global t, h, predX, predY, textX, textY
    x = Vo*t 
    y = height-(h-1/2*g*t**2)
    bt.create_line(predX, predY, x, y, fill = 'white')
    bt.delete(textX)
    bt.delete(textY)
    textX = bt.create_text(x, height//2, text = x, fill = 'white')
    textY = bt.create_text(width//2, y, text = y, fill = 'white')
    bt.update()
    h = height-y
    t += 0.001
    predX = x
    predY = y
    if y < 300:
        bt.after(1, play)


def step(event = None):
    global t, h, predX, predY, bod, textX, textY
    x = Vo*t 
    y = height-(h-1/2*g*t**2)
    bt.create_line(predX, predY, x, y, fill = 'white')
    bt.delete(textX)
    bt.delete(textY)
    textX = bt.create_text(x, height//2, text = x, fill = 'white')
    textY = bt.create_text(width//2, y, text = y, fill = 'white')
    bt.update()
    h = height-y
    t += 0.01
    predX = x
    predY = y


bt.bind_all('<Return>', play)
bt.bind_all('<space>', step)

bt.mainloop()