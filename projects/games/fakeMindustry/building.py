class building:
    def __init__(self, parent, x, y, width, height, type):
        self.parent = parent
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.type = type
        if self.type == "mine":
            self.building = self.parent.create_text(self.x+self.width//2, self.y+self.height//2, text='T')
            self.parent.update()

    def delete(self):
        self.parent.delete(self.building)
        self.parent.update()
