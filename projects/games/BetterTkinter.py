import tkinter

global c

def start(width = 700, height = 500, bg = 'black'):
    global c
    c = tkinter.Canvas(width = width, height = height, bg = bg)
    c.pack()

def line(x1, y1, x2, y2, fill = 'white', width = 2):
    c.create_line(x1, y1, x2, y2, fill = fill, width = width)

def wait(time, thing = None):
    c.after(time, thing)

def rectangle(x1, y1, x2, y2, fill = None, width = 1):
    c.create_rectangle(x1, y1, x2, y2, fill = fill, width = width)

def circle(midleX, midleY, r, fill = None, width = 1, outline='white'):
    c.create_oval(midleX+r, midleY+r, midleX-r, midleY-r, fill = fill, width = width, outline=outline)

def bind_key(what, thing):
    c.bind_all(what, thing)

def update():
    c.update()

def bind_mouse(what, thing):
    c.bind(what, thing)

def reset():
    c.delete('all')

def delete(what):
    c.delete(what)

def oval(x1, y1, x2, y2, fill = None, width = 1):
    c.create_oval(x1, y1, x2, y2, fill = fill, width = width)

def end():
    c.mainloop()