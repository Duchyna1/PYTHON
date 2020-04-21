import tkinter as tk
from Settings import settings

class Paddle:
    def __init__(self, canvas):
        self.canvas = canvas

        self.x = settings['states']['game']['canvas']['width'] // 2 - settings['paddle']['width'] // 2
        self.y = settings['states']['game']['canvas']['height'] - settings['paddle']['height'] - settings['paddle']['h']
        self.color = settings['paddle']['color']['good']
        self.width = settings['paddle']['border']
        self.rect = self.canvas.create_rectangle(self.x- settings['paddle']['width'] // 2,
                                                 self.y,
                                                 self.x+settings['paddle']['width'] // 2,
                                                 self.y+settings['paddle']['height'],
                                                 fill=self.color,
                                                 width=self.width)

    def getY(self):
        return self.y

    def getX(self):
        return self.x

    def getWidth(self):
        return settings['paddle']['width']

    def getHeight(self):
        return settings['paddle']['height']

    def setColor(self, good):
        if good:
            self.canvas.itemconfig(self.rect, fill=settings['paddle']['color']['good'])
        else:
            self.canvas.itemconfig(self.rect, fill=settings['paddle']['color']['bad'])

    def movePaddle(self, x):
        self.canvas.move(self.rect, x-self.x, 0)
        self.x = self.x+x-self.x
