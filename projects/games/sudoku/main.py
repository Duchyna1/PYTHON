from sudoku_maker import *
from sudoku_solver import *
import tkinter

width = 50

numbers = []
cells = []

game = tkinter.Canvas(width=width*9, height=width*9)
game.pack()


def draw_border():
    global width
    for x in range(11):
        if x == 0 or x == 3 or x == 6 or x == 10:
            game.create_line(x*width, 0, x*width, width*9, width=5)
            game.create_line(0, x*width, 9*width, x*width, width=5)
        else:
            game.create_line(x*width, 0, x*width, width*9, width=2)
            game.create_line(0, x*width, 9*width, x*width, width=2)


class cell:
    def __init__(self, x, y, width, number='', select=False, border=3):
        if number == 0:
            self.original = False
            number = ''
        else:
            self.original = True
        self.x = x
        self.y = y
        self.width = width
        self.number = number
        self.select = select
        self.bg = game.create_rectangle(x*width, y*width, x*width+width, y*width+width, fill='lightgray', width=0)
        self.num_dis = game.create_text(x*width+width//2, y*width+width//2, text=number, fill='black', font=(f'Aerial {int(width*0.6)} bold'))

    def sel(self):
        for x in range(9):
            for y in range(9):
                cells[x][y].select = False
                game.itemconfig(cells[x][y].bg, fill='lightgray')
        self.select = True
        game.itemconfig(self.bg, fill='gray')


def setup(event=None):
    global cells, width, numbers
    for x in range(9):
        row_num = []
        for y in range(9):
            row_num.append(0)
        numbers.append(row_num)
    make(numbers)
    # solve(numbers)
    for x in range(9):
        row = []
        for y in range(9):
            row.append(cell(x, y, width, number=numbers[x][y]))
        cells.append(row)
    draw_border()
    game.update()


def slct(event):
    global width
    x, y = event.x//width, event.y//width
    if not cells[x][y].original:
        cells[x][y].sel()


def one(event=None):
    for x in range(9):
        for y in range(9):
            if cells[x][y].select:
                game.itemconfig(cells[x][y].num_dis, text='1', font=(f'Aerial {int(width*0.6)}'))
                cells[x][y].number = 1
                check(x, y)


def two(event=None):
    for x in range(9):
        for y in range(9):
            if cells[x][y].select:
                game.itemconfig(cells[x][y].num_dis, text='2', font=(f'Aerial {int(width*0.6)}'))
                cells[x][y].number = 2
                check(x, y)


def three(event=None):
    for x in range(9):
        for y in range(9):
            if cells[x][y].select:
                game.itemconfig(cells[x][y].num_dis, text='3', font=(f'Aerial {int(width*0.6)}'))
                cells[x][y].number = 3
                check(x, y)


def four(event=None):
    for x in range(9):
        for y in range(9):
            if cells[x][y].select:
                game.itemconfig(cells[x][y].num_dis, text='4', font=(f'Aerial {int(width*0.6)}'))
                cells[x][y].number = 4
                check(x, y)


def five(event=None):
    for x in range(9):
        for y in range(9):
            if cells[x][y].select:
                game.itemconfig(cells[x][y].num_dis, text='5', font=(f'Aerial {int(width*0.6)}'))
                cells[x][y].number = 5
                check(x, y)


def six(event=None):
    for x in range(9):
        for y in range(9):
            if cells[x][y].select:
                game.itemconfig(cells[x][y].num_dis, text='6', font=(f'Aerial {int(width*0.6)}'))
                cells[x][y].number = 6
                check(x, y)


def seven(event=None):
    for x in range(9):
        for y in range(9):
            if cells[x][y].select:
                game.itemconfig(cells[x][y].num_dis, text='7', font=(f'Aerial {int(width*0.6)}'))
                cells[x][y].number = 7
                check(x, y)


def eight(event=None):
    for x in range(9):
        for y in range(9):
            if cells[x][y].select:
                game.itemconfig(cells[x][y].num_dis, text='8', font=(f'Aerial {int(width*0.6)}'))
                cells[x][y].number = 8
                check(x, y)


def nine(event=None):
    for x in range(9):
        for y in range(9):
            if cells[x][y].select:
                game.itemconfig(cells[x][y].num_dis, text='9', font=(f'Aerial {int(width*0.6)}'))
                cells[x][y].number = 9
                check(x, y)


def delete(event=None):
    for x in range(9):
        for y in range(9):
            if cells[x][y].select:
                game.itemconfig(cells[x][y].num_dis, text='', font=(f'Aerial {int(width*0.6)}'))
                cells[x][y].number = ''


def help(event):
    solve(numbers)


def red(x, y, what):
    for xx in range(9):
        for yy in range(9):
            if not cells[xx][yy].select:
                game.itemconfig(cells[xx][yy].bg, fill='lightgray')
    if what == 'row':
        for xx in range(9):
            game.itemconfig(cells[xx][y].bg, fill='red')
    if what == 'col':
        for yy in range(9):
            game.itemconfig(cells[x][yy].bg, fill='red')
    if what == 'square':
        for plusx in range(3):
            for plusy in range(3):
                game.itemconfig(cells[x+plusx][y+plusy].bg, fill='red')


def check(x, y):
    for xx in range(9):
        if not cells[xx][y].select:
            if cells[xx][y].number == cells[x][y].number:
                red(x, y, 'row')
    for yy in range(9):
        if not cells[x][yy].select:
            if cells[x][yy].number == cells[x][y].number:
                red(x, y, 'col')
    xx = x//3*3
    yy = y//3*3
    for plusx in range(3):
        for plusy in range(3):
            if not cells[xx+plusx][yy+plusy].select:
                if cells[x][y].number == cells[xx+plusx][yy+plusy].number:
                    red(xx, yy, 'square')


setup()
game.bind('<ButtonPress>', slct)
game.bind_all('1', one)
game.bind_all('2', two)
game.bind_all('3', three)
game.bind_all('4', four)
game.bind_all('5', five)
game.bind_all('6', six)
game.bind_all('7', seven)
game.bind_all('8', eight)
game.bind_all('9', nine)
game.bind_all('0', delete)
game.bind_all('h', help)
game.mainloop()
