import tkinter
from random import randrange

sirka, vyska, sirka_policka = 50, 50, 10

window = tkinter.Canvas(height = vyska*sirka_policka, width = sirka*sirka_policka)
window.pack()

class policko():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.black = False
        window.create_rectangle(self.x*sirka_policka, self.y*sirka_policka, self.x*sirka_policka+sirka_policka, self.y*sirka_policka+sirka_policka, fill = 'white', width = 0)

    def zmena(self):
        window.delete(policka[self.x][self.y])
        if self.black == True:
            self.black = False
            window.create_rectangle(self.x*sirka_policka, self.y*sirka_policka, self.x*sirka_policka+sirka_policka, self.y*sirka_policka+sirka_policka, fill = 'white', width = 0)
        else:
            self.black = True
            window.create_rectangle(self.x*sirka_policka, self.y*sirka_policka, self.x*sirka_policka+sirka_policka, self.y*sirka_policka+sirka_policka, fill = 'black', width = 0)
        
policka = []
def reset(event=None):
    global policka
    policka = []
    for x in range(sirka):
        riadok = []
        for y in range(vyska):
            riadok.append(policko(x, y))
        policka.append(riadok)

def zmen(event):
    x, y = event.x//sirka_policka, event.y//sirka_policka
    policka[x][y].zmena()

      #sever = 1
#zapad = 4     vycohd = 2
      #juh = 3
posx, posy = sirka//2, vyska//2
dire = 1
def start(event=None):
    global posx, posy, dire
    policka[posx][posy].zmena()
    if dire == 1:
        posy -= 1
        if posx < 0: 
            posx = sirka-1
        if posy < 0:
            posy = vyska-1
        if posx >= sirka:
            posx = 0
        if posy >= vyska:
            posy = 0
        if policka[posx][posy].black == True:
            dire = 4
        elif policka[posx][posy].black == False:
            dire = 2
    elif dire == 2:
        posx += 1
        if posx < 0: 
            posx = sirka-1
        if posy < 0:
            posy = vyska-1
        if posx >= sirka:
            posx = 0
        if posy >= vyska:
            posy = 0
        if policka[posx][posy].black == True:
            dire = 1
        elif policka[posx][posy].black == False:
            dire = 3
    elif dire == 3:
        posy += 1
        if posx < 0: 
            posx = sirka-1
        if posy < 0:
            posy = vyska-1
        if posx >= sirka:
            posx = 0
        if posy >= vyska:
            posy = 0
        if policka[posx][posy].black == True:
            dire = 2
        elif policka[posx][posy].black == False:
            dire = 4
    elif dire == 4:
        posx -= 1
        if posx < 0: 
            posx = sirka-1
        if posy < 0:
            posy = vyska-1
        if posx >= sirka:
            posx = 0
        if posy >= vyska:
            posy = 0
        if policka[posx][posy].black == True:
            dire = 3
        elif policka[posx][posy].black == False:
            dire = 1
    window.create_rectangle(posx*sirka_policka, posy*sirka_policka, posx*sirka_policka+sirka_policka, posy*sirka_policka+sirka_policka, fill = 'yellow', width = 0)        
    window.after(10, start)

reset()
window.bind('<ButtonPress>', zmen)
window.bind_all('s', start)
window.bind_all('r', reset)


window.mainloop()
