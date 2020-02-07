import tkinter
from random import randint

canvas = tkinter.Canvas(width = 400, height = 100, background = "white")
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
textSign = canvas.create_text(125, 50, text = "", font = ("Arial", 65, "bold"))
text1 = canvas.create_text(200, 50, text = "", font = ("Arial", 65, "bold"))
textEquals = canvas.create_text(275, 50, text = "=", font = ("Arial", 65, "bold"))
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
    numbers[hidden] = '  '

def draw(event = None):
    global text0, text1, text2, textSign, answer
    generateProblem()
    canvas.itemconfig(text0, text = numbers[0])
    canvas.itemconfig(text1, text = numbers[1])
    canvas.itemconfig(text2, text = numbers[2])
    canvas.itemconfig(textSign, text = sign)

draw()
canvas.bind_all("<Return>", draw)

canvas.mainloop()