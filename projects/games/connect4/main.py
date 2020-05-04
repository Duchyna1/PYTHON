import pygame
from globals import *
from cell import Cell

pygame.init()
pygame.display.set_caption(WINDOW_LABEL)
screen = pygame.display.set_mode(WINDOW_DIMENSIONS)
running = True

# GENERATE ALL CELLS
cells = []
for i in range(WINDOW_DIMENSIONS[0]//CELL_SIZE):
    row = []
    for j in range(WINDOW_DIMENSIONS[0]//CELL_SIZE):
        row.append(Cell(screen, j*CELL_SIZE, i*CELL_SIZE))
    cells.append(row)

# INPUT LOGIC
def quit():
    return event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE

while running:
    for event in pygame.event.get():
        # QUIT
        if quit():
            running = False

    # UPDATE SCREEN
    pygame.display.flip()

