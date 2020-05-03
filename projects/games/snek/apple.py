import pygame
import random
from globals import *

class Apple:
    def __init__(self, screen, snek):
        self.screen = screen
        self.generate()
        while not self.check(snek):
            self.generate()
        pygame.draw.rect(self.screen, APPLE_COLOR, (self.x+1, self.y+1, APPLE_SIZE-1, APPLE_SIZE-1))

    def draw(self):
        pygame.draw.rect(self.screen, APPLE_COLOR, (self.x+1, self.y+1, APPLE_SIZE-1, APPLE_SIZE-1))

    def generate(self):
        self.x = random.randint(APPLE_SIZE / 2, WINDOW_DIMENSIONS[0]-APPLE_SIZE / 2) // APPLE_SIZE * APPLE_SIZE
        self.y = random.randint(APPLE_SIZE / 2, WINDOW_DIMENSIONS[1]-APPLE_SIZE / 2) // APPLE_SIZE * APPLE_SIZE

    def check(self, snek):
        for tile in snek.tiles:
            if tile.x == self.x and tile.y == self.y:
                return False
        return True

