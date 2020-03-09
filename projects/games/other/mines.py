import tkinter, sys
from random import randrange

sys.setrecursionlimit(1000000000)

widthX = input('Sirka: ')
if widthX == '':
    width = 20
else:
    width = int(widthX)
heightX = input('Vyska: ')
if heightX == '':

    height = 20
else:
    height = int(heightX)
width_polickoX = input('Sirka policka: ')
if width_polickoX == '':
    width_policko = 25
else:
    width_policko = int(width_polickoX)
pocet_minX = input('Pocet min: ')
if pocet_minX == '':
    pocet_min = 40
else:
    pocet_min = int(pocet_minX)

game = tkinter.Canvas(height=width_policko*height, width=width_policko*width, background='#484848')
game.pack()


class policko:
    def __init__(self, x, y, stav, cislo):
        self.x = x
        self.y = y
        self.stav = stav
        self.cislo = cislo
        game.create_rectangle(x*width_policko+width_policko*0.02, y*width_policko+width_policko*0.02, x*width_policko+width_policko*0.98, y*width_policko+width_policko*0.98, fill = 'gray', width = 0)

    def color(self):
        if self.cislo == 1:
            return 'blue'
        if self.cislo == 2:
            return 'green'
        if self.cislo == 3:
            return 'red2'
        if self.cislo == 4:
            return 'darkblue'
        if self.cislo == 5:
            return 'red3'
        if self.cislo == 6:
            return 'deepskyblue'
        if self.cislo == 7:
            return 'brown4'
        if self.cislo == 8:
            return 'gray'

    def okolo(self):
        if self.x != -1 and self.y != -1:
            if mriezka[self.x-1][self.y-1].stav == 0:
                select(self.x-1, self.y-1)
        if self.y != -1:
            if mriezka[self.x][self.y-1].stav == 0:
                select(self.x, self.y-1)
        if self.x+1 != width and self.y-1 != -1:
            if mriezka[self.x+1][self.y-1].stav == 0:
                select(self.x+1, self.y-1)
        if self.x-1 != -1:
            if mriezka[self.x-1][self.y].stav == 0:
                select(self.x-1, self.y)
        if self.x+1 != width:
            if mriezka[self.x+1][self.y].stav == 0:
                select(self.x+1, self.y)
        if self.x-1 != -1 and self.y+1 != height:
            if mriezka[self.x-1][self.y+1].stav == 0:
                select(self.x-1, self.y+1)
        if self.y+1 != height:
            if mriezka[self.x][self.y+1].stav == 0:
                select(self.x, self.y+1)
        if self.x+1 != width and self.y+1 != height:
            if mriezka[self.x+1][self.y+1].stav == 0:
                select(self.x+1, self.y+1)

    def draw_flag(self, x, y):
        x *= width_policko
        y *= width_policko
        game.create_line(x+width_policko*0.34, y+width_policko*0.2, x+width_policko*0.34, y+width_policko*0.8, fill = 'black', width = width_policko*0.08)
        game.create_polygon(x+width_policko*0.36, y+width_policko*0.2, x+width_policko*0.36, y+width_policko*0.6, x+width_policko*0.7, y+width_policko*0.4, fill='red', width = 0)

    def draw_mine(self, x, y):
        x *= width_policko
        y *= width_policko
        game.create_oval(x+width_policko*0.3, y+width_policko*0.3, x+width_policko*0.7, y+width_policko*0.7, fill = 'black')
        game.create_line(x+width_policko*0.28, y+width_policko*0.28, x+width_policko*0.72, y+width_policko*0.72, fill = 'black', width = width_policko*0.08)
        game.create_line(x+width_policko*0.72, y+width_policko*0.28, x+width_policko*0.28, y+width_policko*0.72, fill = 'black', width = width_policko*0.08)

    def vykresli(self, n):
        if n == 1:
            if self.cislo == 99:
                game.create_rectangle(self.x*width_policko+width_policko*0.02, self.y*width_policko+width_policko*0.02, self.x*width_policko+width_policko*0.98, self.y*width_policko+width_policko*0.98, fill = 'red', width = 0)
                self.draw_mine(self.x, self.y)
                game_over()
                game.after(1000, reset)
            elif self.cislo == 0:
                game.create_rectangle(self.x*width_policko+width_policko*0.02, self.y*width_policko+width_policko*0.02, self.x*width_policko+width_policko*0.98, self.y*width_policko+width_policko*0.98, fill = 'lightgray', width = 0)
                if self.x-1 != -1 and self.y-1 != -1:
                    if mriezka[self.x-1][self.y-1].stav == 0:
                        select(self.x-1, self.y-1)
                if self.y-1 != -1:
                    if mriezka[self.x][self.y-1].stav == 0:
                        select(self.x, self.y-1)
                if self.x+1 != width and self.y-1 != -1:
                    if mriezka[self.x+1][self.y-1].stav == 0:
                        select(self.x+1, self.y-1)
                if self.x-1 != -1:
                    if mriezka[self.x-1][self.y].stav == 0:
                        select(self.x-1, self.y)
                if self.x+1 != width:
                    if mriezka[self.x+1][self.y].stav == 0:
                        select(self.x+1, self.y)
                if self.x-1 != -1 and self.y+1 != height:
                    if mriezka[self.x-1][self.y+1].stav == 0:
                        select(self.x-1, self.y+1)
                if self.y+1 != height:
                    if mriezka[self.x][self.y+1].stav == 0:
                        select(self.x, self.y+1)
                if self.x+1 != width and self.y+1 != height:
                    if mriezka[self.x+1][self.y+1].stav == 0:
                        select(self.x+1, self.y+1)
            else:
                game.create_rectangle(self.x*width_policko+width_policko*0.02, self.y*width_policko+width_policko*0.02, self.x*width_policko+width_policko*0.98, self.y*width_policko+width_policko*0.98, fill = 'lightgray', width = 0)
                game.create_text(self.x*width_policko+width_policko*0.5, self.y*width_policko+width_policko*0.5, text = self.cislo, fill = self.color(), font = ('Aerial', int(width_policko*0.6)))
        if n == 2:
            self.draw_flag(self.x, self.y)
        if n == 0:
            game.create_rectangle(self.x*width_policko+width_policko*0.02, self.y*width_policko+width_policko*0.02, self.x*width_policko+width_policko*0.98, self.y*width_policko+width_policko*0.98, fill = 'gray', width = 0)
    
    def click(self, event):
        if event == 'lc':
            if self.stav == 1:
                self.okolo()
        if event == 'lc':
            if self.stav == 0:
                self.stav = 1
        if event == 'rc':
            if self.stav == 0:
                self.stav = 2
            elif self.stav == 2:
                self.stav = 0
        self.vykresli(self.stav)

    def nastav(self):
        if self.cislo == 99:
            return False
        else:
            self.cislo = 99
            return True

