from projects.games.fakeMindustry.building import building
from projects.games.fakeMindustry.conveyor import conveyor
from projects.games.fakeMindustry.things import Materials, Buildings


class cell:
    def __init__(self, parent, x, y, width, height, material, orientation=0, b=None, level=0):
        self.parent = parent
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.material = material
        self.building = b
        self.orientation = orientation
        self.level = level
        self.rec = self.parent.create_rectangle(self.x, self.y, self.x+self.width, self.y+self.height,
                                                fill=Materials.colors[self.material])
        if building is None:
            pass
        else:
            self.setBuilding(self.building, level=self.level)

    def setMaterial(self, material):
        self.material = material
        self.rec = self.parent.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height,
                                                fill=Materials.colors[self.material])

    def setBuilding(self, new, level=0, orientation=0):
        self.orientation = orientation
        self.level = level
        if new is None:
            if self.building is None:
                self.building = building(self.parent, self.x, self.y, self.width, self.height, Buildings.MINE,
                                         self.material, level=self.level)
            self.building.delete()
            self.building = None
        elif new == Buildings.CONVEYOR:
            self.building = conveyor(self.parent, self.x, self.y, self.width, self.height, self.orientation,
                                     level=self.level)
        else:
            self.building = building(self.parent, self.x, self.y, self.width, self.height, new, self.material,
                                     level=self.level)
