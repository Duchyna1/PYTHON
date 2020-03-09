import tkinter
from projects.games.fakeMindustry.cell import cell
from projects.games.fakeMindustry.building import building

from projects.games.fakeMindustry.things import Materials, Buildings

########################################################################################################################

windowWidth, windowHeight = 500, 500
widthCells, heightCells = 5, 5

game = tkinter.Canvas(width=windowWidth, height=windowHeight+100)
game.pack()

cellWidth, cellHeight = windowWidth//widthCells, windowHeight//heightCells

cells = [[cell(game, x, y, cellWidth, cellHeight, Materials.STONE) for x in range(0, windowWidth, cellWidth)] for y in range(0, windowHeight, cellHeight)]

########################################################################################################################

def clickL(event):
    x, y = event.x//cellWidth, event.y//cellHeight
    if cells[y][x].building is Buildings.NONE:
        cells[y][x].setBuilding(Buildings.MINE)
    elif cells[y][x].building.type == Buildings.MINE:
        cells[y][x].setBuilding(Buildings.NONE)


def clickR(event):
    x, y = event.x//cellWidth, event.y//cellHeight
    if cells[y][x].material == Materials.STONE:
        cells[y][x].setMaterial(Materials.IRON)
    elif cells[y][x].material == Materials.IRON:
        cells[y][x].setMaterial(Materials.STONE)


def tick():
    game.update()
    game.after(100, tick)


########################################################################################################################

tick()

########################################################################################################################

game.bind_all("<Button-1>", clickL)
game.bind_all("<Button-3>", clickR)

game.mainloop()
