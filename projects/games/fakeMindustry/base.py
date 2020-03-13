from projects.games.fakeMindustry.things import Stats, Buildings

class base:
    def __init__(self, parent, x, y, width, height):
        self.parent = parent
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.building = [
            self.parent.create_rectangle(self.x, self.y, self.x+self.width, self.y+self.height, width=0,
                                         fill='dark orange'),
            self.parent.create_rectangle(self.x+self.width*0.2, self.y+self.height*0.2,
                                         self.x+self.width*0.8, self.y+self.height*0.8, width=0,
                                         fill='dark gray'),
            self.parent.create_rectangle(self.x+self.width*0.4, self.y+self.height*0.4,
                                         self.x+self.width*0.6, self.y+self.height*0.6, width=0,
                                         fill='dark orange')
        ]

    def delete(self):
        for b in self.building:
            self.parent.delete(b)

    def action(self, ticks):
        pass
