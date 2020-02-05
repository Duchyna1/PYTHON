class create:
    def __init__(self, x, y, width, height, color, border, canvas):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.border = border
        self.canvas = canvas
        self.button = self.canvas.create_rectangle(x, y, x+width, y+height, fill = color, width = border)
