import tkinter
from random import randint

canvas = tkinter.Canvas(width = 425, height = 100, background = "white")
canvas.pack()

minus = True
numbers = []
numbers.append(0)
numbers.append(0)
numbers.append(0)
hidden = 1
correct = []
answer = []
sign = None
text0 = canvas.create_text(50, 50, text = "", font = ("Arial", 65, "bold"))
textSign = canvas.create_text(120, 50, text = "", font = ("Arial", 65, "bold"))
text1 = canvas.create_text(195, 50, text = "", font = ("Arial", 65, "bold"))
textEquals = canvas.create_text(270, 50, text = "=", font = ("Arial", 65, "bold"))
text2 = canvas.create_text(350, 50, text = "", font = ("Arial", 65, "bold"))

def generateProblem():
    global numbers, sign, hidden, correct
    correct = []
    hidden = randint(0, 7)
    if hidden > 1:
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
        numbers[0] = randint(1, numbers[2]-1)
        numbers[1] = numbers[2]-numbers[0]
    else:
        numbers[0] = randint(numbers[2]+1, 100)
        numbers[1] = numbers[0]-numbers[2]
    for i in range(len(str(numbers[hidden]))):
        correct.append(str(numbers[hidden])[i])
    numbers[hidden] = ''

def draw(event = None):
    global text0, text1, text2, textSign, answer
    if answer == correct:
        generateProblem()
        canvas.itemconfig(text0, text = numbers[0], font=("Arial", 65, "bold"))
        canvas.itemconfig(text1, text = numbers[1], font=("Arial", 65, "bold"))
        canvas.itemconfig(text2, text = numbers[2], font=("Arial", 65, "bold"))
        canvas.itemconfig(textSign, text = sign)
    else:
        numbers[hidden] = ''
        if hidden == 0:
            canvas.itemconfig(text0, text='', font=("Arial", 65))
        if hidden == 1:
            canvas.itemconfig(text1, text='', font=("Arial", 65))
        if hidden == 2:
            canvas.itemconfig(text2, text='', font=("Arial", 65))

def redraw(number):
    global numbers, hidden, answer
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
        canvas.itemconfig(text0, text = str(numbers[hidden]), font = ("Arial", 65))
    if hidden == 1:
        canvas.itemconfig(text1, text = str(numbers[hidden]), font = ("Arial", 65))
    if hidden == 2:
        canvas.itemconfig(text2, text = str(numbers[hidden]), font = ("Arial", 65))

def one(event = None):
    redraw("1")
def two(event = None):
    redraw("2")
def three(event = None):
    redraw("3")
def four(event = None):
    redraw("4")
def five(event = None):
    redraw("5")
def six(event = None):
    redraw("6")
def seven(event = None):
    redraw("7")
def eight(event = None):
    redraw("8")
def nine(event = None):
    redraw("9")
def zero(event = None):
    redraw("0")
def back(event = None):
    redraw("-")

draw()
canvas.bind_all("<Return>", draw)
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
canvas.bind_all("<BackSpace>", back)

canvas.mainloop()