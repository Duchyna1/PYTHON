import pygame
from apple import Apple
from snek import Snek
from globals import *

pygame.init()
screen = pygame.display.set_mode(WINDOW_DIMENSIONS)
running = True
clock = pygame.time.Clock()

tick = 0
direction = Direction.UP

snek = Snek(screen)
apple = Apple(screen, snek)

def drawAll():
    # screen.fill(WINDOW_COLOR)
    apple.draw()
    snek.draw()

# MAIN LOOP
while running:
    tick += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        # MOVEMENT
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP and snek.moves[0] != Direction.DOWN:
            direction = Direction.UP
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and snek.moves[0] != Direction.UP:
            direction = Direction.DOWN
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and snek.moves[0] != Direction.RIGHT:
            direction = Direction.LEFT
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and snek.moves[0] != Direction.LEFT:
            direction = Direction.RIGHT

    snek.move()

    if tick % SNEK_TILE_SIZE == 0:
        snek.setMove(direction)

    # SELF HIT DETECTION
    if snek.hit():
        print("HIT!")
    # APPLE HIT DETECTION
    if snek.tiles[0].x == apple.x and snek.tiles[0].y == apple.y:
        apple = Apple(screen, snek)
        snek.grow()

    drawAll()

    pygame.display.flip()
    clock.tick(60)
