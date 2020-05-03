import pygame
from globals import *

class Snek:
    def __init__(self, screen):
        self.screen = screen
        self.tiles = [Tile(self.screen,
                          WINDOW_DIMENSIONS[0]//2-SNEK_TILE_SIZE//2,
                          WINDOW_DIMENSIONS[1]//2-SNEK_TILE_SIZE//2+SNEK_TILE_SIZE*yoff)
                      for yoff in range(DEFAULT_SNEK_SIZE)]
        self.tail = Tail(self.screen)
        self.moves = [Direction.UP for i in range(DEFAULT_SNEK_SIZE+1)]

    def grow(self):
        self.moves.append(Direction.NONE)
        self.tiles.append(Tile(self.screen, self.tail.x, self.tail.y))

    def draw(self):
        self.tail.draw()
        for tile in self.tiles:
            tile.draw()

    def move(self):
        self.tail.move(self.moves[-1])
        for i in range(len(self.tiles)):
            self.tiles[i].move(self.moves[i])

    def setMove(self, direction):
        self.moves.insert(0, direction)
        self.moves.pop()

    def hit(self):
        for i in range(1, len(self.tiles)):
            if self.tiles[0].x == self.tiles[i].x and self.tiles[0].y == self.tiles[i].y:
                return True
        return False

class Tile:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x, self.y = x, y
        pygame.draw.rect(self.screen, SNEK_COLOR, (self.x+1, self.y+1, SNEK_TILE_SIZE-1, SNEK_TILE_SIZE-1))

    def draw(self):
        pygame.draw.rect(self.screen, SNEK_COLOR, (self.x+1, self.y+1, SNEK_TILE_SIZE-1, SNEK_TILE_SIZE-1))

    def move(self, direction):
        if direction == Direction.NONE:
            pass
        elif direction == Direction.UP:
            self.y -= 1
        elif direction == Direction.DOWN:
            self.y += 1
        elif direction == Direction.LEFT:
            self.x -= 1
        elif direction == Direction.RIGHT:
            self.x += 1


class Tail:
    def __init__(self, screen):
        self.screen = screen
        self.x = WINDOW_DIMENSIONS[0]//2-SNEK_TILE_SIZE//2
        self.y = WINDOW_DIMENSIONS[0]//2-SNEK_TILE_SIZE//2+SNEK_TILE_SIZE*DEFAULT_SNEK_SIZE

    def draw(self):
        pygame.draw.rect(self.screen, WINDOW_COLOR, (self.x, self.y, SNEK_TILE_SIZE, SNEK_TILE_SIZE))

    def move(self, direction):
        if direction == Direction.NONE:
            pass
        elif direction == Direction.UP:
            self.y -= 1
        elif direction == Direction.DOWN:
            self.y += 1
        elif direction == Direction.LEFT:
            self.x -= 1
        elif direction == Direction.RIGHT:
            self.x += 1
