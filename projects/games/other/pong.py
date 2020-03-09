import tkinter
from random import randint

width, height = 800, 500

game = tkinter.Canvas(width = width, height = height, background = 'black')
game.pack()

class paddle:

    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.paddle = game.create_rectangle(self.x, self.y, self.x+self.width, self.y+self.height, fill = "white", width = 0)

    def move(self, direc):
        self.y = self.y+direc*self.speed
        if self.y < 0:
            self.y = 0
        elif self.y > height-self.height:
            self.y = height-self.height
        else:
            game.move(self.paddle, 0, direc*self.speed)

class ball:

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.speedX = randint(-5, 5)
        self.speedY = randint(-5, 5)
        self.ball = game.create_oval(x-r, y-r, x+r, y+r, fill = "white", width = 0)
    
    def move(self):
        self.x = self.x+self.speedX
        self.y = self.y+self.speedY
        if self.x < self.r:
            self.x = self.r
            self.speedX *= -1
        elif self.x > width-self.r:
            self.x = width-self.r
            self.speedX *= -1
        if self.y < self.r:
            self.y = self.r
            self.speedY *= -1
        elif self.y > height-self.r:
            self.y = height-self.r
            self.speedY *= -1
        game.move(self.ball, self.speedX, self.speedY)

paddleL = paddle(25, 10, 10, 50, 10)
paddleR = paddle(width-25, 10, 10, 50, 10)

ball = ball(width//2, height//2, 10)

def upL(event = None):
    paddleL.move(-1)

def downL(event = None):
    paddleL.move(1)

def upR(event = None):
    paddleR.move(-1)

def downR(event = None):
    paddleR.move(1)

def start(event = None):
    ball.move()
    game.after(10, start)

game.bind_all("w", upL)
game.bind_all("s", downL)
game.bind_all("<Up>", upR)
game.bind_all("<Down>", downR)
game.bind_all("o", upR)
game.bind_all("l", downR)
game.bind_all('<Return>', start)

game.mainloop()