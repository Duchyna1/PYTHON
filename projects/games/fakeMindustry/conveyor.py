from projects.games.fakeMindustry.things import Stats, Buildings

class conveyor:
    def __init__(self, parent, x, y, width, height, orientation, level=0):
        self.parent = parent
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.orientation = orientation
        self.level = level
        self.type = Buildings.CONVEYOR
        self.building = [
            self.parent.create_rectangle(self.x, self.y, self.x+self.width, self.y+self.height, width=0,
                                         fill='dark gray'),
            self.ball(self.orientation)
        ]

    def ball(self, where):
        if where == 0:
            return self.parent.create_rectangle(self.x+self.width*0.4, self.y, self.x+self.width*0.6,
                                                self.y+self.height*0.5, width=0,
                                                fill=Stats.CONVEYOR['color'][self.level])
        elif where == 1:
            return self.parent.create_rectangle(self.x+self.width*0.5, self.y+self.height*0.4, self.x+self.width,
                                                self.y+self.height*0.6, width=0,
                                                fill=Stats.CONVEYOR['color'][self.level])
        elif where == 2:
            return self.parent.create_rectangle(self.x+self.width*0.4, self.y+self.height*0.5, self.x+self.width*0.6,
                                                self.y+self.height, width=0,
                                                fill=Stats.CONVEYOR['color'][self.level])
        elif where == 3:
            return self.parent.create_rectangle(self.x, self.y+self.height*0.4, self.x+self.width*0.5,
                                                self.y+self.height*0.6, width=0,
                                                fill=Stats.CONVEYOR['color'][self.level])

    def setOrientation(self, where):
        self.parent.delete(self.building[1])
        self.ball(where)
        self.orientation = where

    def action(self, ticks):
        pass

    def delete(self):
        for b in self.building:
            self.parent.delete(b)
