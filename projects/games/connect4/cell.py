import pygame
from globals import *

class Cell:
    def __init__(self, screen,  x, y):
        self.x, self.y = x, y
        self.screen = screen
        self.state = CellState.NONE
        pygame.draw.rect(screen,                        # screen
                         CELL_BORDER_COLOR,             # color
                         (x, y, CELL_SIZE, CELL_SIZE))  # (x, y, width, height)
        pygame.draw.circle(screen,                          # screen
                           WINDOW_COLOR,                    # color
                           (x+CELL_SIZE//2, y+CELL_SIZE//2),# x, y
                           int(CELL_SIZE*0.75//2), 0)       # int(r), border
