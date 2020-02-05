import  tkinter
from tkinter.colorchooser import askcolor

c = tkinter.Canvas()
c.pack()

b = tkinter.Button(command = askcolor)
b.pack()

c.mainloop()