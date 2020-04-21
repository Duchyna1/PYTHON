import tkinter as tk
from Settings import *
from Ball import *
from Paddle import *
from Button import Button

gameSettings = settings['states']['game']

class State:
    PRE = 'pre'
    GAME = 'game'
    PAUSE = 'pause'
    SCORE = 'score'

class GameState(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.state = State.PRE
        self.canvasWidgets = {}
        self.score = 0

        self.create_widgets()

    def create_widgets(self):
        self.scoreLabel = tk.Label(self)
        self.scoreLabel['text'] = self.score
        self.scoreLabel.pack()

        self.canvas = tk.Canvas(self)
        self.canvas['width'] = gameSettings['canvas']['width']
        self.canvas['height'] = gameSettings['canvas']['height']
        self.canvas.pack()

        self.canvas.bind('<Button-1>', self.leftClick)
        self.canvas.bind('<Motion>', self.motion)

        self.preSetup()

    def preSetup(self):
        self.canvas.configure(bg=gameSettings[State.PRE]['bg'])
        self.canvasWidgets['preText'] = self.canvas.create_text(gameSettings['canvas']['width']//2,
                                                                gameSettings['canvas']['height']//2,
                                                                text=gameSettings[State.PRE]['text']['text'],
                                                                fill=gameSettings[State.PRE]['text']['color'],
                                                                font=gameSettings[State.PRE]['text']['font'])
        self.canvas.update()

    def gameSetup(self):
        self.canvas.configure(bg=gameSettings[State.GAME]['bg'])

        self.balls = []
        for i in range(10):
            self.balls.append(generateBall(self.canvas, i*settings['ball']['offset']))

        self.paddle = Paddle(self.canvas)

        self.canvas.update()
        self.loop()

    def pauseSetup(self):
        self.canvasWidgets['pauseQuitButton'] = Button(self.canvas,
                                                       0,
                                                       0,
                                                       gameSettings[State.PAUSE]['quitButton']['height'],
                                                       gameSettings[State.PAUSE]['quitButton']['border'],
                                                       gameSettings[State.PAUSE]['quitButton']['width'],
                                                       gameSettings[State.PAUSE]['quitButton']['color'],
                                                       gameSettings[State.PAUSE]['quitButton']['text']
                                                       )

        self.canvasWidgets['pauseRect'] = self.canvas.create_rectangle(gameSettings['canvas']['width'] // 2 - 150,
                                                                       gameSettings['canvas']['height'] // 2 - 50,
                                                                       gameSettings['canvas']['width'] // 2 + 150,
                                                                       gameSettings['canvas']['height'] // 2 + 50,
                                                                       width=gameSettings[State.PAUSE]['rect']['width'],
                                                                       fill=gameSettings[State.PAUSE]['rect']['color'],
                                                                       stipple="gray50")

        self.canvasWidgets['pauseText'] = self.canvas.create_text(gameSettings['canvas']['width'] // 2,
                                                                  gameSettings['canvas']['height'] // 2,
                                                                  text=gameSettings[State.PAUSE]['text']['text'],
                                                                  fill=gameSettings[State.PAUSE]['text']['color'],
                                                                  font=gameSettings[State.PAUSE]['text']['font'])
        self.canvas.update()

    def scoreSetup(self, win):
        # TODO: restart button, continue button
        if win:
            text = gameSettings['score']['text']['text']['win']
        else:
            text = gameSettings['score']['text']['text']['lose']
        self.canvasWidgets['scoreQuitButton'] = Button(self.canvas,
                                                       0,
                                                       0,
                                                       gameSettings[State.SCORE]['quitButton']['width'],
                                                       gameSettings[State.SCORE]['quitButton']['height'],
                                                       gameSettings[State.SCORE]['quitButton']['border'],
                                                       gameSettings[State.SCORE]['quitButton']['color'],
                                                       gameSettings[State.SCORE]['quitButton']['text']
                                                       )

        self.canvasWidgets['scoreRect'] = self.canvas.create_rectangle(gameSettings['canvas']['width'] // 2-150,
                                                                       gameSettings['canvas']['height'] // 2-50,
                                                                       gameSettings['canvas']['width'] // 2+150,
                                                                       gameSettings['canvas']['height'] // 2+50,
                                                                       width=gameSettings[State.SCORE]['rect']['width'],
                                                                       fill=gameSettings[State.SCORE]['rect']['color'],
                                                                       stipple="gray50")

        self.canvasWidgets['scoreText'] = self.canvas.create_text(gameSettings['canvas']['width'] // 2,
                                                                  gameSettings['canvas']['height'] // 2,
                                                                  text=text,
                                                                  fill=gameSettings[State.SCORE]['text']['color'],
                                                                  font=gameSettings[State.SCORE]['text']['font'])
        self.canvas.update()

    def leftClick(self, event=None):
        x, y = event.x, event.y
        if self.state == State.PRE:
            self.state = State.GAME
            self.canvas.delete(self.canvasWidgets['preText'])
            self.canvas.update()
            self.gameSetup()
        elif self.state == State.GAME:
            self.state = State.PAUSE
            self.pauseSetup()
        elif self.state == State.PAUSE:
            if self.canvasWidgets['pauseQuitButton'].x <= x <= self.canvasWidgets[
                'pauseQuitButton'].x+self.canvasWidgets['pauseQuitButton'].width:
                if self.canvasWidgets['pauseQuitButton'].y <= y <= self.canvasWidgets[
                    'pauseQuitButton'].y+self.canvasWidgets['pauseQuitButton'].height:
                    self.master.destroy()
            else:
                self.state = State.GAME
                self.canvas.delete(self.canvasWidgets['pauseText'])
                self.canvasWidgets['pauseText'] = None
                self.canvas.delete(self.canvasWidgets['pauseRect'])
                self.canvasWidgets['pauseRect'] = None
                self.canvasWidgets['pauseQuitButton'].remove()
                self.canvasWidgets['pauseQuitButton'] = None
                self.canvas.update()
                self.loop()
        elif self.state == State.SCORE:
            # TODO: restart button click, continue button click
            if self.canvasWidgets['scoreQuitButton'].x <= x <= self.canvasWidgets[
                'scoreQuitButton'].x+self.canvasWidgets['scoreQuitButton'].width:
                if self.canvasWidgets['scoreQuitButton'].y <= y <= self.canvasWidgets[
                    'scoreQuitButton'].y+self.canvasWidgets['scoreQuitButton'].height:
                    self.master.destroy()

    def motion(self, event=None):
        x = event.x
        if self.state == State.GAME:
            self.paddle.movePaddle(x)

    def check(self, ball, paddle):
        if paddle.getY() <= ball.getY() <= paddle.getY()+paddle.getHeight():
            if paddle.getX() <= ball.getX() <= paddle.getX()+paddle.getWidth():
                ball.remove()
                self.balls.remove(ball)
                paddle.setColor(ball.getGood())
                if ball.getGood():
                    self.score += gameSettings['game']['score']['good']
                else:
                    self.score -= gameSettings['game']['score']['bad']
                self.scoreLabel.configure(text=self.score)
                if self.score // 100 > settings['ball']['g']:
                    setG(self.score // 100)
                self.balls.append(generateBall(self.canvas))

    def loop(self, event=None):
        if self.score > gameSettings['toWin']:
            self.state = State.SCORE
            self.scoreSetup(True)
        if self.score < gameSettings['toLose']:
            self.state = State.SCORE
            self.scoreSetup(False)

        if self.state == State.GAME:
            for ball in self.balls:
                ball.move()
                self.check(ball, self.paddle)
                if ball.getY() > gameSettings['canvas']['height']:
                    if ball.getGood():
                        self.score -= gameSettings['game']['score']['missGood']
                    else:
                        self.score += gameSettings['game']['score']['missBad']
                    self.scoreLabel.configure(text=self.score)
                    if self.score // 100 > settings['ball']['g']:
                        setG(self.score // 100)
                    ball.remove()
                    self.balls.remove(ball)
                    self.balls.append(generateBall(self.canvas))

            self.canvas.update()
            self.canvas.after(gameSettings[State.GAME]['tickSpeed'], self.loop)
