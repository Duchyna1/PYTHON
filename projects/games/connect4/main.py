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
###########

def drawAll():
    indicator.draw()

def connected(cell):
    x, y = cell.x//CELL_SIZE, (cell.y-CELL_SIZE)//CELL_SIZE
    # DOWN
    if y <= 4:
        for i in range(1, 4):
            if cells[y+i][x].state != cell.state:
                return False
    else:
        return False
    return True

while running:
    for event in pygame.event.get():
        # QUIT
        if quitGame():
            running = False
        # MOVING INDICATOR
        if mouseMotion():
            pos = pygame.mouse.get_pos()
            indicator.move(pos[0])
        if mouseClick():
            pos = pygame.mouse.get_pos()
            indicator.switchColors()
            x = pos[0]//CELL_SIZE
            for y in reversed(range((WINDOW_DIMENSIONS[1]-CELL_SIZE)//CELL_SIZE)):
                if cells[y][x].state == CellState.NONE:
                    cells[y][x].setState(red)
                    if connected(cells[y][x]):
                        print(red, 'YAY!')
                        break
                    else:
                        red = not red
                        break

    drawAll()

    # UPDATE SCREEN
    pygame.display.flip()

