import tkinter as tk
from Settings import *
from MenuState import MenuState

# TODO: hightscore??

root = tk.Tk()
root.title(settings['states']['menu']['window']['title'])
app = MenuState(master=root)
app.mainloop()
