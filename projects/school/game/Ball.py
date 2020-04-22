import tkinter as tk
from Settings import settings
from random import randint

def generateBall(canvas, offset=0):
    random = randint(0, 10)
    if random < 7:
        good = True
    else:
        good = False
    return Ball(canvas,
                randint(settings['ball']['r'],
                        settings['states']['game']['canvas']['width']-settings['ball']['r']),
                good,
                offset)

class Ball:
    def __init__(self, canvas, x, good, offset):
        self.r = settings['ball']['r']
        self.width = settings['ball']['width']
        self.g = settings['ball']['g']

        self.canvas = canvas
        self.x, self.y = x, -self.r-offset

        self.good = good
        if self.good:
            self.color = settings['ball']['color']['good']
        else:
            self.color = settings['ball']['color']['bad']
        self.circle = self.canvas.create_oval(self.x-self.r,
                                              self.y-self.r,
                                              self.x+self.r,
                                              self.y+self.r,
                                              width=self.width,
                                              fill=self.color)

    def getY(self):
        return self.y

    def getX(self):
        return self.x

    def remove(self):
        self.canvas.delete(self.circle)

    def getGood(self):
        return self.good

    def move(self):
        self.canvas.move(self.circle, 0, self.g)
        self.y += self.g
