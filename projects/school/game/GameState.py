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

        self.WON = False

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
                                                       2,
                                                       2,
                                                       gameSettings[State.PAUSE]['quitButton']['width'],
                                                       gameSettings[State.PAUSE]['quitButton']['height'],
                                                       gameSettings[State.PAUSE]['quitButton']['border'],
                                                       gameSettings[State.PAUSE]['quitButton']['color'],
                                                       gameSettings[State.PAUSE]['quitButton']['text']
                                                       )

        self.canvasWidgets['pauseRestartButton'] = Button(self.canvas,
                                                       102,
                                                       2,
                                                       gameSettings[State.PAUSE]['restartButton']['width'],
                                                       gameSettings[State.PAUSE]['restartButton']['height'],
                                                       gameSettings[State.PAUSE]['restartButton']['border'],
                                                       gameSettings[State.PAUSE]['restartButton']['color'],
                                                       gameSettings[State.PAUSE]['restartButton']['text']
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
        self.WON = True
        if win:
            text = gameSettings['score']['text']['text']['win']
        else:
            text = gameSettings['score']['text']['text']['lose']
        self.canvasWidgets['scoreQuitButton'] = Button(self.canvas,
                                                       2,
                                                       2,
                                                       gameSettings[State.SCORE]['quitButton']['width'],
                                                       gameSettings[State.SCORE]['quitButton']['height'],
                                                       gameSettings[State.SCORE]['quitButton']['border'],
                                                       gameSettings[State.SCORE]['quitButton']['color'],
                                                       gameSettings[State.SCORE]['quitButton']['text'])

        self.canvasWidgets['scoreRestartButton'] = Button(self.canvas,
                                                          102,
                                                          2,
                                                          gameSettings[State.SCORE]['restartButton']['width'],
                                                          gameSettings[State.SCORE]['restartButton']['height'],
                                                          gameSettings[State.SCORE]['restartButton']['border'],
                                                          gameSettings[State.SCORE]['restartButton']['color'],
                                                          gameSettings[State.SCORE]['restartButton']['text'])

        self.canvasWidgets['scoreContinueButton'] = Button(self.canvas,
                                                           202,
                                                           2,
                                                           gameSettings[State.SCORE]['continueButton']['width'],
                                                           gameSettings[State.SCORE]['continueButton']['height'],
                                                           gameSettings[State.SCORE]['continueButton']['border'],
                                                           gameSettings[State.SCORE]['continueButton']['color'],
                                                           gameSettings[State.SCORE]['continueButton']['text'])

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
            elif self.canvasWidgets['pauseRestartButton'].x <= x <= self.canvasWidgets[
                'pauseRestartButton'].x+self.canvasWidgets['pauseRestartButton'].width:
                if self.canvasWidgets['pauseRestartButton'].y <= y <= self.canvasWidgets[
                    'pauseRestartButton'].y+self.canvasWidgets['pauseRestartButton'].height:
                    self.canvas.delete('all')
                    self.score = 0
                    self.scoreLabel.configure(text=self.score)
                    self.state = State.PRE
                    self.preSetup()
            else:
                self.state = State.GAME
                self.canvas.delete(self.canvasWidgets['pauseText'])
                self.canvasWidgets['pauseText'] = None
                self.canvas.delete(self.canvasWidgets['pauseRect'])
                self.canvasWidgets['pauseRect'] = None
                self.canvasWidgets['pauseQuitButton'].remove()
                self.canvasWidgets['pauseQuitButton'] = None
                self.canvasWidgets['pauseRestartButton'].remove()
                self.canvasWidgets['pauseRestartButton'] = None
                self.canvas.update()
                self.loop()
        elif self.state == State.SCORE:
            if self.canvasWidgets['scoreQuitButton'].x <= x <= self.canvasWidgets[
                'scoreQuitButton'].x+self.canvasWidgets['scoreQuitButton'].width:
                if self.canvasWidgets['scoreQuitButton'].y <= y <= self.canvasWidgets[
                    'scoreQuitButton'].y+self.canvasWidgets['scoreQuitButton'].height:
                    self.master.destroy()
            elif self.canvasWidgets['scoreRestartButton'].x <= x <= self.canvasWidgets[
                'scoreRestartButton'].x+self.canvasWidgets['scoreRestartButton'].width:
                if self.canvasWidgets['scoreRestartButton'].y <= y <= self.canvasWidgets[
                    'scoreRestartButton'].y+self.canvasWidgets['scoreRestartButton'].height:
                    self.canvas.delete('all')
                    self.score = 0
                    self.scoreLabel.configure(text=self.score)
                    self.state = State.PRE
                    self.preSetup()
            elif self.canvasWidgets['scoreContinueButton'].x <= x <= self.canvasWidgets[
                'scoreContinueButton'].x+self.canvasWidgets['scoreContinueButton'].width:
                if self.canvasWidgets['scoreContinueButton'].y <= y <= self.canvasWidgets[
                    'scoreContinueButton'].y+self.canvasWidgets['scoreContinueButton'].height:
                    self.state = State.GAME
                    self.canvasWidgets['scoreQuitButton'].remove()
                    self.canvasWidgets['scoreRestartButton'].remove()
                    self.canvasWidgets['scoreContinueButton'].remove()
                    self.canvas.delete(self.canvasWidgets['scoreRect'])
                    self.canvas.delete(self.canvasWidgets['scoreText'])
                    self.loop()

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
        self.canvas.update()

        if self.score > gameSettings['toWin']:
            if not self.WON:
                self.state = State.SCORE
                self.scoreSetup(True)
        if self.score < gameSettings['toLose']:
            if not self.WON:
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

            self.canvas.after(gameSettings[State.GAME]['tickSpeed'], self.loop)
