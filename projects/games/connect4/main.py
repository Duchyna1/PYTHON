import pygame
from globals import *
from cell import Cell
from indicator import Indicator

# SETUP
pygame.init()
pygame.display.set_caption(WINDOW_LABEL)
screen = pygame.display.set_mode(WINDOW_DIMENSIONS)
running = True
indicator = Indicator(screen)

# GENERATE ALL CELLS
cells = []
for i in range((WINDOW_DIMENSIONS[1]-CELL_SIZE)//CELL_SIZE):
    row = []
    for j in range(WINDOW_DIMENSIONS[0]//CELL_SIZE):
        row.append(Cell(screen, j*CELL_SIZE, i*CELL_SIZE+INDICATOR_WIDTH))
    cells.append(row)

# DEFAULT PLAYER (True = red, False = yellow)
red = True

# INPUT LOGIC
def quitGame():
    return event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE

def mouseMotion():
    return event.type == pygame.MOUSEMOTION

def mouseClick():
    return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1

#####################################################################

def drawAll():
    indicator.draw()

def connected(cell):
    x, y = cell.x//CELL_SIZE, (cell.y-CELL_SIZE)//CELL_SIZE
    connected = True
    # DOWN
    try:
        for i in range(1, 4):
            if cells[y+i][x].state != cell.state:
                connected = False
    except:
        connected = False
    if connected:
        # debugging
        # print('DOWN')
        return connected

    # SIDES
    for i in range(-4, 0):
        connected = True
        for j in range(1, 5):
            try:
                fistCell = cells[y][x+i+j]
                # debugging
                # print('SIDE' ,x, x+i+j, y, y, fistCell.state)
                if fistCell.state != cell.state:
                    connected = False
            except:
                connected = False
        # debugging
        # print()
        if connected:
            # debugging
            # print('SIDE')
            return connected

    # DIAGONAL LEFT DOWN
    for i in range(-4, 0):
        connected = True
        for j in range(1, 5):
            try:
                fistCell = cells[y+i+j][x+i+j]
                # debugging
                # print('DLD' ,x+i+j, x, y+i+j, y, fistCell.state)
                if fistCell.state != cell.state:
                    connected = False
            except:
                connected = False
        # debugging
        # print()
        if connected:
            # debugging
            # print('DIAGONAL LEFT DOWN')
            return connected

    # DIAGONAL RIGHT UP
    for i in range(-4, 0):
        connected = True
        for j in range(1, 5):
            try:
                fistCell = cells[y-i-j][x+i+j]
                # debugging
                # print('DRU', x+i+j, x, y-i-j, y, fistCell.state)
                if fistCell.state != cell.state:
                    connected = False
            except:
                connected = False
        # debugging
        # print()
        if connected:
            # debugging
            # print('DIAGONAL RIGHT UP')
            return connected

while running:
    for event in pygame.event.get():
        # QUIT
        if quitGame():
            running = False

        # MOVING INDICATOR
        if mouseMotion():
            pos = pygame.mouse.get_pos()
            indicator.move(pos[0])

        # PLACING IDK CIRCLES?
        if mouseClick():
            pos = pygame.mouse.get_pos()
            indicator.switchColors()
            x = pos[0]//CELL_SIZE
            for y in reversed(range((WINDOW_DIMENSIONS[1]-CELL_SIZE)//CELL_SIZE)):
                if cells[y][x].state == CellState.NONE:
                    cells[y][x].setState(red)
                    if connected(cells[y][x]):
                        print(red, 'YAY!')
                    red = not red
                    break


    drawAll()

    # UPDATE SCREEN
    pygame.display.flip()
