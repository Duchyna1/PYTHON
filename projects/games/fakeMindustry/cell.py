from projects.games.fakeMindustry.building import building
from projects.games.fakeMindustry.things import Materials, Buildings


class cell:
    def __init__(self, parent, x, y, width, height, material = None, building = None):
        self.parent = parent
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.material = material
        self.building = building

        for m in Materials.all:
            if m == material:
                self.rec = self.parent.create_rectangle(self.x, self.y, self.x+self.width, self.y+self.height, fill=Materials.colors[m])
                break

        if building is None:
            pass
        else:
            for b in Buildings.all:
                if b == building:
                    self.setBuilding(b)
                    break

    def setMaterial(self, material):
        self.material = material
        for m in Materials.all:
            if material == m:
                self.rec = self.parent.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height,
                                                    fill=Materials.colors[m])
                break
        self.parent.update()

    def setBuilding(self, new):
        if new is None:
            self.building.delete()
            self.building = None
        else:
            self.building = building(self.parent, self.x, self.y, self.width, self.height, new)
