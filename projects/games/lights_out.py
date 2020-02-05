import tkinter
from random import randint

col = 8 #x
row = 8 #y
width = 50
on = 'green'
off = 'black'
outline = 'gray'

game = tkinter.Canvas(height = row*width, width = col*width)
game.pack()

class Light:
    def __init__(self, x, y, turn):
        self.turn = turn
        self.x = x
        self.y = y
        if self.turn == 0:
            game.create_rectangle(self.x*50, self.y*50, self.x*50+width, self.y*50+width, fill = off, width = 1, outline = outline)
        if self.turn == 1:
            game.create_rectangle(self.x*50, self.y*50, self.x*50+width, self.y*50+width, fill = on, width = 1, outline = outline)

    def change(self):
        if self.turn == 0:
            game.create_rectangle(self.x*50, self.y*50, self.x*50+width, self.y*50+width, fill = on, width = 1, outline = outline)
            self.turn = 1
        else:
            game.create_rectangle(self.x*50, self.y*50, self.x*50+width, self.y*50+width, fill = off, width = 1, outline = outline)
            self.turn = 0
        game.update()

    def around(self):
        lights[self.x][self.y].change()
        if not self.x-1 < 0:
            lights[self.x-1][self.y].change()
        if not self.y-1 < 0:
            lights[self.x][self.y-1].change()
        if not self.x+1 == col:
            lights[self.x+1][self.y].change()
        if not self.y+1 == row:
            lights[self.x][self.y+1].change()


def setup(event=None):
    global lights
    lights = []
    for x in range(col):
        new = []
        for y in range(row):
            new.append(Light(x, y, randint(0, 1)))
        lights.append(new)

def rc(event):
    x = event.x//width
    y = event.y//width
    lights[x][y].change()

def lc(event):
    x = event.x//width
    y = event.y//width
    lights[x][y].around()

setup()
game.bind_all('r', setup)
game.bind('<Button-3>', rc)
game.bind('<ButtonPress>', lc)

game.mainloop()