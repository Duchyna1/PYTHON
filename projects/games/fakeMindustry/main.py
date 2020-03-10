import tkinter
from projects.games.fakeMindustry.cell import cell
from projects.games.fakeMindustry.building import building

from projects.games.fakeMindustry.things import Materials, Buildings

from opensimplex import OpenSimplex
from random import randint
import math

########################################################################################################################

windowWidth, windowHeight = 500, 500
widthCells, heightCells = 50, 50

game = tkinter.Canvas(width=windowWidth, height=windowHeight+100)
game.pack()

cellWidth, cellHeight = windowWidth//widthCells, windowHeight//heightCells

cells = [[None for x in range(0, windowWidth, cellWidth)] for y in range(0, windowHeight, cellHeight)]

########################################################################################################################

def noise(nx, ny, big, seed):
    gen = OpenSimplex(seed=seed)
    return gen.noise2d(nx*big, ny*big)


def clickL(event):
    x, y = event.x//cellWidth, event.y//cellHeight
    if cells[y][x].building is None:
        cells[y][x].setBuilding(Buildings.MINE)
    elif cells[y][x].building.type == Buildings.MINE:
        cells[y][x].setBuilding(None)


def clickR(event):
    x, y = event.x//cellWidth, event.y//cellHeight
    if cells[y][x].material == Materials.STONE:
        cells[y][x].setMaterial(Materials.IRON)
    elif cells[y][x].material == Materials.IRON:
        cells[y][x].setMaterial(Materials.STONE)


def tick():
    game.update()
    game.after(100, tick)


def generateOre(material, n, p, b):
    seed = randint(0, 100000)

    max, min = -1, 9999
    values = []
    for y in range(windowHeight // cellHeight):
        values.append([0] * widthCells)
        for x in range(windowWidth // cellWidth):
            nx = x / widthCells - 0.5
            ny = y / widthCells - 0.5
            values[y][x] = int(noise(nx, ny, b, seed)*n)
            if values[y][x] > max:
                max = values[y][x]
            if values[y][x] < min:
                min = values[y][x]

    for y in range(windowHeight // cellHeight):
        for x in range(windowWidth // cellWidth):
            if values[x][y] > (max - min) * p + min:
                cells[y][x] = cell(game, x * cellWidth, y * cellHeight, cellWidth, cellHeight, material)
            if cells[y][x] is None:
                cells[y][x] = cell(game, x * cellWidth, y * cellHeight, cellWidth, cellHeight, Materials.STONE)


########################################################################################################################

generateOre(Materials.COAL, 100, 0.8, 10)
generateOre(Materials.IRON, 100, 0.9, 15)

tick()

########################################################################################################################

game.bind_all("<Button-1>", clickL)
game.bind_all("<Button-3>", clickR)

game.mainloop()
