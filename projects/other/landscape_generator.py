from opensimplex import OpenSimplex
import tkinter
from random import randint

########################################################################################################################

colors = [
    [-0.3, 'blue'],
    [-0.2, 'yellow'],
    [0.7, 'green'],
    [0.9, 'gray'],
    [1, 'white']
]

freq = 10

windowWidth, windowHeight = 1400, 800
cellsX, cellsY = 1400, 800
cellsWidth, cellsHeight = windowWidth/cellsX, windowHeight/cellsY

########################################################################################################################

c = tkinter.Canvas(width=windowWidth, height=windowHeight)
c.pack()

seed = randint(0, 10000)
gen = OpenSimplex(seed=seed)
print(seed)

cells = [[c.create_rectangle(x*cellsWidth, y*cellsHeight, x*cellsWidth+cellsWidth, y*cellsHeight+cellsHeight, width=0)
         for x in range(cellsX)] for y in range(cellsY)]

def noise(nx, ny):
    e = gen.noise2d(nx*freq, ny*freq)
    return e

def getColor(value):
    for x in colors:
        if value < x[0]:
            return x[1]

min = 2
max = 0

for y in range(cellsY):
    for x in range(cellsX):
        nx = x/cellsX - 0.5
        ny = y/cellsY - 0.5
        v = noise(nx, ny)
        c.itemconfig(cells[y][x], fill=getColor(v))
        if v < min:
            min = v
        if v > max:
            max = v
print(min, max)

c.mainloop()