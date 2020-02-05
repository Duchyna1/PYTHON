import tkinter
from random import randint


class create:
    def __init__(self, x, y, width, height, activColor, bgColor, min, max, cur, bgBorder, border, canvas, mode):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.activeColor = activColor
        self.bgColor = bgColor
        self.min = min
        self.max = max
        self.cur = cur
        self.canvas = canvas
        self.bgBorder = bgBorder
        self.border = border
        self.bg = self.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height,
                                               fill=self.bgColor, width=self.bgBorder)
        self.slider = self.canvas.create_rectangle(self.x + self.bgBorder, self.y + self.bgBorder, self.x + self.getX(),
                                                   self.y + self.height, fill=self.activeColor, width=self.border)
        self.mode = mode

    def getX(self):
        percent = (self.cur - self.min) / (self.max - self.min)
        return self.width * percent

    def getCur(self, step):
        percent = (self.getX() + step) / self.width
        return (self.max - self.min) * percent + self.min

    def move(self, x):
        step = x - (self.x + self.getX())
        self.cur = self.getCur(step)
        if self.mode == 'r':
            try:
                self.activeColor = f'#{int(self.cur):02x}0000'
            except:
                pass
        elif self.mode == 'g':
            try:
                self.activeColor = f'#00{int(self.cur):02x}00'
            except:
                pass
        elif self.mode == 'b':
            try:
                self.activeColor = f'#0000{int(self.cur):02x}'
            except:
                pass
        self.canvas.delete(self.slider)
        self.slider = None
        self.slider = self.canvas.create_rectangle(self.x + self.bgBorder, self.y + self.bgBorder, self.x + self.getX(),
                                                   self.y + self.height, fill=self.activeColor, width=self.border)
        self.canvas.update()


canvas = tkinter.Canvas(width=1500, height=600)
canvas.pack()

sliders = []

rec = canvas.create_rectangle(0, 30, 1500, 700, fill='white')

sliders.append(create(0, 0, 1500, 20, 'red', 'white', 0, 256, 10, 0, 0, canvas, 'r'))
sliders.append(create(0, 20, 1500, 20, 'green', 'white', 0, 256, 10, 0, 0, canvas, 'g'))
sliders.append(create(0, 40, 1500, 20, 'blue', 'white', 0, 256, 10, 0, 0, canvas, 'b'))


def drag(event):
    x, y = event.x, event.y
    for slider in sliders:
        if (slider.x < x < slider.x + slider.width) and (slider.y < y < slider.y + slider.height):
            slider.move(x)
            canvas.itemconfig(rec, fill=f'#{int(sliders[0].cur):02x}{int(sliders[1].cur):02x}{int(sliders[2].cur):02x}')
            print(slider.cur, slider.mode)


smerR = 1
speedR = randint(1, 5)
smerG = 1
speedG = randint(1, 5)
smerB = 1
speedB = randint(1, 5)


def start(event=None):
    global smerB, smerG, smerR, speedB, speedG, speedR
    sliders[0].move(sliders[0].getX() + 1 * smerR * speedR)
    sliders[1].move(sliders[1].getX() + 1 * smerG * speedG)
    sliders[2].move(sliders[2].getX() + 1 * smerB * speedB)

    if (int(sliders[0].cur) >= 251) or (int(sliders[0].cur) <= 4):
        smerR *= -1
        speedR = randint(1, 5)
        if int(sliders[0].cur) > 200:
            sliders[0].cur = 250
        else:
            sliders[0].cur = 5
    if (int(sliders[1].cur) >= 251) or (int(sliders[1].cur) <= 4):
        smerG *= -1
        speedG = randint(1, 5)
        if int(sliders[1].cur) > 200:
            sliders[1].cur = 250
        else:
            sliders[1].cur = 5
    if (int(sliders[2].cur) >= 251) or (int(sliders[2].cur) <= 4):
        smerB *= -1
        speedB = randint(1, 5)
        if int(sliders[2].cur) > 200:
            sliders[2].cur = 250
        else:
            sliders[2].cur = 5
    canvas.itemconfig(rec, fill=f'#{int(sliders[0].cur):02x}{int(sliders[1].cur):02x}{int(sliders[2].cur):02x}')
    canvas.update()
    canvas.after(1, start)


# start()

canvas.bind_all("<B1-Motion>", drag)

canvas.mainloop()
