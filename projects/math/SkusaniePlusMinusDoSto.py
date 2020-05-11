import tkinter
from random import randint

try:
    file = open("stats.txt", "x")
    file.close()
    file = open("stats.txt, r")
except:
    file = open("stats.txt", "r")
if file.readline() == '':
    file.close()
    file = open("stats.txt", "w")
    file.write("-1 -1 -1 0")
    file.close()
    file = open("stats.txt", "r")
file.close()
file = open("stats.txt", "r")
stats = file.readline()
stats = stats.split(' ')
priklady = int(stats[0])
spravne = int(stats[1])
pokusy = int(stats[2])
preskocenia = int(stats[3])
file.close()

canvas = tkinter.Canvas(width=425, height=150, background="white")
canvas.pack()

textStats = [canvas.create_text(30, 140, text="Príklady: "), canvas.create_text(130, 140, text="Správne: "),
             canvas.create_text(250, 140, text="Pokusy: "), canvas.create_text(350, 140, text="Preskočenia: "),
             canvas.create_text(70, 140, text=priklady), canvas.create_text(170, 140, text=spravne),
             canvas.create_text(290, 140, text=pokusy), canvas.create_text(400, 140, text=preskocenia)]

minus = None

start = [canvas.create_line(425 // 2, 0, 425 // 2, 150, width=10),
         canvas.create_text(425 // 4, 50, text="Príklady\niba na\nPLUS", font=("Arial", 20, "bold")),
         canvas.create_text(425 // 4 * 3, 50, text="Príklady\nja na\nMÍNUS", font=("Arial", 20, "bold"))]


def click(event):
    global minus, start, problem
    x, y, = event.x, event.y
    if None == minus:
        if x < 425 // 2:
            minus = False
        else:
            minus = True
        for thing in start:
            canvas.delete(thing)
            canvas.update()
        start.clear()
        setup()


numbers = [0, 0, 0]
hidden = 0
correct = []
answer = []
sign = None
problem = []


def setup():
    global problem
    problem.append(canvas.create_text(50, 50, text="", font=("Arial", 65, "bold")))
    problem.append(canvas.create_text(120, 50, text="", font=("Arial", 65, "bold")))
    problem.append(canvas.create_text(195, 50, text="", font=("Arial", 65, "bold")))
    problem.append(canvas.create_text(270, 50, text="=", font=("Arial", 65, "bold")))
    problem.append(canvas.create_text(350, 50, text="", font=("Arial", 65, "bold")))
    draw()


def generateProblem():
    global numbers, sign, hidden, correct, priklady
    priklady += 1
    file = open("stats.txt", "w")
    file.write(str(priklady) + ' ' + str(spravne) + ' ' + str(pokusy) + ' ' + str(preskocenia))
    file.close()
    canvas.itemconfig(textStats[4], text = priklady)
    correct = []
    #hidden = randint(0, 7)
    #if hidden > 1:
    #    hidden = 2
    hidden = 2
    if minus:
        x = randint(0, 1)
        if x == 0:
            sign = "-"
        else:
            sign = "+"
    else:
        sign = "+"
    numbers[2] = randint(2, 99)
    if sign == "+":
        numbers[0] = randint(1, numbers[2] - 1)
        numbers[1] = numbers[2] - numbers[0]
    else:
        numbers[0] = randint(numbers[2] + 1, 100)
        numbers[1] = numbers[0] - numbers[2]
    for i in range(len(str(numbers[hidden]))):
        correct.append(str(numbers[hidden])[i])
    numbers[hidden] = ''


def draw(event=None):
    global problem, answer, pokusy, spravne
    pokusy += 1
    file = open("stats.txt", "w")
    file.write(str(priklady) + ' ' + str(spravne) + ' ' + str(pokusy) + ' ' + str(preskocenia))
    file.close()
    canvas.itemconfig(textStats[6], text = pokusy)
    if answer == correct:
        spravne += 1
        file = open("stats.txt", "w")
        file.write(str(priklady) + ' ' + str(spravne) + ' ' + str(pokusy) + ' ' + str(preskocenia))
        file.close()
        canvas.itemconfig(textStats[5], text = spravne)
        drawProblem()
    else:
        numbers[hidden] = ''
        if hidden == 0:
            canvas.itemconfig(problem[0], text='', font=("Arial", 65))
        if hidden == 1:
            canvas.itemconfig(problem[2], text='', font=("Arial", 65))
        if hidden == 2:
            canvas.itemconfig([problem[4]], text='', font=("Arial", 65))


def redraw(number):
    global numbers, hidden, answer, problem
    if number == "-":
        if len(numbers[hidden]) == 1:
            numbers[hidden] = ''
        elif len(numbers[hidden]) > 1:
            numbers[hidden] = str(numbers[hidden][:-1])
    else:
        numbers[hidden] = numbers[hidden] + number
    answer = []
    for i in range(len(str(numbers[hidden]))):
        answer.append(str(numbers[hidden])[i])
    if hidden == 0:
        canvas.itemconfig(problem[0], text=str(numbers[hidden]), font=("Arial", 65))
    if hidden == 1:
        canvas.itemconfig(problem[2], text=str(numbers[hidden]), font=("Arial", 65))
    if hidden == 2:
        canvas.itemconfig(problem[4], text=str(numbers[hidden]), font=("Arial", 65))


def drawProblem(event=None):
    generateProblem()
    canvas.itemconfig(problem[0], text=numbers[0], font=("Arial", 65, "bold"))
    canvas.itemconfig(problem[2], text=numbers[1], font=("Arial", 65, "bold"))
    canvas.itemconfig(problem[4], text=numbers[2], font=("Arial", 65, "bold"))
    canvas.itemconfig(problem[1], text=sign)


def one(event=None):
    redraw("1")


def two(event=None):
    redraw("2")


def three(event=None):
    redraw("3")


def four(event=None):
    redraw("4")


def five(event=None):
    redraw("5")


def six(event=None):
    redraw("6")


def seven(event=None):
    redraw("7")


def eight(event=None):
    redraw("8")


def nine(event=None):
    redraw("9")


def zero(event=None):
    redraw("0")


def back(event=None):
    redraw("-")

def skip(event = None):
    global preskocenia
    preskocenia += 1
    file = open("stats.txt", "w")
    file.write(str(priklady) + ' ' + str(spravne) + ' ' + str(pokusy) + ' ' + str(preskocenia))
    file.close()
    canvas.itemconfig(textStats[7], text = preskocenia)
    drawProblem()

canvas.bind_all("<Return>", draw)
canvas.bind('<ButtonPress>', click)
canvas.bind_all('1', one)
canvas.bind_all('2', two)
canvas.bind_all('3', three)
canvas.bind_all('4', four)
canvas.bind_all('5', five)
canvas.bind_all('6', six)
canvas.bind_all('7', seven)
canvas.bind_all('8', eight)
canvas.bind_all('9', nine)
canvas.bind_all('0', zero)
canvas.bind_all('s', skip)
canvas.bind_all("<BackSpace>", back)

canvas.mainloop()
