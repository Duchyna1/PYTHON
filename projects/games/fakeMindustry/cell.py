from projects.games.fakeMindustry.building import building
from projects.games.fakeMindustry.things import Materials, Buildings


class cell:
    def __init__(self, parent, x, y, width, height, material, building = None):
        self.parent = parent
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.material = material
        self.building = building

        if self.material == Materials.STONE:
            self.rec = self.parent.create_rectangle(self.x, self.y, self.x+self.width, self.y+self.height, fill='gray')
        elif self.material == Materials.COAL:
            self.rec = self.parent.create_rectangle(self.x, self.y, self.x+self.width, self.y+self.height, fill='black')
        elif self.material == Materials.IRON:
            self.rec = self.parent.create_rectangle(self.x, self.y, self.x+self.width, self.y+self.height, fill='navajo white')

        if self.building == Buildings.MINE:
            self.setBuilding(Buildings.MINE)

    def setMaterial(self, material):
        self.material = material
        if self.material == Materials.STONE:
            self.parent.itemconfig(self.rec, fill='gray')
        elif self.material == Materials.COAL:
            self.parent.itemconfig(self.rec, fill='black')
        elif self.material == Materials.IRON:
            self.parent.itemconfig(self.rec, fill='navajo white')
        self.parent.update()

    def setBuilding(self, new):
        if new == Buildings.NONE:
            self.building.delete()
            self.building = Buildings.NONE
        elif new == Buildings.MINE:
            self.building = building(self.parent, self.x, self.y, self.width, self.height, Buildings.MINE)
