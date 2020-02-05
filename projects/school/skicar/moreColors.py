class create:
    def __init__(self, x, y, width, height, border, canvas):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border = border
        self.canvas = canvas
        self.canvas.create_rectangle(x, y, x+width, y+height, fill = "gray", width = border)
        self.canvas.create_text(x+width//2, y+height//2, text = "MORE")