def stlacselect(event):
    x, y = event.x//width_policko, event.y//width_policko
    mriezka[x][y].click('lc')

def select(x, y):
    mriezka[x][y].click('lc')

def flag(event): 
    x, y = event.x//width_policko, event.y//width_policko
    mriezka[x][y].click('rc')

mriezka = []
def setup():
    global mriezka
    mriezka = []
    for i in range(width):
        riadok = []
        for l in range(height):
            riadok.append(policko(i, l, 0, 0))
        mriezka.append(riadok)

    aktualny_pocet_min = 0
    while aktualny_pocet_min < pocet_min:
        if mriezka[randrange(width)][randrange(height)].nastav():
            aktualny_pocet_min += 1
    for x in range(width):
        for y in range(height):
            if mriezka[x][y].cislo == 99:
                if x-1 != -1 and y-1 != -1:
                    if mriezka[x-1][y-1].cislo != 99:
                        mriezka[x-1][y-1].cislo += 1
                if y-1 != -1:
                    if mriezka[x][y-1].cislo != 99:
                        mriezka[x][y-1].cislo += 1
                if x+1 != width and y-1 != -1:
                    if mriezka[x+1][y-1].cislo != 99:
                        mriezka[x+1][y-1].cislo += 1
                if x-1 != -1:
                    if mriezka[x-1][y].cislo != 99:
                        mriezka[x-1][y].cislo += 1
                if x+1 != width:
                    if mriezka[x+1][y].cislo != 99:
                        mriezka[x+1][y].cislo += 1
                if x-1 != -1 and y+1 != height:
                    if mriezka[x-1][y+1].cislo != 99:
                        mriezka[x-1][y+1].cislo += 1
                if y+1 != height:
                    if mriezka[x][y+1].cislo != 99:
                        mriezka[x][y+1].cislo += 1
                if x+1 != width and y+1 != height:
                    if mriezka[x+1][y+1].cislo != 99:
                        mriezka[x+1][y+1].cislo += 1

def reset(event=None):
    game.delete('all')
    setup()

def help(event=None):
    for x in range(width):
        for y in range(height):
            if mriezka[x][y].cislo == 99:
                if mriezka[x][y].stav == 0:
                    mriezka[x][y].click('rc')

def setings(event=None):
    global width, height, width_policko, pocet_min
    print()
    print()
    print('Nove nastavenia:')
    widthX = input('Sirka: ')
    if widthX == '':
        width = 20
    else:
        width = int(widthX)
    heightX = input('Vyska: ')
    if heightX == '':
        height = 20
    else:
        height = int(heightX)
    width_polickoX = input('Sirka policka: ')
    if width_polickoX == '':
        width_policko = 25
    else:
        width_policko = int(width_polickoX)
    pocet_minX = input('Pocet min: ')
    if pocet_minX == '':
        pocet_min = 40
    else:
        pocet_min = int(pocet_minX)
    reset()

def game_over():
    for x in range(width):
        for y in range(height):
            if mriezka[x][y].stav == 0:
                if mriezka[x][y].cislo == 99:
                    select(x, y)

def fast(event):
    for x in range(width):
        for y in range(height):
            if mriezka[x][y].cislo == 99:
                if mriezka[x][y].stav == 0:
                    mriezka[x][y].click('rc')
    for x in range(width):
        for y in range(height):
            if mriezka[x][y].stav == 0:
                mriezka[x][y].click('lc')

setup()
game.bind('<ButtonPress>', stlacselect)
game.bind('<Button-3>', flag)
game.bind_all('r', reset)
game.bind_all('h', help)
game.bind_all('s', setings)
game.bind_all('f', fast)

game.mainloop() 
