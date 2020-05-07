import pygame, sys, time, random
from pygame.locals import *
from Colours import *

pygame.init()
fps = 30
clock = pygame.time.Clock()
size = width,height = 800,600
screen = pygame.display.set_mode(size)
mySprite = MySprite()

while True:
    event = Event()
    screen.fill(Blue)
    mySprite.draw(screen)
    mySprite.onKeyPress()
    pygame.display.update()
    clock.tick(fps)