import tkinter

canvas = tkinter.Canvas(width = '300', height = '300', bg='white')
canvas.pack(side='right')

listbox = tkinter.Listbox(width='0')
listbox.pack()
farby = ['blue', 'green', 'red', 'brown', 'yellow', 'black', 'orange']
for prvok in farby:
    listbox.insert('end', prvok)

smer = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text = 'S', variable = smer, value = 1)
radiobutton1.pack()
radiobutton2 = tkinter.Radiobutton(text = 'J', variable = smer, value = 2)
radiobutton2.pack()
radiobutton3 = tkinter.Radiobutton(text = 'V', variable = smer, value = 3)
radiobutton3.pack()
radiobutton4 = tkinter.Radiobutton(text = 'Z', variable = smer, value = 4)
radiobutton4.pack()

x = 150
y = 150
def kresli():
    global x, y
    vybrane = listbox.curselection()
    if smer.get() == 1:
        canvas.create_line(x, y, x, y-10, fill=listbox.get(vybrane))
        y = y-10
    if smer.get() == 2:
        canvas.create_line(x, y, x, y+10, fill=listbox.get(vybrane))
        y = y+10
    if smer.get() == 3:
        canvas.create_line(x, y, x+10, y, fill=listbox.get(vybrane))
        x = x+10
    if smer.get() == 4:
        canvas.create_line(x, y, x-10, y, fill=listbox.get(vybrane))
        x = x-10

tlacidlo = tkinter.Button(text='kresli', command=kresli, width='10', bg='yellow', fg='red')
tlacidlo.pack()
