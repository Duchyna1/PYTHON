import pygame
from globals import *

class Cell:
    def __init__(self, screen,  x, y):
        self.x, self.y = x, y
        self.screen = screen
        self.state = CellState.NONE
        pygame.draw.rect(screen,                                    # screen
                         CELL_BORDER_COLOR,                         # color
                         (self.x, self.y, CELL_SIZE, CELL_SIZE))    # (x, y, width, height)
        pygame.draw.circle(screen,                                      # screen
                           WINDOW_COLOR,                                # color
                           (self.x+CELL_SIZE//2, self.y+CELL_SIZE//2),  # x, y
                           int(CELL_SIZE*0.75//2), 0)                   # int(r), border

    def setState(self, red):
        if red:
            self.color = RED
            self.state = CellState.RED
        else:
            self.color = YELLOW
            self.state = CellState.YELLOW

        pygame.draw.circle(self.screen,                                 # screen
                           self.color,                                  # color
                           (self.x+CELL_SIZE//2, self.y+CELL_SIZE//2),  # x, y
                           int(CELL_SIZE*0.75//2), 0)                   # int(r), border