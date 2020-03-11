import tkinter
from random import randint

from opensimplex import OpenSimplex

from projects.games.fakeMindustry.cell import cell
from projects.games.fakeMindustry.things import Materials, Buildings

########################################################################################################################

ticks = 0
tickSpeed = 100

windowWidth, windowHeight = 1000, 600
widthCells, heightCells = 100, 60

game = tkinter.Canvas(width=windowWidth, height=windowHeight+100)
game.pack()

cellWidth, cellHeight = windowWidth//widthCells, windowHeight//heightCells

print('Making grid... ', end='')
cells = [[None for x in range(0, windowWidth, cellWidth)] for y in range(0, windowHeight, cellHeight)]
print('DONE!')
buildings = []

########################################################################################################################

def clickL(event):
    x, y = event.x//cellWidth, event.y//cellHeight
    if cells[y][x].building is None:
        cells[y][x].setBuilding(Buildings.MINE)
        buildings.append(cells[y][x].building)
    elif cells[y][x].building.type == Buildings.MINE:
        buildings.remove(cells[y][x].building)
        cells[y][x].setBuilding(None)

def clickR(event):
    x, y = event.x//cellWidth, event.y//cellHeight
    if cells[y][x].material == Materials.STONE:
        cells[y][x].setMaterial(Materials.IRON)
    elif cells[y][x].material == Materials.IRON:
        cells[y][x].setMaterial(Materials.STONE)

def tick():
    global ticks
    for b in buildings:
        b.action(ticks)
    game.update()
    ticks += 1
    game.after(tickSpeed, tick)

def noise(nx, ny, big, seed):
    gen = OpenSimplex(seed=seed)
    return gen.noise2d(nx*big, ny*big)

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
            if values[y][x] > (max - min) * p + min:
                cells[y][x] = cell(game, x * cellWidth, y * cellHeight, cellWidth, cellHeight, material)
            if cells[y][x] is None:
                cells[y][x] = cell(game, x * cellWidth, y * cellHeight, cellWidth, cellHeight, Materials.STONE)

def generate():
    print('Generating COAL... ', end='')
    generateOre(Materials.COAL, 100, 0.8, 3)
    print('DONE!')
    print('Generating IRON... ', end='')
    generateOre(Materials.IRON, 100, 0.88, 8)
    print('DONE!')
    print('Generating GOLD... ', end='')
    generateOre(Materials.GOLD, 100, 0.9, 10)
    print('DONE!')
    print('Generating DIAMONDS... ', end='')
    generateOre(Materials.DIAMOND, 100, 0.95, 15)
    print('DONE!')


########################################################################################################################

generate()
tick()

########################################################################################################################

game.bind_all("<Button-1>", clickL)
game.bind_all("<Button-3>", clickR)

game.mainloop()
