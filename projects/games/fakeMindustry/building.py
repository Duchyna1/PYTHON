from projects.games.fakeMindustry.things import Stats

class building:
    def __init__(self, parent, x, y, width, height, type, under, level=0):
        self.parent = parent
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.type = type
        self.under = under
        self.inventory = 0
        self.level = level
        if self.type == "mine":
            self.building = [
                self.parent.create_rectangle(self.x+self.width*0.25, self.y, self.x+self.width*0.75, self.y+self.height,
                                             fill='gray', width=0),
                self.parent.create_rectangle(self.x, self.y+self.height*0.25, self.x+self.width,
                                             self.y+self.height*0.75, fill='gray', width=0)
            ]

    def delete(self):
        for b in self.building:
            self.parent.delete(b)

    def action(self, ticks):
        if ticks % Stats.MINE['speed'][self.level] == 0:
            self.inventory += 1
