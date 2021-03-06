class create:
    def __init__(self, x, y, width, height, border, canvas, mode):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border = border
        self.canvas = canvas
        self.mode = mode
        self.button = self.canvas.create_rectangle(x, y, x+width, y+height, fill = "gray", width = border)
        if self.mode == "LINE":
            self.line()
        if self.mode == "CIRCLE":
            self.circle()
        if self.mode == "SQUARE":
            self.square()
        if self.mode == "HOUSE":
            self.house()
        if self.mode == "FLOWER":
            self.flower()

    def line(self):
        self.canvas.create_line(self.x+self.width/100*80, self.y+self.height/100*20, self.x+self.width/100*20, self.y+self.height/100*80, fill = "black", width = self.width//4)

    def circle(self):
        self.canvas.create_oval(self.x+self.width/100*20, self.y+self.height/100*20, self.x+self.width/100*80, self.y+self.height/100*80, fill = "black")

    def square(self):
        self.canvas.create_rectangle(self.x+self.width/100*20, self.y+self.height/100*20, self.x+self.width/100*80, self.y+self.height/100*80, fill = "black")

    def house(self):
        self.canvas.create_rectangle(self.x+self.width/100*20, self.y+self.height/100*40, self.x+self.width/100*80, self.y+self.height/100*80, fill = "red", width = 0)
        self.canvas.create_polygon(self.x+self.width/100*20, self.y+self.height/100*40, self.x+self.width/100*80, self.y+self.height/100*40, self.x+self.height/100*50, self.y+self.height/100*20, fill = "brown", width = 0)

    def flower(self):
        self.canvas.create_oval(self.x+self.width/100*20, self.y+self.height/100*20, self.x+self.width/100*50, self.y+self.height/100*50, fill = "red", width = 0)
        self.canvas.create_oval(self.x+self.width/100*20, self.y+self.height/100*80, self.x+self.width/100*50, self.y+self.height/100*50, fill = "red", width = 0)
        self.canvas.create_oval(self.x+self.width/100*80, self.y+self.height/100*20, self.x+self.width/100*50, self.y+self.height/100*50, fill = "red", width = 0)
        self.canvas.create_oval(self.x+self.width/100*80, self.y+self.height/100*80, self.x+self.width/100*50, self.y+self.height/100*50, fill = "red", width = 0)
        self.canvas.create_oval(self.x+self.width/100*35, self.y+self.height/100*35, self.x+self.width/100*65, self.y+self.height/100*65, fill = "yellow", width = 0)