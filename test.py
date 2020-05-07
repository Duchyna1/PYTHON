import tkinter

canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

def tahanieMys(miesto):
    x = miesto.x
    y = miesto.y
    canvas.create_oval(x-2, y-2, x+2, y+2)
    subor = open('carbanica.txt', 'a')
    subor.write(str(x) + ' ' + str(y) + '\n')

def ulozit(klaves):
    canvas.quit()

def nacitat(klaves):
    subor = open('carbanica.txt', 'r')
    riadok = subor.readline()
    while riadok != '':
        a = riadok.split()
        x = int(a[0])
        y = int(a[1])
        canvas.create_oval(x-4, y-4, x+4, y+4, fill='red')
        riadok = subor.readline()

canvas.bind_all('<B1-Motion>', tahanieMys)
canvas.bind_all('k', ulozit)
canvas.bind_all('z', nacitat)

canvas.mainloop()