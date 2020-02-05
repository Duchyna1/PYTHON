class create:
    def __init__(self, x, y, width, height, activColor, bgColor, min, max, cur, bgBorder, border, canvas):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.activColor = activColor
        self.bgColor = bgColor
        self.min = min
        self.max = max
        self.cur = cur
        self.canvas = canvas
        self.bgBorder = bgBorder
        self.border = border
        self.bg = self.canvas.create_rectangle(self.x, self.y, self.x+self.width, self.y+self.height, fill = self.bgColor, width = self.bgBorder)
        self.slider = self.canvas.create_rectangle(self.x+self.bgBorder, self.y+self.bgBorder, self.x+self.getX(), self.y+self.height, fill = self.activColor, width = self.border)

    def getX(self):
        percent = (self.cur-self.min)/(self.max-self.min)
        return self.width*percent

    def getCur(self, step):
        percent = (self.getX()+step)/self.width
        return (self.max-self.min)*percent+self.min

    def move(self, x):
        step = x-(self.x+self.getX())
        self.cur = self.getCur(step)
        self.canvas.delete(self.slider)
        self.slider = None
        self.slider = self.canvas.create_rectangle(self.x+self.bgBorder, self.y+self.bgBorder, self.x+self.getX(), self.y+self.height, fill = self.activColor, width = self.border)
        self.canvas.update()