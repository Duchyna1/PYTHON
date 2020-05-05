import pygame
from globals import *

class Indicator:
    def __init__(self, screen):
        self.screen = screen
        self.x = WINDOW_DIMENSIONS[0]//2
        self.color = RED

    def draw(self):
        pygame.draw.rect(self.screen,                                   # screen
                         WHITE,                                         # color
                         (0, 0, WINDOW_DIMENSIONS[0], INDICATOR_WIDTH)) # x, y, width, height
        pygame.draw.circle(self.screen,                     # screen
                           self.color,                      # color
                           (self.x, INDICATOR_WIDTH//2),    # x, y
                           int(INDICATOR_WIDTH*0.75//2), 0) # int(r), border

    def switchColors(self):
        if self.color == RED:
            self.color = YELLOW
        else:
            self.color = RED

    def move(self, x):
        self.x = x
