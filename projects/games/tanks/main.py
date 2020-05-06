import pygame
from tanks.Tank import Tank
from globals import *

pygame.init()
pygame.display.set_caption(WINDOW_LABEL)
screen = pygame.display.set_mode(WINDOW_DIMENSIONS)
running = True

tank = Tank(screen, WINDOW_DIMENSIONS[0]//2, WINDOW_DIMENSIONS[1]//2, 0, RED, None)
allSprites = pygame.sprite.RenderPlain(tank)
pygame.display.flip()

# INPUT LOGIC
def quitGame():
    return event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE

def drawAll():
    screen.fill(WINDOW_BG)
    allSprites.update()
    allSprites.draw(screen)
    pygame.display.flip()

while running:
    for event in pygame.event.get():
        # QUIT
        if quitGame():
            running = False
    drawAll()
