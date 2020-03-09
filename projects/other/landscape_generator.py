import tkinter
from random import randrange

window = tkinter.Canvas(height = 500, width = 500)
window.pack()

krok = 10
sirka = 2

def reset(self=None):
    farba = 'black'
    color = []
    window.delete('ALL')
    color = [[0 for x in range(500//sirka)] for y in range(500//sirka)]
    for x in range(500//sirka):
        for y in range(500//sirka):
            if x == 0 and y == 0:
                color[0][0] = randrange(0, 250//krok)*krok
            else:
                step = randrange(0, 2)
                if step == 0:
                    if y == 0:
                        color[x][y] = color[x-1][y]-krok
                        if color[x][y] < 0:
                            color[x][y] = 0
                    elif x == 0:
                        color[x][y] = color[x][y-1]-krok
                        if color[x][y] < 0:
                            color[x][y] = 0
                    else:
                        color[x][y] = (color[x-1][y]+color[x][y-1])//2//10*10-krok
                        if color[x][y] < 0:
                            color[x][y] = 0
                if step == 1:
                    if y == 0:
                        color[x][y] = int(color[x-1][y]+krok*1.4)
                        if color[x][y] > 250:
                            color[x][y] = 250
                    elif x == 0:
                        color[x][y] = int(color[x][y-1]+krok*1.4)
                        if color[x][y] > 250:
                            color[x][y] = 250
                    else:
                        color[x][y] = int((color[x-1][y]+color[x][y-1])//2//10*10+krok*1.4)
                        if color[x][y] > 250:
                            color[x][y] = 250
            if 0 <= color[x][y] < 50:
                farba = 'blue'
            elif 50 < color[x][y] < 100:
                farba = 'LightGoldenrod2'
            elif 100 < color[x][y] < 150:
                farba = 'green'
            elif 150 < color[x][y] < 200:
                farba = 'saddlebrown'
            elif 200 < color[x][y] <= 250:
                farba = 'white'
            window.create_rectangle(x*sirka, y*sirka, x*sirka+sirka, y*sirka+sirka, fill = farba, width = 0)

reset()
window.bind_all('r', reset)      

window.mainloop()